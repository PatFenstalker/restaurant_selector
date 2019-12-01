'''Restaurant Selector App'''

import random
import numpy as np
import tkinter as tk
import ctypes
import collections

# global list that pulls each line in the restaurant_database.txt file that starts with 'Name: '.  
# Made global so it can be cleared consistently in later functions 

in_file_list = []

# global list that pulls each item selected by the user in the choose restaurant page's listbox
# made global so it can be cleared consistetly in later funtions 

final_selection = []

# global list that pulls in the key for a value in which a randomly generated number fell into
# made global so it can be cleared consistetly in later funtions 

winner_list = []

# class creates the main window and defines what frames (pages) are for the gui

class Window(tk.Tk):

    # constructs the Window class

    def __init__(self, *args, **kwargs):

        # creates the tk.(tkinter)Tk(instance of tkinter) as a parent class inside of the child class window

        tk.Tk.__init__(self, *args, **kwargs)
        
        #set up the main window and make it fill all available space

        main_window = tk.Frame(self)

        # place the main_window frame and have it fill all availabel space

        main_window.pack(side='top', fill='both', expand=True)

        # uses grid geometry to configure a single row that expands to fill all space

        main_window.grid_rowconfigure(0, weight = 1)

        # uses grid geometry to configure a single row that expands to fill all space

        main_window.grid_columnconfigure(0, weight = 1)

        # create a dictionary to call the name of the frame (key) with the value being all additional code within the key

        self.frames = {}

        # for each frame in the given frame objects

        for F in (LandingPage, CheckRestaurants, AddRestaurants, ChooseRestaurants):
            
            # defines a varaible frame that turns each item in the list of frames into a Frame assigned to the main window
            
            frame = F(main_window, self)

            # assigns each Frame as an attribute to the window class 

            self.frames[F] = frame

            # places each frame in the window and makes it fill all available space in the window

            frame.grid(row=0, column=0, sticky='nsew')

        # start off by showing the landing page    

        self.show_frame(LandingPage)

    # when requesting to move to a specific frame, raise the frame (bring to the main window)
    
    def show_frame(self, requested_frame):

        # changes the frame attribute to a specific frame (requested_frame)

        frame = self.frames[requested_frame]

        # bring the request frame into view for the window (bring it to the front of the window)

        frame.tkraise()

# creates the landing frame.

class LandingPage(tk.Frame):

    # constructs the Landing Page class that inherits from the window class

    def __init__(self, parent, controller):

        # constructs a frame for and inherits from the Landng Page class

        tk.Frame.__init__(self, parent)

        # defines a background image variable from a specific location

        background_image = tk.PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        
        # creates a label with an image attribute that references the created background_image variable
        
        background_label = tk.Label(self, image=background_image)

        # associates the background_image with the label

        background_label.image = background_image

        # places the label in the landing page frame

        background_label.place(relheight = 1, relwidth = 1)

        # creates a new frame (top_frame) to be placed over the background image
        
        top_frame = tk.Frame(self, bg='#dc9955', bd=5)

        # places the frame within the Landing Page frame

        top_frame.place(relx = 0.5, rely = 0.05, relwidth=0.75, relheight=0.10, anchor='n')

        # creates a label with a number of atributes

        header_label = tk.Label(top_frame, text = "Welcome to the restaurant selector.\nLet's ride this gravy train to Flavortown!", bg='#e5d6b9', font='Arial')

        # places the label inside the top_frame frame

        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        # creates a new frame (bottom_frame) to be placed over the background image

        bottom_frame = tk.Frame(self, bg='#dc9955', bd=10)

        # places the frame within the Landing Page frame

        bottom_frame.place(relx = 0.5, rely = 0.4, relwidth=0.75, relheight=0.2, anchor='n')

        # creates a label with a number of atributes

        header_label = tk.Label(bottom_frame, text = '\nWhat would you like to do?', bg='#e5d6b9', font='Arial', anchor='n')

        # places the label inside the bottom_frame frame

        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        # creates a button with a number of atributes, when the button is clicked it executes a lambda function

        check = tk.Button(bottom_frame, text = 'Check Restaurants', fg='white', bg='#4e3632', command= lambda:controller.show_frame(CheckRestaurants))

        # places the button within the bottom_frame frame.

        check.place(relx=0.125, rely=0.4125, relheight = 0.25, width = 110)

        # creates a button with a number of atributes, when the button is clicked it executes a lambda function

        add = tk.Button(bottom_frame, text = 'Add Restaurant', fg='white', bg='#4e3632', command= lambda:controller.show_frame(AddRestaurants))

        # places the button within the bottom_frame frame.

        add.place(relx=0.425, rely=0.4125, relheight = 0.25, width = 110)

        # creates a button with a number of atributes, when the button is clicked it executes a lambda function

        choose = tk.Button(bottom_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', command= lambda:controller.show_frame(ChooseRestaurants))

        # places the button within the bottom_frame frame.

        choose.place(relx=0.725, rely=0.4125, relheight = 0.25, width = 110)

# creates the check restaurants frame.

class CheckRestaurants(tk.Frame):

    # constructs the Check Restaurants class 

    def __init__(self, parent, controller):

        # # constructs a frame for and inherits from the Check Restaurants class

        tk.Frame.__init__(self, parent)

        # defines a background image variable from a specific location

        background_image = tk.PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        
        # creates a label with an image attribute that references the created background_image variable
        
        background_label = tk.Label(self, image=background_image)

        # associates the background_image with the label

        background_label.image = background_image

        # places the label in the Check Restaurants frame

        background_label.place(relheight = 1, relwidth = 1)

        # creates a new frame (bottom_frame) to be placed over the background image
        
        bottom_frame = tk.Frame(self, bg='#dc9955', bd=10)

        # places the frame inside the Check Restaurants frame

        bottom_frame.place(relx = 0.5, rely = 0.1125, relwidth=0.4, relheight=0.75, anchor='n')

        # creates a function that pulls information from a 

        def update_restaurant_list(self):

            # creates an empty list

            restaurants_in_data_file = []

            # when requested, opens a file from a given location with read permissions as the variable name data

            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:
                
                # for each line in the file (variable name: data)

                for line in data:

                    # if the string 'Name: ' is in the line (to not pull in blank lines)

                    if 'Name: ' in line:

                        # add the the line as a string to the restaurants_in_data_file list with all white space and page breaks removed, from character 5 and beyond
                        # (removes the 'Name ' from the beggining of the string)

                        restaurants_in_data_file.append(str(line.strip()[6:]))

            # denies a variable that hold how the data will be displayed. 
            # (pulls in unique itesm from the restaurants_in_data_file list, sorted alphabetically, each on its own new line with nothing done in between each letter)
            
            list_formatting = '\nRestaurants currently in the list:\n\n' + '\n'.join(map(''.join, sorted(set(restaurants_in_data_file))))

            # returns the list_formatting variable to be used for updating a label

            return list_formatting

        # creates an instance of the update_restaurant_list function

        update_list = update_restaurant_list(self)

        # creates a label with a number of atributes

        header_label = tk.Label(bottom_frame, text = update_list, bg='#e5d6b9', font='Arial', anchor='n')

        # places the label inside the bottom_frame frame

        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        # creates a button that executes a lambda function when pressed

        refresh = tk.Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_list(self))

        # places the button inside the bottom_frame frame

        refresh.place(relx = 0.05, rely = 0.875, relheight = 0.06, width = 100)

        # creates a button that executes a lambda function when pressed

        remove = tk.Button(bottom_frame, text = 'Remove All Items', fg='white', bg='#4e3632', command= lambda: remove_items(self))

        # places the button inside the bottom_frame frame

        remove.place(relx = 0.365, rely = 0.875, relheight = 0.06, width = 100)

        # creates a button that executes a lambda function when pressed

        back = tk.Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))

        # places the button inside the bottom_frame frame

        back.place(relx = 0.68, rely = 0.875, relheight = 0.06, width = 100)

        # creates a function to delete all lines in the referenced file

        def remove_items(self):

            # when requested, opens a file from a given location with writing permissions as the variable name data

            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'w+') as data:

                # for each line in the file (variable name: data)

                for line in data:

                    # delete the line

                    del line
            
                # creates a popup window

                removed = ctypes.windll.user32.MessageBoxW

                # popup window text and header

                removed(None, 'All restaurants have been removed from the list.\n\nMake sure to refresh the restaurant list to see changes.', 'Restaurants Removed', 0)  

        # cteates a function to destroy and recreate a frame

        def refresh_list(self):

            # when activated, after 0 seconds destroy (delete) bottom_frame

            bottom_frame.after(0, bottom_frame.destroy)

            # creates a new frame

            new_frame = tk.Frame(self, bg='#dc9955', bd=10)

            # places the new frame in the same poisition as the destroyed bottom_frame

            new_frame.place(relx = 0.5, rely = 0.1125, relwidth=0.4, relheight=0.75, anchor='n')

            # creates an instance of the update_restaurant_list function to re-update a label

            update_list2 = update_restaurant_list(self)

            # creates a new label with a number of attributes
        
            header_label = tk.Label(new_frame, text = update_list2, bg='#e5d6b9', font='Arial', anchor='n')

            # places the label inside the new_frame frame

            header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

            # creates a button that executes a lambda function when pressed

            refresh = tk.Button(new_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_list(self))

            # places the button inside the new_frame frame

            refresh.place(relx = 0.05, rely = 0.875, relheight = 0.06, width = 100)

            # creates a button that executes a lambda function when pressed

            remove = tk.Button(new_frame, text = 'Remove All Items', fg='white', bg='#4e3632', command= lambda: remove_items(self))

            # places the button inside the new_frame frame

            remove.place(relx = 0.365, rely = 0.875, relheight = 0.06, width = 100)

            # creates a button that executes a lambda function when pressed

            back = tk.Button(new_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))

            # places the button inside the new_frame frame

            back.place(relx = 0.68, rely = 0.875, relheight = 0.06, width = 100)

# creates the add restaurants frame.

class AddRestaurants(tk.Frame):

    # constructs the Add Restaurant class

    def __init__(self, parent, controller):

        # constructs a frame for and inherits from the Add Restaurant class

        tk.Frame.__init__(self, parent)

        # defines a background image variable from a specific location

        background_image = tk.PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        
        # creates a label with an image attribute that references the created background_image variable
        
        background_label = tk.Label(self, image=background_image)

        # associates the background_image with the label

        background_label.image = background_image

        # places the label in the landing page frame

        background_label.place(relheight = 1, relwidth = 1)

        # creates a new frame (bottom_frame) to be placed over the background image
        
        bottom_frame = tk.Frame(self, bg='#dc9955', bd=10)

        # places the frame within the Add Restaurants frame

        bottom_frame.place(relx = 0.5, rely = 0.35, relwidth=0.5, relheight=0.3, anchor='n')

        # creates a label with a number of attributes

        header_label = tk.Label(bottom_frame, text = '\nEnter the name of the restaurant you would like to add to the list.', bg='#e5d6b9', font='Arial', anchor='n')

        # places the label inside the bottom_frame

        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        # creates a function to retreive user input from a tkinter text field

        def retrieve_input(self):

            # defines a variable that captures the input of a named text entry field from the first character to the last character

            user_input = entry_field.get("1.0","end-1c")

            # if the user input variable does not contain any characters

            if user_input == '':

                # create a popup window

                no_input = ctypes.windll.user32.MessageBoxW

                # popup window text and header

                no_input(None, 'Please enter the name of the restaurant you would like to add to the list.', 'Error', 0)

            # if the user_input variable has characters in it

            else:

                # when requested, opens a file from a given location with reading and appending permissions as the variable name data

                with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'a+') as data:

                    # defines a variable as a string

                    n = 'Name: '

                    # adds a formatted string to the file (named data)

                    data.write(n + user_input.title() + '\n')

                    # creates a popup window

                    added = ctypes.windll.user32.MessageBoxW

                    # popup window header and text

                    added(None, f'{user_input.title()} has been added to the list.\n\nMake sure to refresh the restaurant list to see changes.', 'Restaurant Added', 0)

        #creates a function that deletes all characters from the text entry field

        def delete_text(self):

            # deletes all characters from the text entry field from the first character to the last

            entry_field.delete(1.0, tk.END)

        # creates a text entry field with a number or attributes

        entry_field = tk.Text(bottom_frame, font= 'Arial', width = 25, height = 1, bd = 5)

        # binds the return (enter) key to a function when pressed

        entry_field.bind('<KeyPress-Return>', retrieve_input)

        # binds the return (enter) key to a function when released

        entry_field.bind('<KeyRelease-Return>', delete_text)

        # places the text entry field inside the bottom_frame frame

        entry_field.place(relx = 0.2625, rely = 0.33125)

        # creates a button that executes a lambda function when pressed

        add_to_list = tk.Button(bottom_frame, text = 'Add', fg='white', bg='#4e3632', command = lambda: [retrieve_input(self), delete_text(self)])

        # places the button in the bottom_frame frame

        add_to_list.place(relx = 0.2, rely = 0.62, relheight = 0.15, width = 100)

        # creates a button that executes a lambda function when pressed

        back = tk.Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command = lambda: [controller.show_frame(LandingPage), delete_text(self)])

        # places the button in the bottom_frame frame

        back.place(relx = 0.6, rely = 0.62, relheight = 0.15, width = 100)

# creates the choose restaurants frame.

class ChooseRestaurants(tk.Frame):

    # constructs the Choose Restaurant class

    def __init__(self, parent, controller):

        # constructs a frame for and inherits from the Choose Restaurant class

        tk.Frame.__init__(self, parent)

        # defines a background image variable from a specific location

        background_image = tk.PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        
        # creates a label with an image attribute that references the created background_image variable
        
        background_label = tk.Label(self, image=background_image)

        # associates the background_image with the label

        background_label.image = background_image

        # places the label in the landing page frame

        background_label.place(relheight = 1, relwidth = 1)

        # creates a new frame (top_frame) to be placed over the background image
        
        top_frame = tk.Frame(self, bg='#dc9955', bd=5)

        # places the frame within the Choose Restaurant frame

        top_frame.place(relx = 0.5, rely = 0.05, relwidth=0.75, relheight=0.10, anchor='n')

        # creates a label with a number of attributes

        header_label = tk.Label(top_frame, text = "Choose a restaurant to go to.", bg='#e5d6b9', font='Arial')

        # places the label inside the top_frame frame
    
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        # creates a new frame (bottom_frame) to be places over the background image

        bottom_frame = tk.Frame(self, bg='#dc9955', bd=10)

        # places the frame inside the Choose Restaurants frame

        bottom_frame.place(relx = 0.5, rely = 0.24, relwidth=0.75, relheight=0.66, anchor='n')

        # creates a label with a number of attributes

        header_label = tk.Label(bottom_frame, bg='#e5d6b9', font='Arial', anchor='n')

        # places the label inside the bottom_frame frame

        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        # creates a listbox with a number of attributes

        in_list = tk.Listbox(bottom_frame, selectmode = 'multiple', activestyle = 'none', width = 25, bg = '#bfb97f', height = 15,
        selectbackground = '#e5c558', highlightcolor = '#000000', font = 'Arial 12 bold')

        # places the listbox inside the bottom_frame

        in_list.place(relx = 0.3425, rely = 0.1125)        

        # creates a button that executes a lambda function when pressed

        refresh_btn = tk.Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_listbox(self))

        # places the button inside the bottom_frame frame

        refresh_btn.place(relx = 0.225, rely = 0.8125, width = 110, relheight = 0.075)

        # creates a button that executes a lambda function when pressed

        choose_rest = tk.Button(bottom_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', 
        command = lambda: [check_if_selected(self), less_than_two(self), reset(self)])

        # places the button inside the bottom_frame frame

        choose_rest.place(relx = 0.425, rely = 0.8125, width = 110, relheight = 0.075)

        # creates a button that executes a lambda function when pressed
                        
        back = tk.Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda: [reset(self), controller.show_frame(LandingPage), ])

        # places the button inside the bottom_frame frame

        back.place(relx = 0.625, rely = 0.8125, width = 110, relheight = 0.075)

        # creates a function that adds items to the listbox  

        def create_listbox(self):

            # when requested, opens a file from a given location with read permissions as the variable name data
        
            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:

                # for each line in the file (named data)

                for line in data:

                    # if the string 'Name: ' is in the line

                    if 'Name: ' in line:

                        # add the line as a string to the in_file_list list after the 6th character (after 'Name: ')

                        in_file_list.append(str(line.strip()[6:]))

            # defines a variable as the integer 0
            
            num = 0

            # for each unique item in aphabetically sorted in_file_list list 
                
            for item in sorted(set(in_file_list)):

                # add 1 to num variable

                num += 1

                # defines a variable as an integer (used to calculate spaces in the length of the listbox's viewable space per line)

                formula = int((28 - (len(item)*2) / 2))

                # creates a list of ' ' (spaces) based on the returned integer for each item

                item_space = [' ' * formula]

                # adds the item to the item_space list in the last position (after all the spaces)
                        
                item_space.append(item)

                # joins the item with the spaces and adds the new string to the listbox 
                # (end result being a list of items that have spaces based upon their character length that are centered inside the listbox)

                in_list.insert(num, ''.join(item_space))

                # if num is greater than 15 (more than 15 items in the listbox)

                if num > 15:

                    # create a label with a number of attributes 

                    more_than_15_label = tk.Label(bottom_frame, text = 'Note: List is scrollable if there are more than 15 restaurants.', bg='#e5d6b9', font='Arial', anchor='n')

                    # places the label inside the bottom_frame frame

                    more_than_15_label.place(relx = 0.2135, rely = 0.73)

        # calls the create_listbox function
            
        create_listbox(self)

        # creates a function to see if items in the listbox have been selected (are highlighted by the user)

        def check_if_selected(self):

            # variable to store all items that have been added to the listbox

            all_items = in_list.get(0, tk.END)

            # a variable to store all items currently selected (highlighted)

            sel_idx = in_list.curselection()

            # list comprehesion (pull each item in the all items list that is also in the selected index variable and create a new list from the items)

            sel_list = [all_items[item] for item in sel_idx]

            # for each item in the sel_index list

            for item in sel_list:

                # add the item to the final_selection list without spaces

                final_selection.append(item.strip())

        # function to reset a number of lists and the listbox

        def reset(self):

            # references the global list winner_list and makes it able to be worked with

            global winner_list

            # references the global list final_selection and makes it able to be worked with

            global final_selection

            # redefines the final_selection list as an empty list

            final_selection = []

            # redefines the winner_list list as an empty list

            winner_list = []

            # deselects (clears) items from the listbox
            
            in_list.selection_clear(0, tk.END)

        # creates a function to create a random number between 0 and 1000

        def rand_number(self):

            # creates a variable to store a random number between 0 and 1000

            rand_num = random.randint(0, 1000)

            # resturns the rand_num variable

            return rand_num

        # creates a function to determine the winning restaurant

        def select_winner(self):

            # declares the global variable finael_selection so the items can be removed once the function finishes using anotehr function

            global final_selection

            # declares the global variable winner_list so the items can be removed once the function finishes using anotehr function

            global winner_list

            # creates a range from 1 - 1000 in case there more than 100 restaurants

            item_range = np.arange(1000)

            # shuffles the list to make the selection a bit more random

            random.shuffle(final_selection)

            # for each enumeration number and item in the enumerated list named final_selection
            
            for count, item in enumerate(final_selection):

                # establishes a value for the number of items the array will be split between

                step = 0

                # creates the finished value by which the array will be split 
                # (determined by the number of items + 1 as the array cannot be divided by zero)

                step += count + 1

            # create the value of the split arays based on the cleated step variable

            split_list = np.array_split(item_range, step)

            # create an instance of the random number function

            number = rand_number(self)

            # create a dictionary to hold the split array and associate it with items from the final selection list

            combined_dict = dict(zip(final_selection, split_list))

            # declares a vraible to be used as the condition for an upcoming while loop

            working = True

            # starts the while loop

            while working:

                # for each key and value inside of combined_dict

                for key, value in combined_dict.items():

                    # for each array number in each value

                    for array_num in value:

                        # if instance of the random number function (number) is the same number as an array number

                        if number == array_num:

                            # add the key of the value from which the array number came from to the winner list

                            winner_list.append(key)

                            # change instance of the random number finction to a different instance (change the number) and keep looping

                            number = rand_number(self)

                # creates a counter for each item in winner list

                count = collections.Counter(winner_list)

                # creates a list where variables and values from count variable can be stored

                results_list = []

                # function to add a formatted string (item in the list: count of the item) to the results list

                def results(self):

                    # for each item in the count variable

                    for item in count:

                        # add the formated string (item in the list: count of the item) to the list

                        results_list.append((f'{item}: {count[item]}'))     

                # for each item in count

                for item in count:

                    # if the item has a count number that is greater than 3

                    if count[item] > 3:

                        # perform the reset funtion and start the loop again to eliminate the 
                        # loop from not stopping itteration when an item reaches a count of 3 

                        reset(self)

                        # breaks out of the for loop

                        break

                    # or if the count of the item is equal to 3

                    elif count[item] == 3:

                        # run the results function

                        results(self)

                        # create a message box
                        
                        MessageBox = ctypes.windll.user32.MessageBoxW

                        # inside the message box sahre the winner (whichever item got to the count of 3) and results for each item in the counter

                        MessageBox(None, f'{item} is the winner!\n\nResults for all restaurants:\n\n' + '\n'.join(map(''.join, sorted(results_list))), 'Winner!', 0)

                        # clear the counter variabel (count)

                        count.clear()

                        # stop the loop by changing the condition

                        return working == False                    

        # creates a function to find out if at least two items have been selected inside the listbox to choose between

        def less_than_two(self):

            # creates a variable to hold an integer 0

            count = 0

            # for each item that is currently selected inside the in_list list

            for item in in_list.curselection():

                # adds 1 to the count

                count += 1

            # if the count variable is less 2 (less than two items selected)

            if count < 2:

                # create a popup window

                MessageBox = ctypes.windll.user32.MessageBoxW

                # popup window header and text

                MessageBox(None, 'Please select at least two restaurants to choose between.', 'Error', 0)

            # if there are at least two items selected
            
            else:

                # execute the select_winner function

                select_winner(self)

        # creates a function to reset a number of elements involving the listbox

        def refresh_listbox(self):

            # references the global list in_file_list and makes it able to be worked with

            global in_file_list

            # references the global list final selection and makes it able to be worked with

            global final_selection

            # references the global list winner_list and makes it able to be worked with

            global winner_list

            # redefines the in_file_list list as an empty list

            in_file_list = []

            # redefines the final selection list as an empty list

            final_selection = []

            # redefines the winner_list list as an empty list

            winner_list = []

            # after 0 seconds destroy the in_list listbox

            in_list.after(0, in_list.destroy)

            # after 0 seconds destroy the back button

            back.after(0, back.destroy)

            # after 0 seconds destroy the choose_rest button

            choose_rest.after(0, choose_rest.destroy)

            # after 0 seconds destroy the refresh_btn button

            refresh_btn.after(0, refresh_btn.destroy)

            # after 0 seconds destroy the bottom_frame frame

            bottom_frame.after(0, bottom_frame.destroy)

            # creates a new frame (new_frame) to be places over the background image

            new_frame = tk.Frame(self, bg='#dc9955', bd=10)

            # places the new frame inside of the Choose Restaurants frame

            new_frame.place(relx = 0.5, rely = 0.24, relwidth=0.75, relheight=0.66, anchor='n')

            # creates a label with a number of attributes

            header_label = tk.Label(new_frame, bg='#e5d6b9', font='Arial', anchor='n')

            # places the label inside of the new_frame frame

            header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

            # creates a new listbox with a number of attributes

            new_in_list = tk.Listbox(new_frame, selectmode = 'multiple', activestyle = 'none', width = 25, height =15, bg = '#bfb97f',
            selectbackground = '#e5c558', highlightcolor = '#000000', font = 'Arial 12 bold')

            # palces the listbox inside of the new_frame frame

            new_in_list.place(relx = 0.3425, rely = 0.1125)
            
            # creates a new check_if_selected function that checks the new listbox to see if items are selected

            def new_check_if_selected(self):

                # variable to store all items that have been added to the new listbox

                all_items = new_in_list.get(0, tk.END)

                # a variable to store all items currently selected (highlighted)

                sel_idx = new_in_list.curselection()

                # list comprehesion (pull each item in the all items list that is also in the selected index variable and create a new list from the items)

                sel_list = [all_items[item] for item in sel_idx]

                # for each item in the sel_index list

                for item in sel_list:

                    # add the item to the final_selection list without spaces

                    final_selection.append(item.strip())

            # new reset function to clear some old items and the new listbox

            def new_reset(self):

                # references the global list winner_list and makes it able to be worked with                

                global winner_list

                # references the global list final selection and makes it able to be worked with

                global final_selection

                # redefines the final_selection list as an empty list

                final_selection = []

                # redefines the winnder_list list as an empty list

                winner_list = []

                # deselectes (clears) selected items in the new listbox

                new_in_list.selection_clear(0, tk.END)

            # creates a new less_than_two function that check if more than two items have been selected for comparison in the new listbox

            def new_less_than_two(self):

                # creates a variable to hold an integer 0

                count = 0

                # for each item that is currently selected inside the new_in_list list

                for item in new_in_list.curselection():

                    # adds 1 to the count

                    count += 1

                # if the count variable is less 2 (less than two items selected)

                if count < 2:

                    # create a popup window

                    MessageBox = ctypes.windll.user32.MessageBoxW

                    # popup window header and text

                    MessageBox(None, 'Please select at least two restaurants to choose between.', 'Error', 0)

                # if there are at least two items selected
                
                else:

                    # execute the select_winner function

                    select_winner(self)

            # creates a function that add items to the new listbox

            def new_create_listbox(self):

                 # when requested, opens a file from a given location with read permissions as the variable name data
        
                with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:

                    # for each line in the file (named data)

                    for line in data:

                        # if the string 'Name: ' is in the line

                        if 'Name: ' in line:

                            # add the line as a string to the in_file_list list after the 6th character (after 'Name: ')

                            in_file_list.append(str(line.strip()[6:]))

                # defines a variable as the integer 0
                
                num = 0

                # for each unique item in aphabetically sorted new_in_file_list list 
                    
                for item in sorted(set(in_file_list)):

                    # add 1 to num variable

                    num += 1

                    # defines a variable as an integer (used to calculate spaces in the length of the listbox's viewable space per line)

                    formula = int((28 - (len(item)*2) / 2))

                    # creates a list of ' ' (spaces) based on the returned integer for each item

                    item_space = [' ' * formula]

                    # adds the item to the item_space list in the last position (after all the spaces)
                            
                    item_space.append(item)

                    # joins the item with the spaces and adds the new string to the new listbox 
                    # (end result being a list of items that have spaces based upon their character length that are centered inside the listbox)

                    new_in_list.insert(num, ''.join(item_space))

                    # if num is greater than 15 (more than 15 items in the listbox)

                    if num > 15:

                        # create a label with a number of attributes 

                        more_than_15_label = tk.Label(bottom_frame, text = 'Note: List is scrollable if there are more than 15 restaurants.', bg='#e5d6b9', font='Arial', anchor='n')

                        # places the label inside the bottom_frame frame

                        more_than_15_label.place(relx = 0.2135, rely = 0.73)

            # creates an instance of the new_create_list function

            new_create_listbox(self)

            # creates a new refresh_btn that executes a lambda function when pressed

            new_refresh_btn = tk.Button(new_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: [refresh_listbox(self)])

            # places the button inside the new_frame frame

            new_refresh_btn.place(relx = 0.225, rely = 0.8125, width = 110, relheight = 0.075)

            # creates a new choose_rest that executes a lambda function when pressed

            new_choose_rest = tk.Button(new_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', 
            command = lambda: [new_check_if_selected(self), new_less_than_two(self), new_reset(self)])

            # places the button inside the new_frame frame

            new_choose_rest.place(relx = 0.425, rely = 0.8125, width = 110, relheight = 0.075)

            # creates a new back that executes a lambda function when pressed

            new_back = tk.Button(new_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda: [controller.show_frame(LandingPage)])

            # places the button inside the new_frame frame

            new_back.place(relx = 0.625, rely = 0.8125, width = 110, relheight = 0.075)

# defines the main window.

window = Window()

# creates a title for the main window

window.title('Restaurant Selector')

# sets the icon for the main window.

window.iconbitmap('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\borger.ico')

# sets the size for the main window

window.geometry('1000x800')

# limits the size of the main window to maintain the best clarity for the background image.

window.maxsize(1000, 800)

#calls the defined main window and starts the app.

window.mainloop()
