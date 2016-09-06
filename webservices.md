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

## GBIDS API

API for ID checking and conversion for Genbank IDs

* source: [sckott/gbids](https://github.com/sckott/gbids)
* base URL <https://gbids.xyz>

## Technologies used

* All above use the [Ruby Sinatra API framework](http://www.sinatrarb.com)
* Some use Docker, some do not
* MySQL or PostgreSQL used as the DB
* Server is [Caddy](https://caddyserver.com/) for all
* [Redis](http://redis.io/) used for caching for all

[cboettig]: https://github.com/cboettig/
