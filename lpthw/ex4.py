#p.46 ex4 variables and names

cars = 100
# float assignment for space in a car 
	# could be int; does not affect final output unless space_in_a_car units can be less than whole numbers/units
	# float to int and int to float conversions --> can result in errors depending on level of precision required for input and output
	
space_in_a_car = 4.0
drivers = 30
passengers = 90
# calc for cars_not_driven ---> 100-30 = 70
cars_not_driven = cars - drivers

# variable assignment for cars_driven --> 30
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")


#NameError of 'car_pool_capacity' is not defined 
	# variable is defined as carpool_capacity, not car_pool_capacity


