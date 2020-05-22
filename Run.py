"""
Run this file in order to start the restaurant simulation program using below command

python Run.php
"""
import datetime
import time

from Menu import Menu
from Waiter import Waiter
from RestaurantHelper import RestaurantHelper

def main():
    RESTAURANT_NAME = "Anil_Restaurant"
    restaurantTime = datetime.datetime(2017, 5, 1, 5, 0)

    # Create the menu object
    menu = Menu("menu.csv")
    # create the waiter object using the created Menu we just created
    waiter = Waiter(menu)
    print("Welcome to " + RESTAURANT_NAME + "!")
    print(RESTAURANT_NAME + " is now open for dinner.\n")
    #
    for i in range(21):
        print("\n~~~ It is currently", restaurantTime.strftime("%H:%M PM"), "~~~")
        restaurantTime += datetime.timedelta(minutes=10)

        potentialDiner = RestaurantHelper.randomDinerGenerator()
        if potentialDiner is not None:
            print("\n" + potentialDiner.name + " welcome, please be seated!")  # we have a diner to add to the waiter's list of diners

            waiter.addDiner(potentialDiner)

        waiter.advanceDiners(restaurantTime.strftime("%H:%M PM"))
        time.sleep(2)

    print("\n~~~ ", RESTAURANT_NAME, "is now closed. ~~~")
    # After the restaurant is closed, progress any diners until everyone has left
    while waiter.getNumDiners():
        print("\n~~~ It is currently", restaurantTime.strftime("%H:%M PM"), "~~~")
        restaurantTime += datetime.timedelta(minutes=10)
        waiter.advanceDiners()
        time.sleep(2)

    print("Goodbye!")

main()
