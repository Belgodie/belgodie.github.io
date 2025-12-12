---
title: "Home"
layout: stacked
permalink: /
author_profile: true
two_column: true
carousel_slides:
  - image: "/images/projects/PlatformOverview.webp"
    text: "Hola"
    #bgcolor: "rgba(255, 0, 0, 0.25)"
    bgopacity: 0.25
    textcolor: "#ffffffff"
  - image: "/images/projects/MatlabProject.svg"
    text: "Spike Sorting Toolkit"
    bgopacity: 0.25
    textcolor: "#ffffff"
sections:
  - title: "Research & Recent Work"
    id: "research-highlights"
---

<!-- section: research-highlights -->
<div class="home-hero-row">
  <div class="home-hero-row__left">
    {% include components/hero-carousel.html slides=page.carousel_slides %}
  </div>
  <div class="home-hero-row__right">
    {% assign recent = site.publications %}
    {% if page.recent_work_slugs %}
      {% assign recent = site.publications | where_exp: "doc", "page.recent_work_slugs contains doc.slug" %}
    {% endif %}
    {% assign recent = recent | sort: "date" | reverse %}
    {% assign recent = recent | slice: 0, 5 %}
    <div class="recent-work">
      <ul class="recent-work__list">
        {% for pub in recent %}
          <li class="recent-work__item">
            <div class="recent-work__title">
              {% if pub.paperurl %}
                <a href="{{ pub.paperurl }}" target="_blank" rel="noopener">{{ pub.title }}</a>
              {% else %}
                {{ pub.title }}
              {% endif %}
            </div>
            <div class="recent-work__meta">
              {% assign year = pub.date | date: "%Y" %}
              <span class="recent-work__year">{{ year }}</span>
              {% if pub.venue %}
                · <span class="recent-work__venue">{{ pub.venue }}</span>
              {% endif %}
              {% if pub.status %}
                · <span class="recent-work__status">{{ pub.status }}</span>
              {% endif %}
            </div>
          </li>
        {% endfor %}
      </ul>
    </div>
  </div>
</div>

<!-- endsection -->
