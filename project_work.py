# File: project.py
# Author: Gage Broberg, Brandon Torres, Jermome Porter
# Date: 05/01/2020
# E-mail: gagebroberg@tamu.edu, brandontorres28@tamu.edu, officialjp201@tamu.edu
# Description: The Dealership Manager, This program takes in data from a CSV file and uses that data to compute multiple data points for the dealer manager. It also creates visual graphs for the manager to better visualize the data in the CSV file.

import matplotlib.pyplot as plt
import csv
import random

def amount_sale_month_state(state_date_sale_dict, state):
    '''This function takes the state, date, and sale amount info from the document, and a specfic state as an input. Then for that specific state it adds each amount to its corresponding month in the sale_per_month_list so that we can use that list as the y points in the graph for that state.''' 
    sale_per_month_list = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    for states, date_sale in date_state_sale_dict.items():
        if states == state:
            for items in date_sale:
                if items[0] == '1':
                    sale_per_month_list[0][0] += items[1]
                elif items[0] == '2':
                    sale_per_month_list[1][0] += items[1]
                elif items[0] == '3':
                    sale_per_month_list[2][0] += items[1]
                elif items[0] == '4':
                    sale_per_month_list[3][0] += items[1]
                elif items[0] == '5':
                    sale_per_month_list[4][0] += items[1]
                elif items[0] == '6':
                    sale_per_month_list[5][0] += items[1]
                elif items[0] == '7':
                    sale_per_month_list[6][0] += items[1]
                elif items[0] == '8':
                    sale_per_month_list[7][0] += items[1]
                elif items[0] == '9':
                    sale_per_month_list[8][0] += items[1]
                elif items[0] == '10':
                    sale_per_month_list[9][0] += items[1]
                elif items[0] == '11':
                    sale_per_month_list[10][0] += items[1]
                elif items[0] == '12':
                    sale_per_month_list[11][0] += items[1]
    return sale_per_month_list
                

print("=" * 8 + "Dataset details" + "=" * 8)
print()

# opening the csv file and creating our handle to read the data
car_data_file = open("2019_car_sale.csv")
car_data_reader = csv.reader(car_data_file)
num_deals = 0

# creating our initial empty sets and lists for the data to be stored in
models_set = set()
raw_contract_date_and_price_dict = {}
brands_list = []
brands_set = set()
safety_ratings_set = set()
colors_set = set()
state_list = []
sales_amount_list = []

# here we are taking the data and inputting it into the previously created sets and lists for use in the program
header = True
for deal in car_data_reader:
    # This if statement is able to skip the first wor of the csv file, which is just the title headers
    if header:
        header = False
        continue
    num_deals += 1
    models_set.add(deal[0])
    raw_contract_date_and_price_dict.update({deal[5]: deal[1].split("/")[0]})
    brands_set.add(deal[2])
    brands_list.append(deal[2])
    state_list.append(deal[3])
    safety_ratings_set.add(deal[4])
    sales_amount_list.append(deal[5])
    colors_set.add(deal[6])

# print statements required in the sample output 1
sales_amount_list = [int(amount.replace(",", "")) for amount in sales_amount_list]
print(f"Total number of deals: {num_deals}")
print(f"Number of different car models: {len(models_set)}")
print(f"Number of different car brands: {len(brands_set)}")
print(f"Number of different car safety ratings: {len(safety_ratings_set)}")
print(f"Number of different car colors: {len(colors_set)}")
print(f"Total amount of sale: {sum(sales_amount_list)}")
print()
print("=" * 32)
print()

# creating a set to hold the number of cars sold in each state data and outputting
state_dict = {}
state_set = set(state_list)
for state in state_set:
    state_dict.update({state_list.count(state): state})
state_dict_sorted = sorted(state_dict.items(), key=lambda item: item[0], reverse=True)
print(f"Most number of cars sold ({state_dict_sorted[0][0]}) in {state_dict_sorted[0][1]}.")

# initializing variables for each month to add to
january = 0
february = 0
march = 0
april = 0
may = 0
june = 0
july = 0
august = 0
september = 0
october = 0
november = 0
december = 0
monthly_sales_dict = {}

# adding each of the values by state into their respective variables
for key, value in raw_contract_date_and_price_dict.items():
    if value == "1":
        january += int(key.replace(",", ""))
    elif value == "2":
        february += int(key.replace(",", ""))
    elif value == "3":
        march += int(key.replace(",", ""))
    elif value == "4":
        april += int(key.replace(",", ""))
    elif value == "5":
        may += int(key.replace(",", ""))
    elif value == "6":
        june += int(key.replace(",", ""))
    elif value == "7":
        july += int(key.replace(",", ""))
    elif value == "8":
        august += int(key.replace(",", ""))
    elif value == "9":
        september += int(key.replace(",", ""))
    elif value == "10":
        october += int(key.replace(",", ""))
    elif value == "11":
        november += int(key.replace(",", ""))
    elif value == "12":
        december += int(key.replace(",", ""))

# creating a dictionary that holds revenue in each individual month and printing the max revenue and month
contract_date_and_price_dict = {
    "January": january,
    "February": february,
    "March": march,
    "April": april,
    "May": may,
    "June": june,
    "July": july,
    "August": august,
    "September": september,
    "October": october,
    "November": november,
    "December": december
}
contract_date_and_price_dict_sorted = sorted(contract_date_and_price_dict.items(), key=lambda item: item[1], reverse=True)
print(f"Maximum amount of sale ({contract_date_and_price_dict_sorted[0][1]}) was in {contract_date_and_price_dict_sorted[0][0]}.")

print()
print("=" * 32)
print()
print("=" * 8 + "Amount of sale based on car brands" + "=" * 8)
print()

# calculating percentages for different car brands and adding them to a dictionary
brand_dict = {}
for brand in brands_set:
    brand_dict.update({brand: brands_list.count(brand)})
others = 0
percentage_brand_dict = {}
other_category_cutoff = num_deals * 0.04
for brand, sales in brand_dict.items():
    if sales < other_category_cutoff:
        others += sales / num_deals * 100
    else:
        percentage_brand_dict.update({brand: sales / num_deals * 100})
percentage_brand_dict.update({"Others": others})
percentage_brand_dict_sorted = sorted(percentage_brand_dict.items(), key=lambda item: item[1], reverse=True)
for brand_and_percentage in percentage_brand_dict_sorted:
    print(f"{brand_and_percentage[0]} : {round(brand_and_percentage[1], 2)}%")
print()
print("=" * 19)

# data sets for entry into the graphs
states = list(set(state_list))
sales = list(state_dict.keys())

colors = ['b', 'g', 'r', 'c', 'm']


# creates the bar chart for question 2
fig = plt.figure(1)
plt.bar(states, sales, color= colors)

plt.xlabel("State", fontsize= 16)
plt.ylabel("Amount of sale", fontsize = 16)
plt.title("Amount of sale in different states", fontsize = 16)

# we need the code for the question 3 graph here


# we need the code to graph the question 4 pie chart here
plt.figure(3)
labels = []
sizes = []
for brand_percentage in percentage_brand_dict_sorted:       #Separates the dictionary into two lists to use as labels and sizes for the pie graph.
    labels.append(brand_percentage[0]) 
    sizes.append(brand_percentage[1])
colors = ['b', 'g', 'r', 'c', 'm', 'y']
number = 0
for num in range(len(percentage_brand_dict_sorted)):    #Helps assign colors to all elements of chart
    if number == len(percentage_brand_dict_sorted) - 1:
        number = 0
    colors.append(colors[number])
    number += 1
plt.pie(sizes, labels = labels, colors = colors, autopct='%1.2f%%')

# we need the code to graph the last line graph for question 5 here
car_data_file = open("2019_car_sale.csv")
car_data_reader = csv.reader(car_data_file)
date_state_sale_dict = {'Texas':[],'Ohio':[],'California':[],'Nevada':[],'Florida':[]}
header = True
for deal in car_data_reader:        #Creates dictionary for the function that will makes the y-points for each state
    if header:
        header = False
        continue    
    date = deal[1].split("/")[0]
    state = deal[3]
    sale = int(deal[5].replace(",", ""))
    date_state_sale_dict[state].append([date, sale])
    
x_points = ['Janurary','February','March','April','May','June','July','August','September','October','November','December']
texas_y_points = amount_sale_month_state(date_state_sale_dict, 'Texas')
cali_y_points = amount_sale_month_state(date_state_sale_dict, 'California')
florida_y_points = amount_sale_month_state(date_state_sale_dict, 'Florida')
ohio_y_points = amount_sale_month_state(date_state_sale_dict, 'Ohio')
nevada_y_points = amount_sale_month_state(date_state_sale_dict, 'Nevada')
car_data_file.close()           #All y-points created

plt.xlabel('Months')        #Customization
plt.ylabel('Amount of Sale')
plt.title('Amount of Sale in Different Months in Each State')

plt.figure(4, figsize = (12,5))       #Plots the points with respective legend

plt.plot(x_points, texas_y_points, color = 'r')
plt.plot(x_points, cali_y_points, color = 'b')
plt.plot(x_points, florida_y_points, color = 'c')
plt.plot(x_points, ohio_y_points, color = 'y')
plt.plot(x_points, nevada_y_points, color = 'g')
plt.legend(['Texas', 'California','Florida','Ohio','Nevada'])

plt.show()
