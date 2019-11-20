import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       canvas = tk.Canvas(root, height=700, width=900)
       canvas.pack()


       background_image = tk.PhotoImage(file='C:\\Users\\Sephi\\Desktop\\Python\\Final\\flavortown.png')
       background_label = tk.Label(root, image=background_image)
       background_label.place(relwidth=1, relheight=1)


       top_frame = tk.Frame(root, bg='#dc9955', bd=5)
       top_frame.place(relx = 0.5, rely = 0.05, relwidth=0.75, relheight=0.10, anchor='n')

       header_label = tk.Label(top_frame, text = "Welcome to the restaurant selector.\nLet's ride this gravy train to Flavortown!", bg='#e5d6b9', font='Arial')
       header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

       bottom_frame = tk.Frame(root, bg='#dc9955', bd=10)
       bottom_frame.place(relx = 0.5, rely = 0.4, relwidth=0.75, relheight=0.2, anchor='n')


       header_label = tk.Label(bottom_frame, text = 'What would you like to do?', bg='#e5d6b9', font='Arial', anchor='n', pady=15)
       header_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

       check_restaurants = tk.Button(bottom_frame, text = 'Check Restaurants', fg='white', bg='#4e3632')
       check_restaurants.place(relx=0.10, rely=0.45)

       add_restaurants = tk.Button(bottom_frame, text = 'Add Restaurants', fg='white', bg='#4e3632')
       add_restaurants.place(relx=0.43, rely=0.45)

       choose_restaurants = tk.Button(bottom_frame, text = 'Choose Restaurants', fg='white', bg='#4e3632')
       choose_restaurants.place(relx=0.74, rely=0.45)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()