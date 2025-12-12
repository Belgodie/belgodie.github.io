# Row Two Cards – Usage Notes

This include renders two stacked cards side by side using the same markup/padding as your other stacked cards. Alignment is handled by a small margin reset in `custom.scss` scoped to this row (`.home-split-cards .stacked-card__body > * { margin-top: 0; }`), so you don’t need flex/height hacks.

## How to use in a page
1) Define a section in front matter with `layout: row` (no children needed):
   ```yaml
   sections:
     - id: my-two-up
       layout: row
   ```
2) In the body for that section, capture left/right content (Markdown), then call the include:
   ```liquid
   <!-- section: my-two-up -->
   {% capture left_body %}
   Your left card content in Markdown.
   {% endcapture %}

   {% capture right_body %}
   Your right card content in Markdown.
   {% endcapture %}

   {% include row-two-cards.html
      left_title="Left Title"
      left_md=left_body
      right_title="Right Title"
      right_md=right_body %}
   <!-- endsection -->
   ```
3) If you prefer to render an include instead of Markdown on either side, use `left_include` or `right_include` in place of `left_md`/`right_md`.

## Notes
- Titles are optional; omit `left_title`/`right_title` if you want only body text.
- The grid uses the existing `.home-split-cards` spacing (auto-fit minmax(320px, 1fr) with a gap).
- The margin reset keeps the first visible element in both cards aligned; avoid adding extra top margins inside the captured Markdown.
