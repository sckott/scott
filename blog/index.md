---
layout: page
title: Scott Chamberlain's Lab Notebook
---

This is my open lab notebook where I talk about what I'm doing in research, thoughts, analyses, etc.

<div id="posts">
  <h1>Blog posts</h1>
    {% for post in site.posts %}
		<code>{{ post.date | date_to_string }}</code> » <span class='post-title'><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></span><br /><span class='meta'>Tags: {% for tag in post.tags %}{{ tag | array_to_sentence_string }}{% endfor %}</span><p />
    {% endfor %}
</div>