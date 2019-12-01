'''Restaurant Selector App'''

import random
import numpy as np
import tkinter as tk
import ctypes
import collections

in_file_list = []

final_selection = []

winner_list = []

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main_window = tk.Frame(self)
        main_window.pack(side='top', fill='both', expand=True)
        main_window.grid_rowconfigure(0, weight = 1)
        main_window.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (LandingPage, CheckRestaurants, AddRestaurants, ChooseRestaurants):          
            
            frame = F(main_window, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(LandingPage)
    
    def show_frame(self, requested_frame):

        frame = self.frames[requested_frame]

        frame.tkraise()

class LandingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        background_image = tk.PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')      
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
      
        top_frame = tk.Frame(self, bg='#dc9955', bd=5)
        top_frame.place(relx = 0.5, rely = 0.05, relwidth=0.75, relheight=0.10, anchor='n')

        header_label = tk.Label(top_frame, text = "Welcome to the restaurant selector.\nLet's ride this gravy train to Flavortown!", bg='#e5d6b9', font='Arial')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        bottom_frame = tk.Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.4, relwidth=0.75, relheight=0.2, anchor='n')

        header_label = tk.Label(bottom_frame, text = '\nWhat would you like to do?', bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        check = tk.Button(bottom_frame, text = 'Check Restaurants', fg='white', bg='#4e3632', command= lambda:controller.show_frame(CheckRestaurants))
        check.place(relx=0.125, rely=0.4125, relheight = 0.25, width = 110)

        add = tk.Button(bottom_frame, text = 'Add Restaurant', fg='white', bg='#4e3632', command= lambda:controller.show_frame(AddRestaurants))
        add.place(relx=0.425, rely=0.4125, relheight = 0.25, width = 110)

        choose = tk.Button(bottom_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', command= lambda:controller.show_frame(ChooseRestaurants))
        choose.place(relx=0.725, rely=0.4125, relheight = 0.25, width = 110)

class CheckRestaurants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        background_image = tk.PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png') 
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        bottom_frame = tk.Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.1125, relwidth=0.4, relheight=0.75, anchor='n')

        def update_restaurant_list(self):

            restaurants_in_data_file = []

            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:  

                for line in data:

                    if 'Name: ' in line:

                        restaurants_in_data_file.append(str(line.strip()[6:]))
            
            list_formatting = '\nRestaurants currently in the list:\n\n' + '\n'.join(map(''.join, sorted(set(restaurants_in_data_file))))

            return list_formatting

        update_list = update_restaurant_list(self)

        header_label = tk.Label(bottom_frame, text = update_list, bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        refresh = tk.Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_list(self))
        refresh.place(relx = 0.05, rely = 0.875, relheight = 0.06, width = 100)

        remove = tk.Button(bottom_frame, text = 'Remove All Items', fg='white', bg='#4e3632', command= lambda: remove_items(self))
        remove.place(relx = 0.365, rely = 0.875, relheight = 0.06, width = 100)

        back = tk.Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))
        back.place(relx = 0.68, rely = 0.875, relheight = 0.06, width = 100)

        def remove_items(self):

            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'w+') as data:

                for line in data:

                    del line 

                removed = ctypes.windll.user32.MessageBoxW

                removed(None, 'All restaurants have been removed from the list.\n\nMake sure to refresh the restaurant list to see changes.', 'Restaurants Removed', 0)  

        def refresh_list(self):

            bottom_frame.after(0, bottom_frame.destroy)

            new_frame = tk.Frame(self, bg='#dc9955', bd=10)
            new_frame.place(relx = 0.5, rely = 0.1125, relwidth=0.4, relheight=0.75, anchor='n')

            update_list2 = update_restaurant_list(self)
        
            header_label = tk.Label(new_frame, text = update_list2, bg='#e5d6b9', font='Arial', anchor='n')
            header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

            refresh = tk.Button(new_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_list(self))
            refresh.place(relx = 0.05, rely = 0.875, relheight = 0.06, width = 100)

            remove = tk.Button(new_frame, text = 'Remove All Items', fg='white', bg='#4e3632', command= lambda: remove_items(self))
            remove.place(relx = 0.365, rely = 0.875, relheight = 0.06, width = 100)

            back = tk.Button(new_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))
            back.place(relx = 0.68, rely = 0.875, relheight = 0.06, width = 100)

class AddRestaurants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        background_image = tk.PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)

        bottom_frame = tk.Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.35, relwidth=0.5, relheight=0.3, anchor='n')

        header_label = tk.Label(bottom_frame, text = '\nEnter the name of the restaurant you would like to add to the list.', bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        def retrieve_input(self):

            user_input = entry_field.get("1.0","end-1c")

            if user_input == '':

                no_input = ctypes.windll.user32.MessageBoxW
                no_input(None, 'Please enter the name of the restaurant you would like to add to the list.', 'Error', 0)

            else:

                with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'a+') as data:

                    n = 'Name: '

                    data.write(n + user_input.title() + '\n')

                    added = ctypes.windll.user32.MessageBoxW
                    added(None, f'{user_input.title()} has been added to the list.\n\nMake sure to refresh the restaurant list to see changes.', 'Restaurant Added', 0)

        def delete_text(self):

            entry_field.delete(1.0, tk.END)

        entry_field = tk.Text(bottom_frame, font= 'Arial', width = 25, height = 1, bd = 5)
        entry_field.bind('<KeyPress-Return>', retrieve_input)
        entry_field.bind('<KeyRelease-Return>', delete_text)
        entry_field.place(relx = 0.2625, rely = 0.33125)

        add_to_list = tk.Button(bottom_frame, text = 'Add', fg='white', bg='#4e3632', command = lambda: [retrieve_input(self), delete_text(self)])
        add_to_list.place(relx = 0.2, rely = 0.62, relheight = 0.15, width = 100)

        back = tk.Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command = lambda: [controller.show_frame(LandingPage), delete_text(self)])
        back.place(relx = 0.6, rely = 0.62, relheight = 0.15, width = 100)

class ChooseRestaurants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        background_image = tk.PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')   
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        top_frame = tk.Frame(self, bg='#dc9955', bd=5)
        top_frame.place(relx = 0.5, rely = 0.05, relwidth=0.75, relheight=0.10, anchor='n')

        header_label = tk.Label(top_frame, text = "Choose a restaurant to go to.", bg='#e5d6b9', font='Arial') 
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        bottom_frame = tk.Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.24, relwidth=0.75, relheight=0.66, anchor='n')

        header_label = tk.Label(bottom_frame, bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        in_list = tk.Listbox(bottom_frame, selectmode = 'multiple', activestyle = 'none', width = 25, bg = '#bfb97f', height = 15,
        selectbackground = '#e5c558', highlightcolor = '#000000', font = 'Arial 12 bold')
        in_list.place(relx = 0.3425, rely = 0.1125)        

        refresh_btn = tk.Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_listbox(self))
        refresh_btn.place(relx = 0.225, rely = 0.8125, width = 110, relheight = 0.075)

        choose_rest = tk.Button(bottom_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', 
        command = lambda: [check_if_selected(self), less_than_two(self), reset(self)])
        choose_rest.place(relx = 0.425, rely = 0.8125, width = 110, relheight = 0.075)
            
        back = tk.Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda: [reset(self), controller.show_frame(LandingPage), ])
        back.place(relx = 0.625, rely = 0.8125, width = 110, relheight = 0.075)

        def create_listbox(self):

            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:

                for line in data:

                    if 'Name: ' in line:

                        in_file_list.append(str(line.strip()[6:]))

            num = 0
   
            for item in sorted(set(in_file_list)):

                num += 1

                formula = int((28 - (len(item)*2) / 2))

                item_space = [' ' * formula]
   
                item_space.append(item)

                in_list.insert(num, ''.join(item_space))

                if num > 15:

                    more_than_15_label = tk.Label(bottom_frame, text = 'Note: List is scrollable if there are more than 15 restaurants.', bg='#e5d6b9', font='Arial', anchor='n')
                    more_than_15_label.place(relx = 0.2135, rely = 0.73)

        create_listbox(self)

        def check_if_selected(self):

            all_items = in_list.get(0, tk.END)

            sel_idx = in_list.curselection()

            sel_list = [all_items[item] for item in sel_idx]

            for item in sel_list:

                final_selection.append(item.strip())

        def reset(self):

            global winner_list

            global final_selection

            final_selection = []

            winner_list = []
            
            in_list.selection_clear(0, tk.END)

        def rand_number(self):

            rand_num = random.randint(0, 1000)

            return rand_num

        def select_winner(self):

            global final_selection

            global winner_list

            item_range = np.arange(1000)

            random.shuffle(final_selection)

            for count, item in enumerate(final_selection):
                
                step = 0

                step += count + 1

            split_list = np.array_split(item_range, step)

            number = rand_number(self)

            combined_dict = dict(zip(final_selection, split_list))

            working = True

            while working:

                for key, value in combined_dict.items():

                    for array_num in value:

                        if number == array_num:

                            winner_list.append(key)

                            number = rand_number(self)

                count = collections.Counter(winner_list)

                results_list = []

                def results(self):

                    for item in count:

                        results_list.append((f'{item}: {count[item]}'))     

                for item in count:

                    if count[item] > 3:

                        reset(self)

                        break

                    elif count[item] == 3:

                        results(self)
                        
                        MessageBox = ctypes.windll.user32.MessageBoxW

                        MessageBox(None, f'{item} is the winner!\n\nResults for all restaurants:\n\n' + '\n'.join(map(''.join, sorted(results_list))), 'Winner!', 0)

                        count.clear()

                        return working == False                    

        def less_than_two(self):

            count = 0

            for item in in_list.curselection():

                count += 1

            if count < 2:

                MessageBox = ctypes.windll.user32.MessageBoxW
                MessageBox(None, 'Please select at least two restaurants to choose between.', 'Error', 0)
            
            else:

                select_winner(self)

        def refresh_listbox(self):

            global in_file_list

            global final_selection

            global winner_list

            in_file_list = []

            final_selection = []

            winner_list = []

            in_list.after(0, in_list.destroy)
            back.after(0, back.destroy)
            choose_rest.after(0, choose_rest.destroy)
            refresh_btn.after(0, refresh_btn.destroy)
            bottom_frame.after(0, bottom_frame.destroy)

            new_frame = tk.Frame(self, bg='#dc9955', bd=10)
            new_frame.place(relx = 0.5, rely = 0.24, relwidth=0.75, relheight=0.66, anchor='n')

            header_label = tk.Label(new_frame, bg='#e5d6b9', font='Arial', anchor='n')
            header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

            new_in_list = tk.Listbox(new_frame, selectmode = 'multiple', activestyle = 'none', width = 25, height =15, bg = '#bfb97f',
            selectbackground = '#e5c558', highlightcolor = '#000000', font = 'Arial 12 bold')
            new_in_list.place(relx = 0.3425, rely = 0.1125)
            
            def new_check_if_selected(self):

                all_items = new_in_list.get(0, tk.END)

                sel_idx = new_in_list.curselection()

                sel_list = [all_items[item] for item in sel_idx]

                for item in sel_list:

                    final_selection.append(item.strip())

            def new_reset(self):

                global winner_list

                global final_selection

                final_selection = []

                winner_list = []

                new_in_list.selection_clear(0, tk.END)

            def new_less_than_two(self):

                count = 0

                for item in new_in_list.curselection():

                    count += 1

                if count < 2:

                    MessageBox = ctypes.windll.user32.MessageBoxW
                    MessageBox(None, 'Please select at least two restaurants to choose between.', 'Error', 0)

                else:

                    select_winner(self)

            def new_create_listbox(self):

                with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:

                    for line in data:

                        if 'Name: ' in line:

                            in_file_list.append(str(line.strip()[6:]))

                num = 0
                    
                for item in sorted(set(in_file_list)):

                    num += 1

                    formula = int((28 - (len(item)*2) / 2))

                    item_space = [' ' * formula]
 
                    item_space.append(item)

                    new_in_list.insert(num, ''.join(item_space))

                    if num > 15:

                        more_than_15_label = tk.Label(bottom_frame, text = 'Note: List is scrollable if there are more than 15 restaurants.', bg='#e5d6b9', font='Arial', anchor='n')
                        more_than_15_label.place(relx = 0.2135, rely = 0.73)

            new_create_listbox(self)

            new_refresh_btn = tk.Button(new_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: [refresh_listbox(self)])
            new_refresh_btn.place(relx = 0.225, rely = 0.8125, width = 110, relheight = 0.075)

            new_choose_rest = tk.Button(new_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', 
            command = lambda: [new_check_if_selected(self), new_less_than_two(self), new_reset(self)])
            new_choose_rest.place(relx = 0.425, rely = 0.8125, width = 110, relheight = 0.075)

            new_back = tk.Button(new_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda: [controller.show_frame(LandingPage)])
            new_back.place(relx = 0.625, rely = 0.8125, width = 110, relheight = 0.075)

window = Window()

window.title('Restaurant Selector')

window.iconbitmap('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\borger.ico')

window.geometry('1000x800')

window.maxsize(1000, 800)

window.mainloop()
