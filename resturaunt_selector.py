import random
import numpy as np


file = open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'a+')

unique_restaurant = []

choice_list = []

final_selection = []

def open_file():
    open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'a+')

def add_restaurant():


    while True:

        result2 = input('Would you like to add a restaurant? (enter yes or no): ')
        if result2.lower() == 'yes':
            add_name = input('What is the name on the restaurant you would like to add?: ')

            n = '\n\nName: '

            with open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'a+'):
                file.write(n + add_name.title())

        elif result2.lower() == 'no':
            break
        else:
            print('Please enter yes or no.')


def add_to_list():
    data = open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'r')

    uniques = []

    for line in data:
        if 'Name: ' in line:
            uniques.append((str(line.strip()[6:])))

    for item in set(uniques):
        unique_restaurant.append(item)

def show_restaurants():
    num = 0
    for item in unique_restaurant:
        num += 1
        choice = (str(num) + '. ' + item)
        choice_list.append(choice)

def close_file():
    file.close()


def select_choices():

    while True:

        add = True

        while add:

            for item in choice_list:
                print(item)

            selected = (input('Please enter the number for Which restaurant you would like to choose between: '))
            for item in choice_list:
                if str(selected) in str(item[0]):

                    final_selection.append(item)
                    choice_list.remove(item)
                    add = False
                    break
            else:
                print('Oops please try again')

        result = input('Would you like to add another restaurant?: ')

        if result.lower() == 'yes':
            continue
        else:
            break


def rand_number():
    rand_num = random.randint(0, 100)
    return rand_num

def select_winner():


    # creates a range from 1 - 100

    item_range = np.arange(100)

    # establish a number for the range to be divided evenly by

    for count, item in enumerate(final_selection):
        step = 0
        step += count + 1
        item = 0

    # split the range by the given number

    split_list = np.array_split(item_range, step)

    # create a variable that is a random number

    number = rand_number()

    # create a dictionary to hold the range items and associate them with items from the test list

    combined_dict = dict(zip(final_selection, split_list))

    # if the random number is in the value for the dictionary return the key

    for key, value in combined_dict.items():
        for array_num in value:
            if number == array_num:
                print(f'{key[3:]} is the winner!')





print('Welcome to the restaurant selector!')

while True:

    open_file()

    add_restaurant()

    file.readlines()

    add_to_list()

    show_restaurants()

    select_choices()

    select_winner()

    result2 = input('Would you like to try again? (enter yes or no): ')
    if result2.lower() == 'yes':
        continue
    elif result2.lower() == 'no':
        print('Thank you for using the restaurant selector!')
        break
    else:
        print('Please enter yes or no.')






