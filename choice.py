import random

names = input("Enter the names...! ( seperated by commas.) ")
names_list = names.split(",")

length = len(names_list)
random_choice = random.randint(0,length-1)
names_list[random_choice]
print(f"{names_list[random_choice]} will pay the bill.")