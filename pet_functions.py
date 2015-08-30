# imports the global variables
import pet_variables
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


### Functions providing the basic function of the programme ###

# a function which displays the pet's stats in a nice way.
def pet_stats():
    os.system('clear')
    print(pet_variables.pet_name)
    print(pet_variables.pet_photo)
    print("Status: " + pet_variables.pet_status)
    print("Age: " + str(pet_variables.pet_age))
    print("Health: " + pet_variables.pet_health * "♥")
    print("Hunger: " + pet_variables.pet_hunger * "*")
    print("Happines: " + pet_variables.pet_happiness * "☺")


# A function which checks if the pet is still alive
def is_alive():
    return pet_variables.pet_health > 0


# A function which let's the player choose his pet.
def beginning():
    print("Which pet do you want to look after?")
    print("1: Cat, 2: Mouse, 3: Fish, 4: Owl")
    chosen_pet = int(input("Choose your pet:"))
    if chosen_pet == 1:
        pet_variables.pet_photo = pet_variables.cat
    elif chosen_pet == 2:
        pet_variables.pet_photo = pet_variables.mouse
    elif chosen_pet == 3:
        pet_variables.pet_photo = pet_variables.fish
    elif chosen_pet == 4:
        pet_variables.pet_photo = pet_variables.owl
    pet_variables.pet_name = input("How do you want to call your pet?")


# A function which changes the status of the pet depending of the age value.
# Each status has it's own characteristics.

def set_youngling_stats():
    pet_variables.max_health = 10
    pet_variables.max_happiness = 8
    pet_variables.max_hunger = 7


def set_adult_stats():
    pet_variables.max_health = 10
    pet_variables.max_happiness = 8
    pet_variables.max_hunger = 7


def set_elderly_stats():
    pet_variables.max_health = 7
    pet_variables.max_happiness = 5
    pet_variables.max_hunger = 10


def reset_stats():
    pet_variables.pet_health = pet_variables.max_health
    pet_variables.pet_happiness = pet_variables.max_happiness
    pet_variables.pet_hunger = pet_variables.max_hunger


def aging():
    if pet_variables.pet_age == 5:
        pet_variables.pet_status = "adult"
        set_adult_stats()
        print("Congratulation your pet has become an adult. It needs less food now")
        print("and it's health has improved however it's grumpier than a youngling.")
    elif pet_variables.pet_age == 15:
        pet_variables.pet_status = "elderly"
        set_elderly_stats()
        print("Congratulation your pet has become an elderly it needs now less food.")
        print("However it's health is worse and it's grumpier than an adult.")


### Functions to increase and decrease stats ###

def increase_hunger():
    if pet_variables.pet_hunger < pet_variables.max_hunger:
        pet_variables.pet_hunger += 1


def increase_poke_count():
    pet_variables.poke_count += 1


def increase_happiness():
    if pet_variables.pet_happiness < pet_variables.max_happiness:
        pet_variables.pet_happiness += 1


def increase_health():
    if pet_variables.pet_health < pet_variables.max_health:
        pet_variables.pet_health += 1


def decrease_hunger():
    if pet_variables.pet_hunger > 0:
        pet_variables.pet_hunger -= 1


def decrease_happiness():
    if pet_variables.pet_happiness > 0:
        pet_variables.pet_happiness -= 1


def decrease_health():
    if pet_variables.pet_health > 0:
        pet_variables.pet_health -= 1


def decrease_poke_count():
    pet_variables.poke_count -= 1


# The function to decrease the stats and make the pet "live" needs to
# run in the background.
def decrease_stats():
    while True:
        time.sleep(pet_variables.day)
        decrease_hunger()
        if pet_variables.pet_hunger <= 0:
            decrease_health()
            decrease_happiness()


### Activities ###

# A function which simulates stroking it doesn't have any
# effect on the pet.
def stroking():
    os.system('clear')
    print()
    print("You're stroking the back of your pet gently.")
    print("It makes comforting noises and leans against your hand.")
    time.sleep(1)


# Increases the pets hungriness by +1 unless the hunger is bigger than
# the pet's maximum hunger. In this case the pet will vomit and looses hunger
# and health.
def feeding():
    os.system('clear')
    print("Hungriness of " + pet_variables.pet_name + ": " + pet_variables.pet_hunger * "*")
    feeding_confirmed = input("Do you want to feed your pet?")
    if feeding_confirmed in ("Y", "y"):
        increase_hunger()


# A simple guessing game which increases the pet's happiness
def playing():
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
    increase_happiness()
    print("Game over!")


# let's you poke the pet and it will talk
# if you poke it more than 3 times it will get angry at you
def poking():
    os.system('clear')
    if pet_variables.poke_count < 3:
        print("You poke " + pet_variables.pet_name + " and it starts to speak.")
        increase_poke_count()
        mixer.init()
        mixer.music.load('happy.mp3')
        mixer.music.play()
        time.sleep(5)
    else:
        print("You annoyed " + pet_variables.pet_name + "." + " It got angry at you.")
        decrease_happiness()
        mixer.init()
        mixer.music.load('angry.mp3')
        mixer.music.play()
        time.sleep(3)


# A function which let's the pet sleep and regenerates it's stats
def sleeping():
    os.system('clear')
    print("Your pet is sleeping now.")
    time.sleep(10)
    if pet_variables.max_hunger / pet_variables.pet_hunger > 0.5:
        reset_stats()
        print("Your pet woke up feeling rested and in a good mood.")
    else:
        print("Your pet has woken up.")
    time.sleep(3)
