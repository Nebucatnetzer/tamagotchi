import pet_variables
import time
from random import randint

# Pictures and symboles used ingame
cat = "(=^o.o^=)__"
mouse = "<:3 )~~~~"
fish = "<`)))><"
owl = "(^0M0^)"
# variables needed for the guessing game
secret = randint(1, 10)


def pet_stats():
    print(pet_variables.pet_name)
    print(pet_variables.pet_photo)
    print("Status: " + pet_variables.pet_status)
    print("Age: " + str(pet_variables.pet_age))
    print("Health: " + pet_variables.pet_health * "♥")
    print("Hunger: " + pet_variables.pet_hunger * "*")
    print("Happines: " + pet_variables.pet_happiness * "☺")


# A function which checks if the pet is still alive
def is_alive():
    if pet_variables.pet_health > 0:
        return True
    else:
        return False


# A function which let's the player choose his pet.
def beginning():
    print("Which pet do you want to look after?")
    print("1: Cat, 2: Mouse, 3: Fish, 4: Owl")
    chosen_pet = int(input("Choose your pet:"))
    if chosen_pet == 1:
        pet_variables.pet_photo = cat
    elif chosen_pet == 2:
        pet_variables.pet_photo = mouse
    elif chosen_pet == 3:
        pet_variables.pet_photo = fish
    elif chosen_pet == 4:
        pet_variables.pet_photo = owl


# A cunction which changes the status of the pet depending of the age value.
# Each status has it's own characteristics.
def aging():
    pet_variables.pet_status
    pet_variables.max_health
    pet_variables.max_happiness
    pet_variables.max_hunger
    if pet_variables.pet_age == 5:
        pet_variables.pet_status = "adult"
        pet_variables.max_health = 10
        pet_variables.max_happiness = 8
        pet_variables.max_hunger = 7
        print("Congratulation your pet has become an adult. It needs less food now")
        print("and it's health has improved however it's grumpier than a youngling.")
    elif pet_variables.pet_age == 15:
        pet_variables.pet_status = "elderly"
        pet_variables.max_health = 7
        pet_variables.max_happiness = 5
        pet_variables.max_hunger = 10
        print("Congratulation your pet has become an elderly it needs now less food.")
        print("However it's health is worse and it's grumpier than an adult.")


def decrease_hunger():
    pet_variables.pet_hunger = pet_variables.pet_hunger - 1


def decrease_happiness():
    pet_variables.pet_happiness = pet_variables.pet_happiness - 1


def decrease_health():
    pet_variables.pet_health = pet_variables.pet_health - 1


def decrease_stats():
    while True:
        time.sleep(15)
        decrease_hunger()
        if pet_variables.pet_hunger <= 0:
            decrease_health()
            decrease_happiness()


# Increases the pets hungriness by +1 unless the hunger is bigger than
# the pet's maximum hunger. In this case the pet womits and looses hunger
# and health.
def feading():
    pet_variables.pet_hunger
    print("Hungriness of " + pet_variables.pet_name + ": " + pet_variables.pet_hunger * "*")
    feading_confirmed = input("Do you want to feed your pet?")
    if feading_confirmed in ("Y", "y"):
        pet_variables.pet_hunger = pet_variables.pet_hunger + 1


# A simple guessing game which increases the pet's happiness
def playing():
    pet_variables.pet_happiness
    guess = 0
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
    pet_variables.pet_happiness = pet_variables.pet_happiness + 1
    print("Game over!")
