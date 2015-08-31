# imports the time library needed to delay certain functions
import time
# imports the random library needed to generate a random number for
# the guessing game
from random import randint
# imports the os library needed to clear the terminal
import os
# imports the pygame library needed to play the sound in the
# poking function
from pygame import mixer

# variables needed for the guessing game
secret = randint(1, 10)

### a class for controlling the pet ###

class Pet(object):

    def __init__(self, name, photo, status, health, age, hunger, happiness, poke_count,
                 max_health, max_hunger, max_happiness):
        # The pet's stats
        self.name = name
        self.photo = photo
        self.status = status
        self.health = health
        self.age = age
        self.hunger = hunger
        self.happiness = happiness
        self.poke_count = poke_count
        self.max_health = max_health
        self.max_hunger = max_hunger
        self.max_happiness = max_happiness


    # a function which displays the pet's stats in a nice way.
    def display_stats(self):
        os.system('clear')
        print(self.name)
        print(self.photo)
        print("Status: " + self.status)
        print("Age: " + str(self.age))
        print("Health: " + self.health * "♥")
        print("Hunger: " + self.hunger * "*")
        print("Happines: " + self.happiness * "☺")


    # A function which checks if the pet is still alive
    def is_alive(self):
        return self.health > 0


    # A function which changes the status of the pet depending of the age value.
    # Each status has it's own characteristics.

    def set_youngling_stats(self):
        self.max_health = 10
        self.max_happiness = 8
        self.max_hunger = 7


    def set_adult_stats(self):
        self.max_health = 10
        self.max_happiness = 8
        self.max_hunger = 7


    def set_elderly_stats(self):
        self.max_health = 7
        self.max_happiness = 5
        self.max_hunger = 10


    def reset_stats(self):
        self.health = self.max_health
        self.happiness = self.max_happiness
        self.hunger = self.max_hunger


    def aging(self):
        if self.age == 5:
            self.status = "adult"
            self.set_adult_stats()
            print("Congratulation your pet has become an adult. It needs less food now")
            print("and it's health has improved however it's grumpier than a youngling.")
        elif self.age == 15:
            self.status = "elderly"
            self.set_elderly_stats()
            print("Congratulation your pet has become an elderly it needs now less food.")
            print("However it's health is worse and it's grumpier than an adult.")


    ### Functions to increase and decrease stats ###

    def increase_hunger(self):
        if self.hunger < self.max_hunger:
            self.hunger += 1


    def increase_poke_count(self):
        self.poke_count += 1


    def increase_happiness(self):
        if self.happiness < self.max_happiness:
            self.happiness += 1


    def increase_health(self):
        if self.health < self.max_health:
            self.health += 1


    def decrease_hunger(self):
        if self.hunger > 0:
            self.hunger -= 1


    def decrease_happiness(self):
        if self.happiness > 0:
            self.happiness -= 1


    def decrease_health(self):
        if self.health > 0:
            self.health -= 1


    def decrease_poke_count(self):
        self.poke_count -= 1


    # The function to decrease the stats and make the pet "live" needs to
    # run in the background.
    def decrease_stats(self):
        while True:
            time.sleep(15)
            self.decrease_hunger()
            if self.hunger <= 0:
                decrease_health()
                decrease_happiness()


  ### Activities ###

    # A function which simulates stroking it doesn't have any
    # effect on the pet.
    def stroking(self):
        os.system('clear')
        print()
        print("You're stroking the back of your pet gently.")
        print("It makes comforting noises and leans against your hand.")
        time.sleep(1)


    # Increases the pets hungriness by +1 unless the hunger is bigger than
    # the pet's maximum hunger. In this case the pet will vomit and looses hunger
    # and health.
    def feeding(self):
        os.system('clear')
        print("Hungriness of " + self.name + ": " + self.hunger * "*")
        feeding_confirmed = input("Do you want to feed your pet?")
        if feeding_confirmed in ("Y", "y"):
            self.increase_hunger()


    # A simple guessing game which increases the pet's happiness
    def playing(self):
        guess = 0
        os.system('clear')
        while guess != secret:
            g = input("Guess the Number")
            guess = int(g)
            if guess == secret:
                print("You win!")
            else:
                if guess > secret:
                    print("Your guess is too high")
                else:
                    print("Too low")
        self.increase_happiness()
        print("Game over!")


    # let's you poke the pet and it will talk
    # if you poke it more than 3 times it will get angry at you
    def poking(self):
        os.system('clear')
        if self.poke_count < 3:
            print("You poke " + self.name + " and it starts to speak.")
            self.increase_poke_count()
            mixer.init()
            mixer.music.load('happy.mp3')
            mixer.music.play()
            time.sleep(5)
        else:
            print("You annoyed " + self.name + "." + " It got angry at you.")
            self.decrease_happiness()
            mixer.init()
            mixer.music.load('angry.mp3')
            mixer.music.play()
            time.sleep(3)


    # A function which let's the pet sleep and regenerates it's stats
    def sleeping(self):
        os.system('clear')
        print("Your pet is sleeping now.")
        time.sleep(10)
        if self.max_hunger / self.hunger > 0.5:
            self.reset_stats()
            print("Your pet woke up feeling rested and in a good mood.")
        else:
            print("Your pet has woken up.")
        time.sleep(3)