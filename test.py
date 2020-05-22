from Menu import Menu
from Diner import Diner
from Waiter import Waiter
from RestaurantHelper import RestaurantHelper

def main():
    RESTAURANT_NAME = "Anil_Restaurant"  # TODO 1: add your own restaurant name in the quotes

    menu = Menu("menu.csv")
    waiter = Waiter(menu)  # TODO 4: uncomment this one the Waiter class is implemented

    diner = Diner("1")
    waiter.addDiner(diner)
    waiter.advanceDiners()

    diner = Diner("2")
    waiter.addDiner(diner)
    waiter.advanceDiners()

    diner = Diner("3")
    waiter.addDiner(diner)
    waiter.advanceDiners()

    diner = Diner("4")
    waiter.addDiner(diner)
    waiter.advanceDiners()

    diner = Diner("5")
    waiter.addDiner(diner)
    waiter.advanceDiners()


    diner = Diner("6")
    waiter.addDiner(diner)
    waiter.advanceDiners()

    diner = Diner("7")
    waiter.addDiner(diner)
    waiter.advanceDiners()

    diner = Diner("8")
    waiter.addDiner(diner)
    waiter.advanceDiners()


main()
