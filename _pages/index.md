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
  - title: ""
    id: "welcome-news"
    layout: "row"
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

<!-- section: welcome-news -->
{% capture welcome_body %}
<div class="wrap-card">
  <img src="{{ '/images/welcome.png' | relative_url }}" alt="Welcome" class="wrap-card__img">
  <div class="wrap-card__text">
    Welcome to my research page! Here you will find information about my work in microfluidic systems, biosensors, and organ-on-chip technologies. Feel free to explore my projects, publications, and get in touch if you are interested in collaborating or learning more. I am especially interested in collaborations that bring together microfabrication, microfluidics, and signal processing.
  </div>
</div>
{% endcapture %}

{% capture news_body %}
{% assign news_items = site.news | sort: "date" | reverse | slice: 0, 5 %}
<ul class="home-news__list">
  {% for item in news_items %}
    <li class="home-news__item">
      <div class="home-news__blurb">
        {{ item.content
           | markdownify
           | replace: "<p>", ""
           | replace: "</p>", ""
           | strip
           | strip_newlines
           | replace: "\r", " "
           | replace: "\n", " "
           | truncate: 220 }}
        {% if item.link %}
          <a class="home-news__link-icon" href="{{ item.link }}" target="_blank" rel="noopener" aria-label="Open link">
            <i class="fas fa-link" aria-hidden="true"></i>
          </a>
        {% endif %}
      </div>
      <div class="home-news__date home-news__date--below">{{ item.date | date: "%b, %Y" }}</div>
    </li>
  {% endfor %}
</ul>
{% endcapture %}

{% include row-two-cards.html
   left_title="Welcome"
   left_md=welcome_body
   right_title="Recent News"
   right_md=news_body %}
<!-- endsection -->
