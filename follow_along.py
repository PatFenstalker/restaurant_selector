from tkinter import *
from PIL import Image, ImageTk


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

        background_image = PhotoImage(file='C:\\Users\\Sephi\\Desktop\\Python\\Final\\flavortown.png')
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

        background_image = PhotoImage(file='C:\\Users\\Sephi\\Desktop\\Python\\Final\\flavortown.png')
        background_label = Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        bottom_frame = Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.1, relwidth=0.4, relheight=0.75, anchor='n')

        data = open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'r')

        restaurants_in_data_file = []

        for line in data:
                if 'Name: ' in line:
                    restaurants_in_data_file.append((str(line.strip()[6:])))


        header_label = Label(bottom_frame, text = 'Restaurants currently in the list:\n\n' + '\n'.join(map(''.join, set(restaurants_in_data_file))), bg='#e5d6b9', font='Arial', anchor='n')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command= lambda:controller.show_frame(LandingPage))
        back.place(relx = 0.45, rely = 0.9)


class AddRestaurants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        canvas = Canvas(self, height=800, width=1000)
        canvas.pack()

        background_image = PhotoImage(file='C:\\Users\\Sephi\\Desktop\\Python\\Final\\flavortown.png')
        background_label = Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        bottom_frame = Frame(self, bg='#dc9955', bd=10)
        bottom_frame.place(relx = 0.5, rely = 0.25, relwidth=0.5, relheight=0.3, anchor='n')

        header_label = Label(bottom_frame, text = 'Enter the restaurant you would like to add to the list.', bg='#e5d6b9', font='Arial', anchor='n', pady=25)
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        entry_field = Text(bottom_frame, font= 'Arial', width = 20, height = 1, bd = 5)
        entry_field.place(relx = 0.13, rely = 0.35)

        def retrieve_input():
            with open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'a+') as file:
                user_input = entry_field.get("1.0","end-1c")
                n = '\n\nName: '
                file.write(n + user_input.title())

        data = open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'r')

        restaurants_in_data_file = []

        for line in data:
                if 'Name: ' in line:
                    restaurants_in_data_file.append((str(line.strip()[6:])))


        add_to_list = Button(bottom_frame, text = 'Add', fg='white', bg='#4e3632')
        add_to_list.place(relx = 0.615, rely = 0.35, relwidth = 0.25, relheight = 0.13, command = retrieve_input())

        back = Button(bottom_frame, text = 'Back', fg='white', bg='#4e3632', command = lambda:controller.show_frame(LandingPage))
        back.place(relx = 0.5, rely = 0.75)


class ChooseRestaurants(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        canvas = Canvas(self, height=800, width=1000)
        canvas.pack()

        background_image = PhotoImage(file='C:\\Users\\Sephi\\Desktop\\Python\\Final\\flavortown.png')
        background_label = Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(relheight = 1, relwidth = 1)
        
        top_frame = Frame(self, bg='#dc9955', bd=5)
        top_frame.place(relx = 0.5, rely = 0.05, relwidth=0.75, relheight=0.10, anchor='n')

        header_label = Label(top_frame, text = "Choose a Restaurant to go to.", bg='#e5d6b9', font='Arial')
        header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        back = Button(self, text = 'Back', command= lambda:controller.show_frame(LandingPage))
        back.pack()


window = Window()
window.maxsize(1000, 800)

window.mainloop()
