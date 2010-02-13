Typy!
======

Typy is a pygame-based typing game planned out and conceived by
ET and myself (she's big on typing games).


The plan
---------
The concept is fairly simple, using stories (i.e. nursery rhymes) 
words will scroll from right to left at variable rates of speed 
(depending on the level) and the player must type the words as they
appear on the screen. 

When the player types the correct word and hits "space",
just as if they were writing the story themselves one of two things
will happen:

  * **Correct**: Player receives a number of *coins* based on the length of the word and its difficulty
  * **Wrong**: *Coins* are detracted from the player's coin purse

At the end of a round (or story) the player will visit the **store**,
where they can purchase "tools". These tools can then be used in the next
round of play, allowing the player to advance further or get themselves out
of tight jams. Tools will be invoked by the user hitting "enter" which will
slow the speed of the words and give the player a few seconds to type in the
name of the tool that they would like to use, i.e. for the "ice" tool the player
would have to type in i-c-e to enable the tool. 

If the user accumulates a large amount of coins, they can buy more interesting tools
or more interesting stories as they start to collect more and more coins


Unanswered Questions
---------------------

  * Can/should the player be able to fetch/scrape stories from a site or copy/paste them into a dialog to "play" with that story?
  * How to gauge "difficulty" of a particular word
  * High-scores sharing?
  * Saving player's coins between invocations of the game?

