#!/usr/bin/env python3
# import the threading module
import threading
# import the pets_variables
import pet_variables
# a module which includes various custom functions
import pet_functions


# Beginning of the main routine which makes up the actual game.

# thread which runs in the background to cause hunger, etc
t = threading.Thread(target=pet_functions.decrease_stats)
t.start()
# Only starts if the pet is still alive.
while pet_functions.is_alive():
    if not pet_variables.beginning_finished:
        # Let the player choose his pet and skip the beginning from then on.
        pet_functions.beginning()
        pet_variables.beginning_finished = True
        print()
        print()
        print("Your pet is currently a youngling which means it's needs a lot of attention.")
        print("Take good care of it or it will die very soon.")
    # checks if the pet has reached a new life stage and updates it accordingly
    pet_functions.aging()
    print()
    # Each round print the pets stats so that the player can see them.
    pet_functions.pet_stats()
    print()
    # Present the player with activities to choose from
    print("What would you like to do?")
    # Start the chosen activity and go back to the activity selector.
    print("1: Feeding, 2: Playing, 3: Stroke Pet,")
    print("4: Poking, 5: Sleeping, 6: Show Stats")
    try:
        chosen_activity = int(input("Choose the desired activity:"))
        if chosen_activity == 1:
            pet_functions.feeding()
        elif chosen_activity == 2:
            pet_functions.playing()
        elif chosen_activity == 3:
            pet_functions.stroking()
        elif chosen_activity == 4:
            pet_functions.poking()
        elif chosen_activity == 5:
            pet_functions.sleeping()
        elif chosen_activity == 6:
            pet_functions.pet_stats()
    except ValueError:
        pet_functions.pet_stats()
print("Your pet died.")
