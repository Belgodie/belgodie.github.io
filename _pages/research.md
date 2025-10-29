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
#   style            -> card layout name (currently "projects" or "publications")
#   show_meta        -> set to false to hide project metadata line
#   cta_url / cta_label -> optional button under publication lists
#   link_field       -> front-matter field to use for the link icon (set to "url" to use the page URL)
#   link_url         -> constant URL applied to every item (overrides link_field if present)
#   link_external    -> true to open the icon link in a new tab
#   link_label_prefix -> optional text prepended to the accessible label for the icon
# Any Markdown between <!-- section: id --> and <!-- endsection --> renders inside the card before the auto-generated list.
sections:
  - title: "Current Projects"
    id: "projects"
    collection: "portfolio"
    filter: "featured"
    style: "projects"
    limit: 6
    link_field: "url"
  - title: "Publications"
    id: "publications"
    collection: "publications"
    style: "publications"
    limit: 5
    link_field: "url"
    cta_url: "/publications/"
    cta_label: "See all publications"
---

<!-- section: projects -->
<!-- endsection -->

<!-- section: publications -->
You can also find my articles on [Google Scholar]({{ site.author.googlescholar }}).
<!-- endsection -->


