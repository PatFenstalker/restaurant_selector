import tkinter as tk
from tkinter import messagebox

def show_restaurants():

    data = open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'r')

    restaurants_in_data_file = []

    for line in data:
        if 'Name: ' in line:
            restaurants_in_data_file.append((str(line.strip()[6:])))
    
    messagebox.showinfo(
        "Restaurants", 'Restaurants in the list:\n\n' + '\n'.join(map(''.join, set(restaurants_in_data_file))))


root = tk.Tk()
root.title('Restaurant Selector')

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


check_restaurants = tk.Button(bottom_frame, text = 'Check Restaurants', fg='white', bg='#4e3632', command=show_restaurants)
check_restaurants.place(relx=0.10, rely=0.45)


add_restaurants = tk.Button(bottom_frame, text = 'Add Restaurants', fg='white', bg='#4e3632')
add_restaurants.place(relx=0.43, rely=0.45)


choose_restaurants = tk.Button(bottom_frame, text = 'Choose Restaurants', fg='white', bg='#4e3632')
choose_restaurants.place(relx=0.74, rely=0.45)


root.mainloop()