import random
import numpy as np
from tkinter import *
import ctypes

in_file_list = []

final_selection = []


class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        #set up frame

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (LandingPage, CheckRestaurants, AddRestaurants, ChooseRestaurants):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(LandingPage)
    
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class LandingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        canvas = Canvas(self, height=200, width=1000)
        canvas.pack()

        background_image = PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        background_label = Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        top_frame = Frame(self, bg='#dc9955', bd=5)
        top_frame.place(relx = 0.5, rely = 0.05, relwidth=0.75, relheight=0.10, anchor='n')


        header_label = Label(top_frame, text = "Welcome to the restaurant selector.\nLet's ride this gravy train to Flavortown!", bg='#e5d6b9', font='Arial')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)


        bottom_frame = Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.4, relwidth=0.75, relheight=0.2, anchor='n')


        header_label = Label(bottom_frame, text = '\nWhat would you like to do?', bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)


        check = Button(bottom_frame, text = 'Check Restaurants', fg='white', bg='#4e3632', command= lambda:controller.show_frame(CheckRestaurants))
        check.place(relx=0.125, rely=0.4125, relheight = 0.25, width = 110)

        add = Button(bottom_frame, text = 'Add Restaurants', fg='white', bg='#4e3632', command= lambda:controller.show_frame(AddRestaurants))
        add.place(relx=0.425, rely=0.4125, relheight = 0.25, width = 110)

        choose = Button(bottom_frame, text = 'Choose Restaurants', fg='white', bg='#4e3632', command= lambda:controller.show_frame(ChooseRestaurants))
        choose.place(relx=0.725, rely=0.4125, relheight = 0.25, width = 110)


class CheckRestaurants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        canvas = Canvas(self, height=800, width=1000)
        canvas.pack()

        background_image = PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        background_label = Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        bottom_frame = Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.1125, relwidth=0.4, relheight=0.75, anchor='n')

        restaurants_in_data_file = []

        with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:
            for line in data:
                if 'Name: ' in line:
                    restaurants_in_data_file.append(str(line.strip()[6:]))
        
        test = '\nRestaurants currently in the list:\n\n' + '\n'.join(map(''.join, sorted(set(restaurants_in_data_file))))

        header_label = Label(bottom_frame, text = test, bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        refresh = Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_list(self))
        refresh.place(relx = 0.05, rely = 0.875, relheight = 0.06, width = 100)

        remove = Button(bottom_frame, text = 'Remove All Items', fg='white', bg='#4e3632', command= lambda: remove_items(self))
        remove.place(relx = 0.365, rely = 0.875, relheight = 0.06, width = 100)

        back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))
        back.place(relx = 0.68, rely = 0.875, relheight = 0.06, width = 100)
        
        

        def remove_items(self):
            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'w+') as data:
                for line in data:
                    del line
            

        def refresh_list(self):
            bottom_frame.after(0, bottom_frame.destroy)

            new_frame = Frame(self, bg='#dc9955', bd=10)
            new_frame.place(relx = 0.5, rely = 0.1125, relwidth=0.4, relheight=0.75, anchor='n')
        
            restaurants_in_data_file = []

            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:
                for line in data:
                    if 'Name: ' in line:
                        restaurants_in_data_file.append(str(line.strip()[6:]))
            
            test = '\nRestaurants currently in the list:\n\n' + '\n'.join(map(''.join, sorted(set(restaurants_in_data_file))))

            header_label = Label(new_frame, text = test, bg='#e5d6b9', font='Arial', anchor='n')
            header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

            refresh = Button(new_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_list(self))
            refresh.place(relx = 0.05, rely = 0.875, relheight = 0.06, width = 100)

            remove = Button(new_frame, text = 'Remove All Items', fg='white', bg='#4e3632', command= lambda: remove_items(self))
            remove.place(relx = 0.365, rely = 0.875, relheight = 0.06, width = 100)

            back = Button(new_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))
            back.place(relx = 0.68, rely = 0.875, relheight = 0.06, width = 100)


class AddRestaurants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        canvas = Canvas(self, height=800, width=1000)
        canvas.pack()

        background_image = PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        background_label = Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        bottom_frame = Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.35, relwidth=0.5, relheight=0.3, anchor='n')

        header_label = Label(bottom_frame, text = '\nEnter the restaurant you would like to add to the list.', bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)


        def retrieve_input(self):
            user_input = entry_field.get("1.0","end-1c")

            if user_input == '':
                no_input = ctypes.windll.user32.MessageBoxW
                no_input(None, 'Please enter the name of a restaurant you would like to add', 'Error', 0)

            else:
                with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'a+') as file:
                    n = '\n\nName: '
                    file.write(n + user_input.title())

        def delete_text(self):
            entry_field.delete(1.0, END)
       
        entry_field = Text(bottom_frame, font= 'Arial', width = 25, height = 1, bd = 5)
        entry_field.bind('<KeyPress-Return>', retrieve_input)
        entry_field.bind('<KeyRelease-Return>', delete_text)
        entry_field.place(relx = 0.2625, rely = 0.33125)

        add_to_list = Button(bottom_frame, text = 'Add', fg='white', bg='#4e3632', command = lambda: [retrieve_input(self), delete_text(self)])
        add_to_list.place(relx = 0.2, rely = 0.62, relheight = 0.15, width = 100)

        back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command = lambda:controller.show_frame(LandingPage))
        back.place(relx = 0.6, rely = 0.62, relheight = 0.15, width = 100)


class ChooseRestaurants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        canvas = Canvas(self, height=800, width=1000)
        canvas.pack()

        background_image = PhotoImage(file='C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\flavortown.png')
        background_label = Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        top_frame = Frame(self, bg='#dc9955', bd=5)
        top_frame.place(relx = 0.5, rely = 0.05, relwidth=0.75, relheight=0.10, anchor='n')

        header_label = Label(top_frame, text = "Choose a Restaurant to go to.", bg='#e5d6b9', font='Arial')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        bottom_frame = Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.24, relwidth=0.75, relheight=0.66, anchor='n')

        header_label = Label(bottom_frame, bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        in_list = Listbox(bottom_frame, selectmode = MULTIPLE, activestyle = 'none', width = 25, bg = '#bfb97f', height = 15,
        selectbackground = '#e5c558', highlightcolor = '#000000', font = 'Arial 12 bold')
        in_list.place(relx = 0.3425, rely = 0.1125)

        #listbox_scrollbar = Scrollbar(in_list, orient = 'vertical')
        #listbox_scrollbar.pack()
        #listbox_scrollbar.config(command = in_list.yview)
        #in_list.config(yscrollcommand=listbox_scrollbar.set)

        

        with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as file:
            for line in file:
                if 'Name: ' in line:
                    in_file_list.append(str(line.strip()[6:]))
        
        num = 0
            
        for item in sorted(set(in_file_list)):
            num += 1
            item_space = '                      ' + item            
            in_list.insert(num, item_space)

        def check_if_selected(self):
            all_items = in_list.get(0, END)
            sel_idx = in_list.curselection()
            sel_list = [all_items[item] for item in sel_idx]
            for rest in sel_list:
                final_selection.append(rest.strip())

        def reset(self):
            in_list.selection_clear(0, END)

        def rand_number(self):
            rand_num = random.randint(0, 100)
            return rand_num

        def select_winner(self):

            global final_selection
            global in_file_list


            print('ifl')
            for item in final_selection:
                print(item)
            print('--------------')

            print('fs')

            for item in final_selection:
                print(item)
            print('--------------')

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

            number = rand_number(self)

            # create a dictionary to hold the range items and associate them with items from the test list

            combined_dict = dict(zip(final_selection, split_list))

            # if the random number is in the value for the dictionary return the key        

            for key, value in combined_dict.items():
                for array_num in value:
                    if number == array_num:
                        MessageBox = ctypes.windll.user32.MessageBoxW
                        MessageBox(None, f'{key} is the winner!', 'Winner!', 0)

            final_selection = []

            in_file_list = []





                        
        def clear_final_selection(self):
            in_list.selection_clear(0, END)

        refresh_btn = Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: [refresh_listbox(self), reset(self)])
        refresh_btn.place(relx = 0.225, rely = 0.8125, width = 110, relheight = 0.075)

        choose_rest = Button(bottom_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', 
        command = lambda: [check_if_selected(self), select_winner(self), reset(self)])
        choose_rest.place(relx = 0.425, rely = 0.8125, width = 110, relheight = 0.075)
                        
        back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda: [controller.show_frame(LandingPage), reset(self)])
        back.place(relx = 0.625, rely = 0.8125, width = 110, relheight = 0.075)     
        

        def refresh_listbox(self):
            in_list.after(0, in_list.destroy)
            back.after(0, back.destroy)
            choose_rest.after(0, choose_rest.destroy)
            refresh_btn.after(0, refresh_btn.destroy)

            for resta in in_file_list:
                del resta

            print(in_file_list)
            print('---------')

            for restau in final_selection:
                del restau
            
            print(final_selection)
            print('---------')

            new_in_list = Listbox(bottom_frame, selectmode = MULTIPLE, activestyle = 'none', width = 25, height =15, bg = '#bfb97f',
            selectbackground = '#e5c558', highlightcolor = '#000000', font = 'Arial 12 bold')
            new_in_list.place(relx = 0.3425, rely = 0.1125)

            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as file:
                for line in file:
                    if 'Name: ' in line:
                        in_file_list.append(str(line.strip()[6:]))

            num = 0
            
            for item in sorted(set(in_file_list)):
                num += 1
                item_space = '                      ' + item            
                new_in_list.insert(num, item_space)
            
            def new_check_if_selected(self):
                all_items = new_in_list.get(0, END)
                sel_idx = new_in_list.curselection()
                sel_list = [all_items[item] for item in sel_idx]
                for rest in sel_list:
                    final_selection.append(rest.strip())

            def new_clear_final_selection(self):                
                new_in_list.selection_clear(0, END)

                for item in final_selection:
                    print(item)  

            new_refresh_btn = Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: [refresh_listbox(self)])
            new_refresh_btn.place(relx = 0.225, rely = 0.8125, width = 110, relheight = 0.075)

            new_choose_rest = Button(bottom_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', 
            command = lambda: [new_check_if_selected(self), select_winner(self), new_clear_final_selection(self)])
            new_choose_rest.place(relx = 0.425, rely = 0.8125, width = 110, relheight = 0.075)

            new_back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda: [controller.show_frame(LandingPage)])
            new_back.place(relx = 0.625, rely = 0.8125, width = 110, relheight = 0.075)


window = Window()
window.title('Restaurant Selector')
window.iconbitmap('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\borger.ico')
window.maxsize(1000, 800)

window.mainloop()
