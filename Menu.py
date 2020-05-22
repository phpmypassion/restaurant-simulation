# Menu.py
# Goal: This class represents the restaurant’s menu which contains four different categories of menu items diners can order from.

import csv

from MenuItem import MenuItem

class Menu(object):
    MENU_ITEM_TYPES = ["Veg", "Non-veg", "Drinks", "Snacks"]

    def __init__(self, filename):
        self.__menuItemDictionary = {}
        for t in self.MENU_ITEM_TYPES:
            self.__menuItemDictionary[t] = []
        with open(filename) as f:
            reader = list(csv.reader(f))
            for row in reader:
                menuItem = MenuItem(row[0], row[1], row[2], row[3], row[4])
                self.__menuItemDictionary[menuItem.type].append(menuItem)

    def getMenuItem(self, type, index):
        for key in self.__menuItemDictionary:
            if key == type:
                myMenuItem = self.__menuItemDictionary[key][index]
        return myMenuItem

    def printMenuItemsByType(self, type):
        print(type, ':')
        for i, v in enumerate(self.__menuItemDictionary[type]):
            print("#", i + 1, v)

    def getNumMenuItemsByType(self, type):
        return len(self.__menuItemDictionary[type])
