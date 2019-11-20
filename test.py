def show_restaurants():

    restaurants_in_data_file = []

    with open('C:\\Users\\Sephi\\Desktop\\Python\\Final\\restaurant_database.txt', 'r') as data:
        for line in data:
            if 'Name: ' in line:
                restaurants_in_data_file.append((str(line.strip()[6:])))
    
    for item in restaurants_in_data_file:
        print(item)


show_restaurants()