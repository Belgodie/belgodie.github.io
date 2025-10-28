---
title: "Research"
layout: multi-section
permalink: /research/
author_profile: true
---

<div class="archive">
  <div class="page__inner-wrap">
    <h1 class="page__title">Research</h1>
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
  </div>
</div>

<div class="archive" id="publications">
  <div class="page__inner-wrap">
    <h1 class="page__title">Publications</h1>
    {% if site.author.googlescholar %}
      <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
    {% endif %}
    <hr class="section-divider">
    {% include publications_list.html %}
  </div>
</div>
