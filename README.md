# tamagotchi

## Todo
* make the aging work parallel the main programme
* adding a function to decrease the health

## Possible things to add
Some interesting things I could add to the
tamagotchi programme which shouldn't be too hard:

* ~~create a loop~~
* ~~give it happiness~~
* ~~give it points for hungriness~~
* ~~add the guessing game and increase the happiness by one point when you finished the game~~
* ~~create a list with things you can do~~
* pet it to increase happiness
* poke it to make it speak, pokes let it loose a happiness point
* ~~add max values depending on the status~~
* sleeping with all values with over 50% full heals the pet if it has lost health
* add pooping and cleaning function
* let it get sick if it's health is low, by random chance or if there's too much poop
* ~~let it age~~
* decrease the hunger value after x seconds
* add sleep function, you have to switch the lights off otherwise it will have nightmare and loose one health point.
* add the possibility to get sick. Maybe compare two random numbers. 
* add a function to restart the game or exit it after the pet died. 
* add a function let the user exit the game
* safe the stats in a text file

##30.6.2015

Time function has to be implemented otherwise the decrease.* functions won't work. 
It seems to work however the import time part has to go into the pet_functions.py file.
Maybe I should move all the imports to that file otherwise it's not clear why they are needed.

Moved all the imports to there relevant place 
And added the time import. Things are working now like intended.
However the pet doesn't get updated automatically. I currently don't know how to achieve that.
I'll have to ask reddit how to do it.

##6.7.2015

I've written a function to decrease the stats in the background. Means the tamagotchi can now get hungry etc.
However it currently doesn't work. I don't know why atm. If you call it independently it works just fine.

In addition I've cleaned up the code a bit and made sure that the stats variables don't fall under 0 because that might cause some problems in the future.
