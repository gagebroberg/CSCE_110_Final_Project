# File: project.py
# Author: Gage Broberg, Brandon Torres, Jermome Porter
# Date: 05/01/2020
# E-mail: gagebroberg@tamu.edu, brandontorres28@tamu.edu, officialjp201@tamu.edu
# Description: The Dealership Manager, This program takes in data from a CSV file and uses that data to compute multiple data points for the dealer manager. It also creates visual graphs for the manager to better visualize the data in the CSV file.

import matplotlib.pyplot as plt
import csv

def amount_sale_month_state(state_date_sale_dict, state):
    '''This function takes the state, date, and sale amount info from the document, and a specfic state as an input. Then for that specific state it adds each amount to its corresponding month in the sale_per_month_list so that we can use that list as the y points in the graph for that state.''' 
    sale_per_month_list = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    for states, date_sale in state_date_sale_dict.items():
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


def amount_sale_brand(brand):
    '''Returns the total amount of sale for the inputed brand from the csv file'''
    with open("2019_car_sale.csv") as car_data_file:
        car_data_reader = csv.reader(car_data_file)
        brand_amount = 0
        header = True
        for deal in car_data_reader:
            # This if statement is able to skip the first wor of the csv file, which is just the title headers
            if header:
                header = False
                continue
            if deal[2] == str(brand):
                
                brand_amount = brand_amount + int(deal[5].replace(",", ""))
                
    return brand_amount


def section_1():     
    '''This Function runs the code required for section 1 of the output and returns any necessary variables for futher functions'''
    print("=" * 8 + "Dataset details" + "=" * 8)
    print()
    
    # opening the csv file and creating our handle to read the data
    car_data_file = open("2019_car_sale.csv")
    car_data_reader = csv.reader(car_data_file)
    num_deals = 0
    
    # creating our initial empty sets and lists for the data to be stored in
    models_set = set()
    raw_contract_date_and_price_dict = {}
    price_state_dict = {}
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
        price_state_dict.update({int(deal[5].replace(",", "")): deal[3]})
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
    
    # initializing state totals
    texas = 0
    california = 0
    florida = 0
    nevada = 0
    ohio = 0
    
    # adding each of the revenues by state into the state total
    for revenue, state in price_state_dict.items():
        if state == "Texas":
            texas += revenue
        elif state == "California":
            california += revenue
        elif state == "Florida":
            florida += revenue
        elif state == "Nevada":
            nevada += revenue
        elif state == "Ohio":
            ohio += revenue
    
    state_dict = {"Texas": texas, "California": california, "Florida": florida, "Ohio": ohio, "Nevada": nevada}
    state_dict_sorted = sorted(state_dict.items(), key=lambda item: item[1], reverse=True)
    print(f"Most number of cars sold ({state_dict_sorted[0][1]}) in {state_dict_sorted[0][0]}.")
    
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
        brand_amount = amount_sale_brand(brand)
        brand_dict.update({brand: brand_amount})
    others = 0
    percentage_brand_dict = {}
    other_category_cutoff = sum(sales_amount_list) * 0.04
    for brand, sales in brand_dict.items():
        if sales < other_category_cutoff:
            others += sales / sum(sales_amount_list) * 100
        else:
            percentage_brand_dict.update({brand: sales / sum(sales_amount_list) * 100})
    percentage_brand_dict.update({"Others": others})
    percentage_brand_dict_sorted = sorted(percentage_brand_dict.items(), key=lambda item: item[1], reverse=True)
    for brand_and_percentage in percentage_brand_dict_sorted:
        print(f"{brand_and_percentage[0]} : {round(brand_and_percentage[1], 2)}%")
    print()
    print("=" * 19)
    
    return state_dict, contract_date_and_price_dict, percentage_brand_dict_sorted


def section_2(state_dict):
    '''Creates bar graph for section 2 of output'''
    # data sets for entry into the graphs
    states = ["Texas", "California", "Florida", "Ohio", "Nevada"]
    sales = list(state_dict.values())
    colors = ['b', 'g', 'r', 'c', 'm']
    
    # creates the bar chart for question 2
    plt.figure(1)
    plt.bar(states, sales, color= colors)
    plt.xlabel("State", fontsize= 16)
    plt.ylabel("Amount of sale", fontsize = 16)
    plt.title("Amount of sale in different states", fontsize = 16, bbox={'facecolor': '0.5', 'pad': 2})


def section_3(contract_date_and_price_dict):
    '''Creates graph for section 3 of the output'''
    # creates the line chart for question 3
    plt.figure(2, figsize = (9,5))
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


def section_4(percentage_brand_dict_sorted):
    '''Creates pie chart for section 4 of the output'''
    # we need the code to graph the question 4 pie chart here
    plt.figure(3)
    labels = []
    sizes = []
    for brand_percentage in percentage_brand_dict_sorted:       #Separates the dictionary into two lists to use as labels and sizes for the pie graph.
        labels.append(brand_percentage[0]) 
        sizes.append(round(brand_percentage[1], 1))
    colors = ['b', 'g', 'r', 'c', 'm', 'y']
    number = 0
    for num in range(len(percentage_brand_dict_sorted)):    #Helps assign colors to all elements of chart
        if number == len(percentage_brand_dict_sorted) - 1:
            number = 0
        colors.append(colors[number])
        number += 1
    plt.title('Percentage of Colors by Different Car Brands', bbox={'facecolor':'0.5', 'pad':7})
    plt.pie(sizes, labels = labels, colors = colors, autopct='%1.1f%%')


def section_5():
    '''Creates graph for last section of output'''
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
        
    plt.figure(4, figsize = (12,5))       #Plots the points with respective legend
    
    plt.xlabel('Months')        #Customization
    plt.ylabel('Amount of Sale')
    plt.title('Amount of Sale in Different Months in Each State')
    
    plt.plot(x_points, texas_y_points, color = 'r')
    plt.plot(x_points, cali_y_points, color = 'b')
    plt.plot(x_points, florida_y_points, color = 'c')
    plt.plot(x_points, ohio_y_points, color = 'y')
    plt.plot(x_points, nevada_y_points, color = 'g')
    plt.legend(['Texas', 'California','Florida','Ohio','Nevada'])


def main():
    '''Runs the different section functions under one main function, getting variables as needed'''
    state_dict, contract_date_and_price_dict, percentage_brand_dict_sorted = section_1()
    section_2(state_dict)
    section_3(contract_date_and_price_dict)
    section_4(percentage_brand_dict_sorted)
    section_5()
    plt.show()


main()