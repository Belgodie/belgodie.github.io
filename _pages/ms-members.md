---
title: "M.S. Members"
layout: stacked
permalink: /ms-members/
author_profile: true
two_column: false
sections:
  - title: "M.S. Members"
    id: "ms-members"
---
{% assign fields_members = "Research Areas:research,Education:education,E-mail:email" | split: "," %}
{% assign ms_section = site.data.datacards.members.sections | where: "title", "MS Members" | first %}

<!-- section: ms-members -->
{% include cards/generic-cards.html
   items=ms_section.members
   fields=fields_members
   title_key="name"
   subtitle_key="role"
   photo_key="photo"
   two_column=page.two_column %}
<!-- endsection -->
