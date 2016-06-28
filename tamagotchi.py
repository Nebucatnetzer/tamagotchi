# import the threading module
import threading
# a module which includes various custom functions
from pet_functions import Pet

# global variable need to lock the beginning
beginning_finished = False
day = 15

# Pictures and symbols used ingame
cat = "(=^o.o^=)__"
mouse = "<:3 )~~~~"
fish = "<`)))><"
owl = "(^0M0^)"

# initializing the tamagotchi
tamagotchi = Pet(name="empty", photo="empty", status="youngling", age=0, health=5, hunger=5, happiness=5,
                 max_happiness=10, max_health=5, max_hunger=5, poke_count=0)


# A function which let's the player choose his pet.
def beginning():
    global beginning_finished
    print("Which pet do you want to look after?")
    print("1: Cat, 2: Mouse, 3: Fish, 4: Owl")
    chosen_pet = int(input("Choose your pet:"))
    if chosen_pet == 1:
        pet_photo = cat
    elif chosen_pet == 2:
        pet_photo = mouse
    elif chosen_pet == 3:
        pet_photo = fish
    elif chosen_pet == 4:
        pet_photo = owl
    pet_name = input("How do you want to call your pet?")
    tamagotchi.name = pet_name
    tamagotchi.photo = pet_photo
    print()
    print()
    print("Your pet is currently a youngling which means it's needs a lot of attention.")
    print("Take good care of it or it will die very soon.")
    beginning_finished = True

# Present the player with activities to choose from
def menu():
    print("What would you like to do?")
    # Start the chosen activity and go back to the activity selector.
    print("1: Feeding, 2: Playing, 3: Stroke Pet,")
    print("4: Poking, 5: Sleeping, 6: Show Stats")
    try:
        chosen_activity = int(input("Choose the desired activity:"))
        if chosen_activity == 1:
            tamagotchi.feeding()
        elif chosen_activity == 2:
            tamagotchi.playing()
        elif chosen_activity == 3:
            tamagotchi.stroking()
        elif chosen_activity == 4:
            tamagotchi.poking()
        elif chosen_activity == 5:
            tamagotchi.sleeping()
        elif chosen_activity == 6:
            tamagotchi.display_stats()
    except ValueError:
        tamagotchi.display_stats()

# Beginning of the main routine which makes up the actual game.

# Only starts if the pet is still alive.
def main():
    while tamagotchi.is_alive():
        if not beginning_finished:
            # Let the player choose his pet and skip the beginning from then on.
            beginning()
            tamagotchi.decrease_stats()
        # checks if the pet has reached a new life stage and updates it accordingly
        tamagotchi.aging()
        print()
        # Each round print the pets stats so that the player can see them.
        tamagotchi.display_stats()
        print()
        menu()
    print("Your pet died.")


if __name__ == "__main__": main()
