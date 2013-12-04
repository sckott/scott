---
layout: post
title: Notes on Stouffer et al. 2012 Science
author: Scott
tags:
- science
- networks
- bipartite
- notes
---

### Notes

+ title was "Evolutionary conservation of species' roles in food webs"
+ used 32 empirical food webs
+ questions were: 
	+ do species have consistent "roles" across different food webs they are embedded in, and
	+ are species roles phylogenetically conserved
+ Found that
	+ species roles (motifs) are conserved across different communities
	+ species benefit to the community (they call dynamic importance - bascially is the impact that the motif they are in has on community persistence simulations of the empirical networks) is homogenous - closely related species to have similar benefit to their community than expected at random
	+ at larger taxonomic scales, they show that phyla, classes, orders, and families, tend to play similar roles betlween New Zealand food webs, and all other food webs. 
+ Other questions
	+ What are the mechanisms for the evolutionary conservation of species roles?
		+ Is it related to similarity in traits?
		+ or possibly similarity in abundance?
	+ Is there conservation of species roles in mutualistic plant-pollinator networks?
		+ this paper only looked at food webs.
+ Potential problems
	+ they did not provide code, so can't necessarily replicate what they did
	+ can we look at where species are in motifs with bipartite networks?  that is, species of similar type (plants) can’t interact with one another
		+ probably: just means that motifs are of a more limited set, that is, whereas in a food web you can have a triangle, you can only have an open triangle in a bipartite network

![triangle](http://schamberlain.github.com/scott/img/triangle.png)

VS.

![triangle](http://schamberlain.github.com/scott/img/triangle_open.png)

+ Code: asked for code form Daniel Stouffer - it was not provided in the paper 

### How can we do something similar with bipartite networks?
+ Problems, in bipartite networks:
	+ there is no directionality to links, so that decreases the unique graphlets/motifs
+ Possible solutions:
	+ Use modules? (Olesen _et. al._ 2007) talk about modules as roles in bipartite networks, however this isn't the same as motifs. Motifs/graphlets are asking what roles do species play in substructures of the network, whereas with modules we can say whether a species plays the role of a module hub, network hub, connector, or peripheral (according to Olesen terminology).  But this isn't the same as motif/graphlets. 



{% highlight r %}
library(bipartite)
data(small1976)
res <- computeModules(small1976)  # takes several minutes!
plotModuleWeb(res)
{% endhighlight %}

![center](http://schamberlain.github.com/scott/img/modules.png) 

		
	+ Converting bipartite two-mode networks to one-mode networks
		+ One option is to convert two-mode bipartite networks into one-mode networks, which results in two one-mode networks, one for plants and one for pollinators.  Then, each one-mode network represents links shared by species in the same partite.  With this, one can look at motifs and graphlets, but what does that mean?  If a certain plant species X is found in a lot of motifs of a certain kind, does that tell us anything about the two-mode bipartite network of plant-pollinator interactions?


{% highlight r %}
library(tnet)
library(bipartite)

data(small1976)  # load small1976 network (it’s a matrix)
mat <- as.data.frame(small1976)  # convert to data.frame
mat <- mat[, 1:10]  # get samller matrix for ease
plotweb(mat)  # bipartite plot
{% endhighlight %}

![center](http://schamberlain.github.com/scott/img/twovsonemode1.png) 

{% highlight r %}
row.names(mat) <- NULL
mat_elist <- web2edges(mat, return = T)  # convert to edgelist
mat_onemode <- projecting_tm(mat_elist, method = "Newman")  # make into one-mode network
mat_onemode_i <- tnet_igraph(mat_onemode, directed = F)  # convert to igraph object for plotting
plot(mat_onemode_i)  # plot one-mode undirected graph
{% endhighlight %}

![NA](http://schamberlain.github.com/scott/img/twovsonemode2.png) 


	+ or maybe we can do this: 


{% highlight r %}
library(tnet)
library(bipartite)
library(reshape2)
library(ggplot2)

data(small1976)  # load small1976 network (it’s a matrix)
mat <- as.data.frame(small1976)  # convert to data.frame
mat <- mat[, 1:10]  # get samller matrix for ease
# plotweb(mat) # bipartite plot
row.names(mat) <- NULL
mat_elist <- web2edges(mat, return = T)  # convert to edgelist
onemode_plants <- projecting_tm(mat_elist, method = "Newman")  # make into one-mode network

# Insects (columns of mat)
mat2 <- matrix(c(mat_elist[, 2], mat_elist[, 1], mat_elist[, 3]), ncol = 3)  # rearrange to get pollinators in first column
onemode_pollinators <- projecting_tm(mat2, method = "Newman")  # make into one-mode network

# Combine into one matrix
dimnames(mat_elist)[[2]] <- c("i", "j", "w")
dimnames(onemode_plants)[[2]] <- c("i", "j", "w")
dimnames(onemode_pollinators)[[2]] <- c("i", "j", "w")
ee <- rbind(mat_elist, onemode_plants, onemode_pollinators)
ee_ <- dcast(ee, i ~ j, value.var = "w")
ee_[is.na(ee_)] <- 0
row.names(ee_) <- ee_[, 1]
ee_ <- ee_[, -1]

# Plotting it
ee__ <- tnet_igraph(ee, directed = F)
plot(ee__)  # where noddes 1-13 are plants, and 14-23 are pollinators
{% endhighlight %}

![center](http://schamberlain.github.com/scott/img/other.png) 


Basically a network of plant-pollinator interactions together with the putative competitive/facilitative interactions within each partite (plants and pollinators). Obviously this graph needs coloring for the different types of nodes...


*********
#### Get the .Rmd file used to create this post [at my github account](https://github.com/SChamberlain/scott/blob/master/_drafts/2012-09-20-network-roles.Rmd) - or [.md file](https://github.com/SChamberlain/scott/tree/master/_posts/2012-09-20-network-roles.md).

#### Written in [Markdown](http://daringfireball.net/projects/markdown/), with help from [knitr](http://yihui.name/knitr/), and nice knitr highlighting/etc. in in [RStudio](http://rstudio.org/).

*********
#### References
<p>Olesen JM, Bascompte J, Dupont YL and Jordano P (2007).
&ldquo;The Modularity of Pollination Networks.&rdquo;
<EM>Proceedings of The National Academy of Sciences</EM>, <B>104</B>.
ISSN 0027-8424, <a href="http://dx.doi.org/10.1073/pnas.0706375104">http://dx.doi.org/10.1073/pnas.0706375104</a>.