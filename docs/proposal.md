# PROPOSAL
##SPARRING ULTRA MELEES OF HISTORY

### A Pygame Project

#### CONCEPT
It is our aim to produce a 2d fighting game in the style of Street Fighter using the python framework Pygame. 
Two human-controled players will each control a 2 diminsional fighter on the screen with the goal to knock out the opposing player. 
A start menu will transition to a screen where players select from a choice of at least two different characters with the goal of a full roster of 6. 
Each will have variations in speed, durability, and strength.
The two players will then compete to knock out their opponent best two out of three rounds. Health bars will be displayed.

#### THEME
We brainstormed our potential character roster of individuals from history, such as Hammurabi, Cyrus the great, Hattori Hanzo, Cleopatra, Queen Victoria, or Cathrin the Great. 
Some may be recolors of each other.
We intend to create our own sprite sets GIMP. These will be animated through pygame.
Alternatively, we have a sprite set of famous scientists such as Isaac Newton and Albert Einstein we may use instead depending on time. 
We would need to make additional animations to suppliment the existing sprites.

#### PYTHON/PYGAME
We will build our project in Python 3.6 . Both Pygame and Python include a libraries for unit testing (Pytest) . 
Depending on compatibility with Travis-CI, we may end up sticking exclusively to Pytest. 
It is our goal to bring in arcade style-controllers or to use the IUS ACM/CSG arcade cabinet for our presentation.
With this in mind, the project will either run on the existing PC in the arcade cabinet or on a Raspberry Pi. The project should build on any environment with Python installed.


#### CONTROLS
Controls will be arcade-style with 4-direction input and 6 buttons. 
Up to jump, down to crouch, and backwards to block. The three top buttons will be high punch, medium punch, low punch, and the three bottom buttons corrisponding kick actions. 
double tapping left or right will initiate a dash action and timing a forward directional input with an opponent's attack would allow a parry attack. 
Given the time, we intend to also implement a simple combo system.


 ^                   U
< >    XXX          L R    LP MP HP
 V     XXX	     D     LK MK HK






