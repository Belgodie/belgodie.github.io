---
title: "Members"
layout: stacked
permalink: /members/
author_profile: true
two_column: false  # set to false for single-column layout
fields_members:
  - research
  - education
  - email
sections:
  - title: "Ph.D. Members"  # display title on page
    id: "phd-members"
    data_title: "PhD Members"  # title used to look up data section in members.yml
    include: datacard-section.html
  - title: "M.S. Members"  # display title on page
    id: "ms-members"
    data_title: "MS Members"  # title used to look up data section in members.yml
    include: datacard-section.html
---
<!-- Content handled by member-section.html include via stacked layout -->
