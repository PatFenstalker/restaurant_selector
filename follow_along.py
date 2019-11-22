import random
import numpy as np
from tkinter import *
import ctypes


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


        header_label = Label(bottom_frame, text = 'What would you like to do?', bg='#e5d6b9', font='Arial', anchor='n', pady=15)
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)


        check = Button(bottom_frame, text = 'Check Restaurants', fg='white', bg='#4e3632', command= lambda:controller.show_frame(CheckRestaurants))
        check.place(relx=0.10, rely=0.45)

        add = Button(bottom_frame, text = 'Add Restaurants', fg='white', bg='#4e3632', command= lambda:controller.show_frame(AddRestaurants))
        add.place(relx=0.43, rely=0.45)

        choose = Button(bottom_frame, text = 'Choose Restaurants', fg='white', bg='#4e3632', command= lambda:controller.show_frame(ChooseRestaurants))
        choose.place(relx=0.74, rely=0.45)


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
        bottom_frame.place(relx = 0.5, rely = 0.1, relwidth=0.4, relheight=0.75, anchor='n')

        restaurants_in_data_file = []

        with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:
            for line in data:
                if 'Name: ' in line:
                    restaurants_in_data_file.append(str(line.strip()[6:]))
        
        test = 'Restaurants currently in the list:\n\n' + '\n'.join(map(''.join, sorted(set(restaurants_in_data_file))))

        header_label = Label(bottom_frame, text = test, bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        refresh = Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_list(self))
        refresh.place(relx = 0.25, rely = 0.9)
        
        back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))
        back.place(relx = 0.65, rely = 0.9)

        def refresh_list(self):
            bottom_frame.after(0, bottom_frame.destroy)

            new_frame = Frame(self, bg='#dc9955', bd=10)
            new_frame.place(relx = 0.5, rely = 0.1, relwidth=0.4, relheight=0.75, anchor='n')
        
            restaurants_in_data_file = []

            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'r') as data:
                for line in data:
                    if 'Name: ' in line:
                        restaurants_in_data_file.append(str(line.strip()[6:]))
            
            test = 'Restaurants currently in the list:\n\n' + '\n'.join(map(''.join, sorted(set(restaurants_in_data_file))))

            header_label = Label(new_frame, text = test, bg='#e5d6b9', font='Arial', anchor='n')
            header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

            refresh = Button(new_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_list(self))
            refresh.place(relx = 0.25, rely = 0.9)
            
            back = Button(new_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))
            back.place(relx = 0.65, rely = 0.9)


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
        bottom_frame.place(relx = 0.5, rely = 0.25, relwidth=0.5, relheight=0.3, anchor='n')

        header_label = Label(bottom_frame, text = 'Enter the restaurant you would like to add to the list.', bg='#e5d6b9', font='Arial', anchor='n', pady=25)
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)


        def retrieve_input(self):
            user_input = entry_field.get("1.0","end-1c")
            
            with open('C:\\Users\\pat74648\\OneDrive - Spectrum Health\\Desktop\\Python\\final\\restaurant_database.txt', 'a+') as file:
                n = '\n\nName: '
                file.write(n + user_input.title())

        def delete_text(self):
            entry_field.delete(1.0, END)
       
        add_to_list = Button(bottom_frame, text = 'Add', fg='white', bg='#4e3632', command = lambda: [retrieve_input(self), delete_text(self)])
        
        add_to_list.place(relx = 0.615, rely = 0.35, relwidth = 0.25, relheight = 0.13)

        entry_field = Text(bottom_frame, font= 'Arial', width = 20, height = 1, bd = 5)

        entry_field.bind('<KeyPress-Return>', retrieve_input)
        entry_field.bind('<KeyRelease-Return>', delete_text)

        entry_field.place(relx = 0.13, rely = 0.35)

        

        back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command = lambda:controller.show_frame(LandingPage))
        back.place(relx = 0.5, rely = 0.75)


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
        bottom_frame.place(relx = 0.5, rely = 0.25, relwidth=0.75, relheight=0.66, anchor='n')

        header_label = Label(bottom_frame, bg='#e5d6b9', font='Arial', anchor='n', pady=15)
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        in_list = Listbox(bottom_frame, selectmode = MULTIPLE, activestyle = 'none', width = 25, bg = '#bfb97f',
        selectbackground = '#e5c558', highlightcolor = '#000000', font = 'Arial 12 bold')
        in_list.place(relx = 0.35, rely = 0.2)

        #listbox_scrollbar = Scrollbar(in_list, orient = 'vertical')
        #listbox_scrollbar.pack()
        #listbox_scrollbar.config(command = in_list.yview)
        #in_list.config(yscrollcommand=listbox_scrollbar.set)

        in_file_list = []

        final_selection = []

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
            for item in final_selection:
                final_selection.remove(item)
                in_list.selection_clear(0, END)

        def rand_number(self):
            rand_num = random.randint(0, 100)
            return rand_num

        def select_winner(self):


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



           
            #for key, value in combined_dict.items():
            #    for array_num in value:
##
 #                   win_counter = 0
#
 #                   while win_counter < 3:
#
 #                       if random.randint(0,100) == array_num:
  #                          win_counter += 1
   #                         print(random.randint(0,100))
#
 #                   if win_counter == 3:
  #                      MessageBox = ctypes.windll.user32.MessageBoxW
   #                     MessageBox(None, f'{key} is the winner!\nWin counter: {win_counter}', 'Winner!', 0)
                         
                        
        




        def clear_final_selection(self):
            for item in in_file_list:
                while item in in_file_list:
                    in_file_list.remove(item)

            for item in final_selection:
                while item in final_selection:
                    final_selection.remove(item)
            
            in_list.selection_clear(0, END)

            

                        
        back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda: [controller.show_frame(LandingPage), reset(self)])
        back.place(relx = 0.35, rely = 0.85, relwidth = 0.1)

        refresh_btn = Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: refresh_listbox(self))
        refresh_btn.place(relx = 0.75, rely = 0.85, relwidth = 0.1)

        choose_rest = Button(bottom_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', 
        command = lambda: [check_if_selected(self), select_winner(self), clear_final_selection(self)])
        choose_rest.place(relx = 0.5, rely = 0.85)

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

            new_in_list = Listbox(bottom_frame, selectmode = MULTIPLE, activestyle = 'none', width = 25, bg = '#bfb97f',
            selectbackground = '#e5c558', highlightcolor = '#000000', font = 'Arial 12 bold')
            new_in_list.place(relx = 0.35, rely = 0.2)

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
                for item in in_file_list:
                    while item in in_file_list:
                        in_file_list.remove(item)

                for item in final_selection:
                    while item in final_selection:
                        final_selection.remove(item)
                
                new_in_list.selection_clear(0, END)

                for item in final_selection:
                    print(item)  


            new_back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda: [controller.show_frame(LandingPage)])
            new_back.place(relx = 0.35, rely = 0.85, relwidth = 0.1)

            new_choose_rest = Button(bottom_frame, text = 'Choose Restaurant', fg='white', bg='#4e3632', 
            command = lambda: [new_check_if_selected(self), select_winner(self), new_clear_final_selection(self)])
            new_choose_rest.place(relx = 0.5, rely = 0.85)

            new_refresh_btn = Button(bottom_frame, text = 'Refresh', fg='white', bg='#4e3632', command= lambda: [refresh_listbox(self)])
            new_refresh_btn.place(relx = 0.75, rely = 0.85, relwidth = 0.1)





window = Window()
window.maxsize(1000, 800)

window.mainloop()
