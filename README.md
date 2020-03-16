# oTree App for Infinitely Repeated Prisoner's Dilemma
### Salvatore Nunnari, Bocconi University, salvatore.nunnari@unibocconi.it

This repository contains one oTree app:

* **prisoner**: infinitely repeated prisoner's dilemma (with discount factor implemented as random termination rule) as in the experiments by Dal Bò, Pedro and Guillaume R. Fréchette (2011), "The Evolution of Cooperation in Infinitely Repeated Games: Experimental Evidence", American Economic Review, 101(1): 411-429. 

If "time_limit==False", the app implements "num_matches" instances of an infinitely repeated game. If "time_limit==True", the app implements as many instances of an infinitely repeated game as subjects are able to play in "time_limit_seconds" (as in Dal Bò and Fréchette 2011, where the last match of each session was the first match to end after 60 minutes from the beginning of the experiment). 

This app was developed with oTree version 2.5.5.
