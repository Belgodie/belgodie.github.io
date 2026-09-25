"""Give paper files in files/papers/ uninformative names and keep a private index of what is what.

Each paper in _publications/ gets a random 4-digit number, saved once in its file as `file_id:`.
Its local files are then renamed after that number, by role:

    pdf:          ->  files/papers/4817.pdf
    thumbnail:    ->  files/papers/4817-fig.jpg
    cover_image:  ->  files/papers/4817-cover.jpg

and the paper file is updated to point at the new names. Web addresses (e.g. a publisher's
open-access PDF) and files outside files/papers/ are left alone. Running it again changes nothing
unless a paper has new, not-yet-renamed files.

It also writes files/papers/INDEX.local.txt (number -> paper). That file is git-ignored, so it never
leaves your computer; running the script on another computer recreates it.

Usage (from the repository root):
    python scripts/obscure_papers.py            # rename + update + write the index
    python scripts/obscure_papers.py --dry-run  # only show what would change
"""

import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLICATIONS = os.path.join(ROOT, "_publications")
PAPERS_URL = "/files/papers/"
PAPERS_DIR = os.path.join(ROOT, "files", "papers")
INDEX_FILE = os.path.join(PAPERS_DIR, "INDEX.local.txt")

# front-matter field -> suffix added after the number
ROLES = [("pdf", ""), ("thumbnail", "-fig"), ("cover_image", "-cover")]

# `key: value   # optional comment` (value optionally quoted); commented-out lines never match
FIELD_LINE = r'^({key}):(\s*)(["\']?)([^"\'#\s]+)\3(\s*#.*)?$'


def front_matter(text):
    """Return (start, end) character offsets of the YAML front matter body."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    if not match:
        return None
    return match.start(1), match.end(1)


def read_field(body, key):
    match = re.search(FIELD_LINE.format(key=key), body, re.M)
    return match.group(4) if match else None


def set_field(body, key, value):
    """Replace the value of `key`, keeping its quotes and trailing comment."""
    pattern = re.compile(FIELD_LINE.format(key=key), re.M)
    return pattern.sub(lambda m: m.group(1) + ":" + m.group(2) + m.group(3) + value + m.group(3) + (m.group(5) or ""), body, count=1)


def read_title(body):
    match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', body, re.M)
    return match.group(1) if match else "(no title)"


def used_numbers(papers):
    numbers = {p["file_id"] for p in papers if p["file_id"]}
    if os.path.isdir(PAPERS_DIR):
        for name in os.listdir(PAPERS_DIR):
            match = re.match(r"^(\d{4})(-[a-z]+)?\.", name)
            if match:
                numbers.add(match.group(1))
    return numbers


def main():
    dry_run = "--dry-run" in sys.argv
    papers = []
    for name in sorted(os.listdir(PUBLICATIONS)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(PUBLICATIONS, name)
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        span = front_matter(text)
        if not span:
            print("skip (no front matter): " + name)
            continue
        body = text[span[0]:span[1]]
        papers.append({"name": name, "path": path, "text": text, "span": span, "body": body,
                       "file_id": read_field(body, "file_id")})

    taken = used_numbers(papers)
    renames, index_rows, changed_files = [], [], []

    for paper in papers:
        body = paper["body"]
        local = []
        for key, suffix in ROLES:
            value = read_field(body, key)
            if value and value.startswith(PAPERS_URL):
                local.append((key, suffix, value))
            elif value and value.startswith("/"):
                print("note: {}: {} points outside {} ({}), left as is".format(paper["name"], key, PAPERS_URL, value))

        number = paper["file_id"]
        if local and not number:
            number = str(random.randint(1000, 9999))
            while number in taken:
                number = str(random.randint(1000, 9999))
            taken.add(number)
            # add `file_id:` just above the first file field
            first_key = local[0][0]
            body = re.sub(r"^(" + first_key + r":)", "file_id: " + number + "   # random number used to name this paper's files (scripts/obscure_papers.py)\n\\1", body, count=1, flags=re.M)

        paper_files = []
        for key, suffix, value in local:
            old_name = value[len(PAPERS_URL):]
            extension = os.path.splitext(old_name)[1].lower()
            new_name = number + suffix + extension
            paper_files.append(new_name)
            if old_name == new_name:
                continue
            old_path = os.path.join(PAPERS_DIR, old_name)
            new_path = os.path.join(PAPERS_DIR, new_name)
            if not os.path.exists(old_path):
                print("warning: {}: {} file not found: {} (paper file not changed for it)".format(paper["name"], key, value))
                continue
            if os.path.exists(new_path) and os.path.normcase(old_path) != os.path.normcase(new_path):
                sys.exit("error: {} already exists; not overwriting it".format(new_path))
            renames.append((old_path, new_path, old_name, new_name))
            body = set_field(body, key, PAPERS_URL + new_name)

        if body != paper["body"]:
            start, end = paper["span"]
            changed_files.append((paper["path"], paper["text"][:start] + body + paper["text"][end:]))

        if number:
            index_rows.append((number, paper["name"], read_title(body), paper_files))

    for old_path, new_path, old_name, new_name in renames:
        print("{}  {} -> {}".format("would rename" if dry_run else "renamed", old_name, new_name))
        if not dry_run:
            os.rename(old_path, new_path)
    for path, text in changed_files:
        print("{}  {}".format("would update" if dry_run else "updated", os.path.relpath(path, ROOT)))
        if not dry_run:
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(text)

    lines = ["Private index of files/papers/ - generated by scripts/obscure_papers.py, git-ignored (never uploaded).", ""]
    for number, name, title, files in sorted(index_rows):
        lines.append("{}  {}".format(number, title))
        lines.append("      paper file: _publications/{}".format(name))
        lines.append("      files:      {}".format(" · ".join(files) if files else "(none local)"))
        lines.append("")
    if dry_run:
        print("\n--- index that would be written to files/papers/INDEX.local.txt ---\n" + "\n".join(lines))
    else:
        with open(INDEX_FILE, "w", encoding="utf-8") as handle:
            handle.write("\n".join(lines))
        print("index written: files/papers/INDEX.local.txt")
    if not renames and not changed_files:
        print("nothing to rename - all paper files already use their numbers")


if __name__ == "__main__":
    main()
