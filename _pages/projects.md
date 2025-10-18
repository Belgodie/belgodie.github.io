---
title: "Projects"
layout: single
permalink: /projects/
---

<div class="projects-grid">
  {% for item in site.portfolio %}
    <article class="project-card">
    {% if item.header and item.header.teaser %}
        <div class="project-teaser">
        <img src="{{ item.header.teaser | relative_url }}" alt="{{ item.header.alt | default: item.title }}" loading="lazy">
        </div>
    {% endif %}
    <h3 class="project-title">{{ item.title }}</h3>
    {% if item.excerpt %}
        <p class="project-excerpt">{{ item.excerpt | markdownify | strip_html }}</p>
    {% endif %}
    </article>
  {% endfor %}
</div>