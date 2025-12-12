---
title: "Ph.D. Members"
layout: stacked
permalink: /phd-members/
author_profile: true
two_column: false
sections:
  - title: "Ph.D. Members"
    id: "phd-members"
---
{% assign fields_members = "Research Areas:research,Education:education,E-mail:email" | split: "," %}
{% assign phd_section = site.data.datacards.members.sections | where: "title", "PhD Members" | first %}

<!-- section: phd-members -->
{% include cards/generic-cards.html
   items=phd_section.members
   fields=fields_members
   title_key="name"
   subtitle_key="role"
   photo_key="photo"
   two_column=page.two_column %}
<!-- endsection -->
