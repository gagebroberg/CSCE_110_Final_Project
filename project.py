# File: project.py
# Author: Gage Broberg, Brandon Torres, Jermome Porter
# Date: 05/01/2020
# E-mail: gagebroberg@tamu.edu, brandontorres28@tamu.edu, officialjp201@tamu.edu
# Description: The Dealership Manager, This program takes in data from a CSV file and uses that data to compute multiple data points for the dealer manager. It also creates visual graphs for the manager to better visualize the data in the CSV file.

import matplotlib.pyplot as plt
import csv

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



# creates the bar chart for question 2
fig = plt.figure(1)
plt.bar(states, sales)
plt.xlabel("State", fontsize= 16)
plt.ylabel("Amount of sale", fontsize = 16)
plt.title("Amount of sale in different states", fontsize = 16)

# creates the line chart for question 3
fig2 = plt.figure(2)
plt.title('Amount of Sales', fontsize = 16)
plt.xlabel('Months of the year', fontsize = 16)
plt.ylabel('Sales in Dollars', fontsize = 16)
# creating the X values
months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# creating the y values
y_val = []
for value in contract_date_and_price_dict.values():
    y_val.append(value)
plt.plot(months, y_val)

# turning off scientific notation
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

# we need the code to graph the question 4 pie chart here


# we need the code to graph the last line graph for question 5 here


plt.show()

