---
name: easier-models
layout: post
title: Easier model diagnostics function
date: 2012-12-10
author: Scott Chamberlain
tags: 
- R
- data
- model
- statistics
- ggplot2
---

It's a pain to write a bunch of lines of code to do model diagnostics. This little function does a nice job of putting out a number of diagnostic plots, and the gives the ANOVA table too, with an option to just write the ANOVA table out as a data.frame so you can easily combine many ANOVA tables for easy writing to CSV for instance. 

***************

### The function

{% highlight r %}
fitmod <- function(equation, data, gimme = FALSE) {
    conn_mod1 <- lm(equation, data = data)  # run model
    m1 <- fortify(conn_mod1, data)  # adds model residuals/etc to original data.frame
    anov <- Anova(conn_mod1, type = 3)  # so we can get type III SS
    a <- ggplot(m1, aes_string(x = as.character(equation)[[2]])) + geom_histogram()
    b <- qplot(.fitted, .stdresid, data = m1, geom = "point")
    c <- qplot(.stdresid, data = m1, geom = "histogram")
    if (gimme) {
        temp <- data.frame(anov[1:4])
        temp$vars <- row.names(temp)
        temp
    } else {
        list(list(anov), do.call(grid.arrange, list(a, b, c)))
    }
}
{% endhighlight %}


***************

### Just run the model and give results and diagnostic plots. This gives a histogram of the response variable, a plot of the fitted numbers vs. residuals, and a histogram of the residuals.

{% highlight r %}
library(car); library(ggplot2)

fitmod(Sepal.Length ~ Sepal.Width * Species, iris)
{% endhighlight %}


![center](http://sckott.github.com/scott/img/outputall.png) 

{% highlight text %}
Response: Sepal.Length
                    Sum Sq  Df F value  Pr(>F)    
(Intercept)           4.12   1   21.32 8.5e-06 ***
Sepal.Width           3.36   1   17.36 5.3e-05 ***
Species               0.50   2    1.29    0.28    
Sepal.Width:Species   0.16   2    0.41    0.67    
Residuals            27.85 144                    
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 
{% endhighlight %}


***************

### Or you can run the model and get just the ANOVA table back as a data.frame that can be combined with others, e.g., to write to a CSV file

{% highlight r %}
library(plyr)
# Simple example
fitmod(Sepal.Length ~ Sepal.Width * Species, iris, gimme = TRUE)
{% endhighlight %}



{% highlight text %}
                     Sum.Sq  Df F.value    Pr..F.                vars
(Intercept)          4.1233   1 21.3225 8.526e-06         (Intercept)
Sepal.Width          3.3569   1 17.3592 5.311e-05         Sepal.Width
Species              0.4982   2  1.2881 2.790e-01             Species
Sepal.Width:Species  0.1572   2  0.4064 6.668e-01 Sepal.Width:Species
Residuals           27.8465 144      NA        NA           Residuals
{% endhighlight %}



{% highlight r %}

# Or do many in lapply call to combine them
mymods <- list(Sepal.Length ~ Sepal.Width * Species, Petal.Length ~ Petal.Width * 
    Species)
out <- llply(mymods, function(x) fitmod(x, iris, TRUE))
names(out) <- c("mod1", "mod2")
ldply(out)
{% endhighlight %}



{% highlight text %}
    .id  Sum.Sq  Df  F.value    Pr..F.                vars
1  mod1  4.1233   1  21.3225 8.526e-06         (Intercept)
2  mod1  3.3569   1  17.3592 5.311e-05         Sepal.Width
3  mod1  0.4982   2   1.2881 2.790e-01             Species
4  mod1  0.1572   2   0.4064 6.668e-01 Sepal.Width:Species
5  mod1 27.8465 144       NA        NA           Residuals
6  mod2 13.4329   1 102.8050 1.448e-18         (Intercept)
7  mod2  0.1625   1   1.2438 2.666e-01         Petal.Width
8  mod2  6.7474   2  25.8196 2.614e-10             Species
9  mod2  2.0178   2   7.7213 6.525e-04 Petal.Width:Species
10 mod2 18.8156 144       NA        NA           Residuals
{% endhighlight %}



*********
#### Get the .Rmd file used to create this post [at my github account](https://github.com/sckott/scott/blob/gh-pages/_drafts/2012-12-10-easier-models.Rmd) - or [.md file](https://github.com/sckott/scott/blob/gh-pages/_posts/2012-12-10-easier-models.md).

#### Written in [Markdown](http://daringfireball.net/projects/markdown/), with help from [knitr](http://yihui.name/knitr/).
