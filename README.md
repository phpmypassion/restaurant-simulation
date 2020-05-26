# Restaurant Simulation
 
### RestaurantHelper.py
-	Goal: This class includes helper methods to allow diners to randomly show up to the restaurant.

### Run.py
-	Goal: This class starts the simulation.

## Part 1 – Creating the Restaurant’s Menu 

### menu.csv
-	Goal: This CSV file has all restaurant’s menu items. It has four coloumn described as below.
	*col1: Items Name
	*col2: Types of Item (Veg/Non-veg/Drinks/Snacks)
	*col3: Time Takes for Cooking.
	*col4: No. of Chefs Available Per Item

### MenuItem.py
-	Goal: This class will represent a single item that a diner can order from the restaurant’s menu

### Menu.py
-	Goal: This class represents the restaurant’s menu which contains four different categories of menu items diners can order from.

## Part 2 – Creating Diners

### Diner.py
- Goal: This class represents one of the diners at the restaurant and keeps tracks of their status and meal.

## Part 3 – Creating a Waiter

### Waiter.py
- Goal: This class will represent the restaurant's waiter. The waiter maintains a list of the dines it is currently taking care of, and progresses them through the different stages of the restaurant. The waiter in the simulation will repeat multiple cycles of attending to the diners. In each cycle, the waiter will seat a new diner, if one arrives, take any diners' orders if needed, and give diners their bill, according to each diner's status.

### Run Restaurant Simulation As Below
- Python Run.py
