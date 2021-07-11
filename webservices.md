---
layout: page
title: WebServices
---

## CRAN checks API

API for software check results for the R package distribution network <https://cran.rstudio.com/web/packages/>

* source: [sckott/cchecksapi](https://github.com/sckott/cchecksapi)
* base URL <https://cranchecks.info/>

## Technologies used across projects

* [Ruby Sinatra API framework](http://www.sinatrarb.com)
* Some use Docker, some do not
* MySQL or PostgreSQL or SQLite used as the DB
* Server is always [Caddy](https://caddyserver.com/)
* [Redis](http://redis.io/) used for caching for some (other's don't have caching)

--------

## No longer maintained

Or **I** am no longer involved in maintaining.

### Fishbase API

API for <https://www.fishbase.de/>

* source: [ropensci/fishbaseapi](https://github.com/ropensci/fishbaseapi)
* base URL <https://fishbase.ropensci.org>
* mainted by [Carl Boettiger][cboettig]

### BIEN API

API for Botanical Information and Ecology Network data <http://bien.nceas.ucsb.edu/bien/>

* source: [sckott/bienapi](https://github.com/sckott/bienapi)
* base URL <https://bienapi.xyz/>

### Full Text DOI API

API for resolving DOIs to full text URLs (if available)

* source: [ropenscilabs/pubpatternsapi](https://github.com/ropenscilabs/pubpatternsapi)
* base URL <https://ftdoi.org/>

### USDA plants database API

API for <http://plants.usda.gov/java/>

* source: [sckott/usdaplantsapi](https://github.com/sckott/usdaplantsapi)
* base URL <https://plantsdb.xyz>

### rOpenSci API - 

API for <https://ropensci.org> packages, citations, etc.

* source: [ropensci/roapi](https://github.com/ropensci/roapi)
* base URL <https://roapi.org>

### TraitsDB API - no longer maintained

API for traits data - very much a work in progress - would love your thoughts at <https://github.com/sckott/traitdb/issues/1>

* source: [sckott/traitdb](https://github.com/sckott/traitdb)
* base URL <https://traits.party/>


[cboettig]: https://github.com/cboettig/
