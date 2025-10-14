---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Health Technology, Technical University of Denmark, 2028 (expected)
* M.S. in Electrical Engineering, Korea Advanced Institute of Science and Technology, 2025
* B.Eng. in Electrical Engineering, Korea University 2022
  
Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Teaching Experience
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
