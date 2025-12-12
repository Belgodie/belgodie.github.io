## Datacards guide

Use this folder to store reusable data for card-style layouts (people, publications, courses, etc.). The cards render via `_includes/cards/generic-cards.html`, which you configure from your page.

### How the generic include works
```
{% include cards/generic-cards.html
   items=...          # array of items to render
   fields=...         # array of "Label:key" strings
   title_key="..."    # key for the main title
   subtitle_key="..." # key for the subtitle (optional)
   photo_key="..."    # key for photo URL (optional)
   initials_key="..." # key for initials fallback (optional)
   two_column=true %} # optional grid layout
```

`fields` is a comma-separated string that gets split into an array. Each entry is `Label:key`, so the include knows which label to show and which key to read from each item.

### Example data shapes

**Members with sections** (`_data/datacards/members.yml`):
```yaml
sections:
  - title: "PhD Members"
    members:
      - name: "Da Phuc"
        role: "PhD Candidate"
        research: "Flexible Electronics"
        education:
          - "2021 • M.S. in Biotechnology, Fresno"
          - "2019 • B.S. in Chemistry, Fresno"
        email: "da.phuc@example.edu"
        photo: "/images/members/daphuc.png"
  - title: "MS Members"
    members:
      - name: "Alma Marcela Gozo"
        role: "Master Student"
        research: "Flexible Microfluidics"
        education: "2022 • B.S. in Mechanical Engineering, USFQ"
        email: "alma.marcela.gozo@example.edu"
        photo: "/images/members/almamarcelagozo.png"
```

**Publications (no sections)** (`_data/datacards/pubs.yml`):
```yaml
- title: "Bio-inspired soft microgripper"
  journal: "Soft Robotics"
  authors: "A. Author, B. Author, C. Author"
  published: "2024"
  link: "https://doi.org/10.1234/example"
  photo: "/images/pubs/gripper.png"
```

**Courses (no sections)** (`_data/datacards/courses.yml`):
```yaml
- class: "EECS 210: Intro to Embedded Systems"
  university: "Example University"
  description: "Foundations of microcontrollers, interrupts, low-level I/O."
  photo: "/images/courses/eecs210.png"
```

### Rendering on a page

**Sectioned data (e.g., Members):**
```liquid
{% assign fields_members = "Research Areas:research,Education:education,E-mail:email" | split: "," %}
{% assign phd_section = site.data.datacards.members.sections | where: "title", "PhD Members" | first %}
{% include cards/generic-cards.html
   items=phd_section.members
   fields=fields_members
   title_key="name"
   subtitle_key="role"
   photo_key="photo"
   two_column=true %}
```
Repeat for other sections (MS, Undergrad) by changing the section title and `items`.

**Flat data (e.g., Publications):**
```liquid
{% assign pubs = site.data.datacards.pubs %}
{% assign fields = "Paper Title:title,Journal:journal,Authors:authors,Published:published,Link:link" | split: "," %}
{% include cards/generic-cards.html
   items=pubs
   fields=fields
   title_key="title"
   subtitle_key="journal"
   photo_key="photo"
   two_column=true %}
```

**Another flat example (Courses):**
```liquid
{% assign courses = site.data.datacards.courses %}
{% assign fields = "Class:class,University:university,Description:description" | split: "," %}
{% include cards/generic-cards.html
   items=courses
   fields=fields
   title_key="class"
   subtitle_key="university"
   photo_key="photo"
   two_column=true %}
```

### Notes
- `fields` controls the labels and which keys to pull from each item.
- If you don’t have a photo, omit `photo_key` or leave the value empty.
- `two_column` enables the responsive two-column grid; set to `false` for single column.
- The styling is reused from the existing card styles (`.group-member*`) defined in `_sass/custom.scss`.
