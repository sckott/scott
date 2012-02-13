---
layout: post
title: Will a GitHub publishing model work?
author: Scott
tag:
- github
- thoughts
- publishing
---

# Introduction

Publishing and publishers are stagnant, and have not innovated much in a long time, save a few such as [Public Library of Science or PLoS][plos]. 

Beyond PLoS, some experiments in publishing are taking place, including:

* [Annotum][]: an "open-source, open-process, open-access scholarly authoring and publishing platform based on WordPress"

* [Scholastica][]: a peer-review, manuscript handling web-based platform. 

* [Peerage of Science][pos]: a web service for "automatically controlled, standardized, rigorous, fully anonymous scientific peer review"

* [GigaScience][]: online open-access open-data journal, with big-data studies, links standard manuscript publication with database for associated data, data anlaysis tools, and cloud-computing resources. 

All these publishing innovations are great.  But, I think we need more, as do others.  A few weeks ago, a number of us discussed on Twitter the possibility of a publishing model based on [GitHub][].  (Marcio von Muhlen had a blog post in April last year titled ["We need a GithHub of science"][post] - which I should point out here as it is relavant.) 

# The proposal

What would a GitHub hosted journal look like?  I think there are three technological/software components (not counting human components of reviewers editors, etc.):

1. Web platform/database for hosting manuscripts in various stages from just submitted to revisions to published.  

2. Review system, including database of reviewers, the reviews themselves, etc.

3. A frontend to present the papers/etc, submit manuscripts, and CSS to make it all look pretty. 

In my opinion, GitHub can play a major role in numbers (1) and (3).  In (1), the git based versioning of code could also be used to submit and handle papers.  In addition, wrt (3), [GitHub Pages][ghpages] is a way to present content in a static web page from one of the branches of your GitHub repository.  See [here][] for a growing list of websites hosted on GitHub pages.  Presenting published and early view papers, etc. doesn't need to have some insane website, so this could be a cheap way to do it. And you can use a custom domain name for the journal, e.g., go from myjournal.github.com to myjournal.com.  

As for (2), the above-mentioned Scholastica or Peerage of Science could be an option for handling peer reviews.  

# Disadvantages and advantages

## The disadvantages
So a GitHub hosted journal has obivous drawbacks...

* Technical knowhow: Some scientists may not know how to use git, and if papers have to be submitted in Latex, then you will eliminate many potential authors possibly.

* There aren't rich web markup tools. 

* Others?

## The advantages
...and advantages

* Completely open: A GitHub journal would be completely open, so that the public/scientists could see everything that was going on in the journal, including all the manuscript revisions, and reviews if they were done on GitHub, or at least mirrored to GitHub. 

* API: GitHub has a built in API, so we don't have to build one ourselves. 

* Versioning: manuscripts would include automatic versioning, including tracking down to the periods that were changed between versions

* Metrics: GitHub has built in metrics on "watchers", "followers", and for clones and forks, among other things. In addition, we could pull altmetrics data from the [TotalImpact][] API, and present those data associated with papers on the rendered website for the journal. Of course, anyone could hit the TotalImpact, or GitHub APIs themselves for these metrics too. 

* Pull requests: maybe pull requests could be used to submit papers.  

The question is do these advantages outweigh the potential drawbacks.  I don't know the answer to this question, but I think this conversation is worth having. 

# What would the structure look like on GitHub?
Maybe like this:

<iframe src="https://docs.google.com/presentation/embed?id=1J7DSxk0H90NVcRvPhug4UYcH_pCngMWO7-aIeqAxIeA&start=false&loop=false&delayms=3000" frameborder="0" width="480" height="389" allowfullscreen="true" webkitallowfullscreen="true"></iframe>

# What do you think?

What do you think?  Does this journal idea sound feasible? Should we just start a journal hosted on GitHub and see what happens?


[plos]: http://www.plos.org/publications/journals/
[Annotum]: http://annotum.org/ 
[Scholastica]: http://scholasticahq.com/
[pos]: http://www.peerageofscience.org/
[GigaScience]: http://www.gigasciencejournal.com/
[post]: http://marciovm.com/i-want-a-github-of-science/index.html
[GitHub]: https://github.com/
[ghpages]: http://pages.github.com/ 
[here]: https://github.com/mojombo/jekyll/wiki/sites
[TotalImpact]: http://totalimpact.org/
