---
title: "Alumni"
layout: stacked
permalink: /alumni/
author_profile: true
two_column: false
sections:
  - title: "Alumni"
    id: "alumni"
---
{% assign fields_members = "Research Areas:research,Education:education,E-mail:email" | split: "," %}
{% assign alumni_section = site.data.datacards.members.sections | where: "title", "Alumni" | first %}

<!-- section: alumni -->
{% include cards/generic-cards.html
   items=alumni_section.members
   fields=fields_members
   title_key="name"
   subtitle_key="role"
   photo_key="photo"
   two_column=page.two_column %}
<!-- endsection -->
