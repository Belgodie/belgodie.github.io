---
title: "Members"
layout: stacked
permalink: /members/
author_profile: true
two_column: false  # set to false for single-column layout
sections:
  - title: "PhD Members"
    id: "phd-members"
  - title: "MS Members"
    id: "ms-members"
  - title: "Undergrad Members"
    id: "undergrad-members"
  - title: "Courses"
    id: "courses"
  - title: "Alumni"
    id: "alumni"
---
{% assign fields_members = "Research Areas:research,Education:education,E-mail:email" | split: "," %}

<!-- section: phd-members -->
{% assign phd_section = site.data.datacards.members.sections | where: "title", "PhD Members" | first %}
{% include cards/generic-cards.html
   items=phd_section.members
   fields=fields_members
   title_key="name"
   subtitle_key="role"
   photo_key="photo"
   two_column=page.two_column %}
<!-- endsection -->

<!-- section: ms-members -->
{% assign ms_section = site.data.datacards.members.sections | where: "title", "MS Members" | first %}
{% include cards/generic-cards.html
   items=ms_section.members
   fields=fields_members
   title_key="name"
   subtitle_key="role"
   photo_key="photo"
   two_column=page.two_column %}
<!-- endsection -->

<!-- section: undergrad-members -->
{% assign ug_section = site.data.datacards.members.sections | where: "title", "Undergrad Members" | first %}
{% include cards/generic-cards.html
   items=ug_section.members
   fields=fields_members
   title_key="name"
   subtitle_key="role"
   photo_key="photo"
   two_column=page.two_column %}
<!-- endsection -->


<!-- section: courses -->
{% assign courses = site.data.datacards.courses %}
{% assign fields = "Class:class,University:university,Description:description" | split: "," %}
{% include cards/generic-cards.html
   items=courses
   fields=fields
   title_key="class"
   subtitle_key="university"
   photo_key="photo"
   two_column=false %}
<!-- endsection -->

<!-- section: alumni -->
{% assign alumni_section = site.data.datacards.members.sections | where: "title", "Alumni" | first %}
{% include cards/generic-cards.html
   items=alumni_section.members
   fields=fields_members
   title_key="name"
   subtitle_key="role"
   photo_key="photo"
   two_column=page.two_column %}
<!-- endsection -->
