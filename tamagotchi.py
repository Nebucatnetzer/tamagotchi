#import the threading module
import threading
#import custom modules
#A function to nicely print out the pets stats
import pet_functions

#Variable needed to skip the beginning when finished
beginning_finished = False

#Beginning of the main routine which makes up the actual game.
#Only starts if the pet is still alive.
while pet_functions.is_alive():         
    t = threading.Thread(target=pet_functions.decrease_stats)
    t.start()
    if not beginning_finished:
        #Let the player choose his pet and skip the beginning from then on.
        pet_functions.beginning()
        beginning_finished = True
        print()
        print()
        print("Your pet is currently a youngling which means it's needs a lot of attention.")
        print("Take good care of it or it will die very soon.")
    #Each round print the pets stats so that the player can see them.
    pet_functions.aging()
    print()
    pet_functions.pet_stats()
    print()
    #Present the player with activities to choose from
    print("What would you like to do?")
    print("1: Feading, 2: Playing, 3: Show Stats")
    #Start the chosen activity and go back to the activity selector.
    chosen_activity = int(input("Choose the desired activity:"))
    if chosen_activity == 1:
        pet_functions.feading()
    elif chosen_activity == 2:
        pet_functions.playing()
    elif chosen_activity == 3:
        pet_functions.pet_stats()
print("Your pet died.")    
