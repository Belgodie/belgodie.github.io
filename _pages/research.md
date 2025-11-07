---
title: "Research"
layout: stacked
permalink: /research/
# Each entry in `sections:` can use the knobs below:
#   title            -> visible heading text
#   id               -> anchor slug and marker used in <!-- section: id -->
#   collection       -> which Jekyll collection to pull items from (portfolio, publications, news, etc.)
#   filter           -> optional boolean flag to include items where that front-matter key is true (e.g., featured)
#   slugs            -> optional ordered list of specific items to show instead of the whole collection
#   sort             -> field used for ordering (defaults to date)
#   order            -> "asc" for ascending; omit for descending
#   limit            -> maximum number of items to display
#   style            -> card layout name (currently "project-row or project-column (+ columns and column_width)" or "publications" or 'news")
#   show_meta        -> set to false to hide project metadata line
#   cta_url / cta_label -> optional button under publication lists
#   link_field       -> what to use for the link icon ("url" to use the internal page URL // 'pdf' for /files/paper.pdf // 'paperurl' for doi.org from markdown file)
#   link_url         -> constant URL applied to every item (overrides link_field if present) - almost never used
#   link_external    -> true to open the icon link in a new tab (good for external sites) // false or omitted is same tab (good for internal pages) 
#   link_label_prefix -> optional text prepended to the accessible label for the icon (For screen readers)
# Any Markdown between <!-- section: id --> and <!-- endsection --> renders inside the card before the auto-generated list.
sections:
  - title: "Current Projects"
    id: "projects"
    collection: "portfolio"
    filter: "featured"
    style: "project-row"
    limit: 6
    
  - title: "Publications"
    id: "publications"
    collection: "publications"
    style: "publications"
    limit: 5
    link_field: "paperurl"
    link_external: true
    cta_url: "/publications/"
    cta_label: "See all publications"

  - title: "Recent News"
    id: "news"
    style: "news"
    collection: "news"
    limit: 5
    link_field: "link"
    link_external: true 

  #- title: "Acerca del Man"
  #  content: |
  #      literalmente tu content
---

<!-- section: projects -->
<!-- endsection -->

<!-- section: publications -->
You can also find my articles on [Google Scholar]({{ site.author.googlescholar }}).
<!-- endsection -->


