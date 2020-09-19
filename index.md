This page contains a list of UK MPs in order of how likely they are to give the source for numbers they use on Twitter.  It automatically updates once a week.

The method is a little bit of a blunt instrument, but it is surprisingly revealing

The code works like this:

*   download recent tweets by MPs.
*   take those that involve numbers (because we are interested in if the MP references their figures)
*   count how many of the tweets with numbers contain a URL.

So this is good:

[![Screen Shot 2014-11-23 at 12.42.57](https://i0.wp.com/joereddington.com/wp-content/uploads/2014/11/Screen-Shot-2014-11-23-at-12.42.57.png?resize=544%2C473)](https://i0.wp.com/joereddington.com/wp-content/uploads/2014/11/Screen-Shot-2014-11-23-at-12.42.57.png)

…and this is bad:

![Screen Shot 2014-11-23 at 12.42.46](https://i1.wp.com/joereddington.com/wp-content/uploads/2014/11/Screen-Shot-2014-11-23-at-12.42.46.png?resize=540%2C283)


This is a very low bar. Obviously the site could be to http://www.definatelynotaconspiricytheorist.com/, but at least that's a _start_.  

This project has had several iterations since 2014. You can view the first list [here](http://joereddington.com/4534/2014/11/24/the-list-of-uk-politicians-most-likely-to-be-making-up-facts./). I checked how good the idea was with humans [here](http://joereddington.com/5153/2015/04/28/does-your-mp-cite-their-sources-or-do-they-make-up-the-facts-find-out-here/) and it worked very well. 

All of the code is in [GitHub](https://github.com/joereddington/whichmpscitesources), and if you’d like to look at the list a single MPs you will find it [here](http://joereddington.com/mps_always/full/).

For the first list, [someone on reddit](https://www.reddit.com/r/unitedkingdom/comments/34ht2x/how_likely_is_your_mp_to_cite_sources_ranking/cqux0mj) said something very important:

> I think it’s pretty clear that the top 20% of those MPs are doing something right methodologically, compared to the bottom 20%. But I’d be careful of singling out any individual case with such a blunt tool. Especially if all 5 are from the same party

...and you should take that as your general guide. If your MP is in the bottom half of the table, there is probably something wrong. 

<table>
<tbody>
<tr>
<td>Ranking</td>
<td>Name</td>
<td>Twitter Handle</td>
<td>Tweets</td>
<td>Tweets with Figures</td>
<td>Sourced Tweets with Figures/td&gt;</td>
<td>Percentage</td>
</tr>
{% include list.html %}
</tbody>
</table>

This is a project by [Joe Reddington](https://joereddington.github.io/). It owes existence to a range of volunteers, anonymous internet commentators, and loved ones. The twitter handles came from the wonderful [MPs on Twitter](https://www.mpsontwitter.co.uk/ ) site.  
