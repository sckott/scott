---
layout: page
title: WebServices
---

## Fishbase API

API for <http://www.fishbase.org>

* source: [ropensci/fishbaseapi](https://github.com/ropensci/fishbaseapi)
* base URL <https://fishbase.ropensci.org>
* in collaboration w/ [Carl Boettiger][cboettig]

## USDA plants database API

API for <http://plants.usda.gov/java/>

* source: [sckott/usdaplantsapi](https://github.com/sckott/usdaplantsapi)
* base URL <https://plantsdb.xyz>

## rOpenSci API

API for <https://ropensci.org> packages, citations, etc.

* source: [ropensci/roapi](https://github.com/ropensci/roapi)
* base URL <https://roapi.org>

## TraitsDB API

API for traits data - very much a work in progress - would love your thoughts at <https://github.com/sckott/traitdb/issues/1>

* source: [sckott/traitdb](https://github.com/sckott/traitdb)
* base URL <https://traits.party/>

## Full Text DOI API

API for resolving DOIs to full text URLs (if available)

* source: [ropenscilabs/pubpatternsapi](https://github.com/ropenscilabs/pubpatternsapi)
* base URL <https://ftdoi.org/>

## Technologies used

* All above use the [Ruby Sinatra API framework](http://www.sinatrarb.com)
* Some use Docker, some do not
* MySQL or PostgreSQL or SQLite used as the DB
* Server is always [Caddy](https://caddyserver.com/)
* [Redis](http://redis.io/) used for caching for some (other's don't have caching)

[cboettig]: https://github.com/cboettig/
