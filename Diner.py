# Diner.py
# Goal: This class represents one of the diners at the restaurant and keeps tracks of their status and meal.

class Diner(object):
    STATUS = ["seated", "ordering", "order_placed", "order_served", "eating", "playing", "leaving"]

    def __init__(self, name):
        self.__name = name
        self.__order = []
        self.__status = self.STATUS[0]

    def __str__(self):
        return 'Diner {p.name} is currently {p.status}\n'.format(p=self)

    __repr__ = __str__

    def updateStatus(self):
        for value, key in enumerate(self.STATUS):
            if self.STATUS[6] == self.__status:
                print("Update failed, the Diner is leaving")
                break
            elif self.STATUS[value] == self.__status:
                self.__status = self.STATUS[value + 1]
                break

    def printOrder(self):
        print("Above all, You order the ", self.__order)

    def calculateMealCost(self):
        return sum([item[1] for item in self.__order])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
