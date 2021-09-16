# coding: UTF-8 -A variable-width character encoding used for electronic communication.
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from os import read
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('menu_data.csv')
sales_filepath = Path('sales_data.csv')



def read_data():
    """
    This function read in the menu data and sales data, append it into the menu list and sales list , return menu list and sales list.
    """
    menu = []
    sales = []
    with open(menu_filepath,'r') as f:
        read_file = csv.reader(f)
        next(read_file)
        for row in read_file:
            menu.append(row)


    with open(sales_filepath,'r') as f:
        read_file = csv.reader(f)
        next(read_file)
        for row in read_file:
            sales.append(row)
    return menu,sales



def main(menu,sales):
    """
    The Purpose of this function is to generated the aggreate per product result and store it in to dictionary named report and save that result in the text file.
    The Parameter this function take is menu data and sales data, in the form of lists which were return by read_data function. 
    The report dict object hold our key-value pairs of items and metrics
    """
    
    report = {}
    items_list = []
    
    for row in sales:
        quantity = int(row[3])
        menu_item = row[4]
        if menu_item not in report:
            report[menu_item] =	{
                                    "01-count": 0,
                                    "02-revenue": 0,
                                    "03-cogs": 0,
                                    "04-profit": 0,
                                    }
        for menu_row in menu:
            item = menu_row[0]
            price = float(menu_row[3])
            cost = int(menu_row[4])
            if menu_item == item:
                profit = price-cost
                report[menu_item]["01-count"] += quantity
                report[menu_item]["02-revenue"] += price*quantity
                report[menu_item]["03-cogs"] += cost*quantity
                report[menu_item]["04-profit"] +=profit*quantity 
        else:
            print(f"{menu_item} does not equal {item}! NO MATCH!") 

    file_obj = open("Report.txt","w", newline='')    
    
    for menu_item in sales:
        items_list.append(menu_item[4])
    remove_duplicate = list(dict.fromkeys(items_list))

    for i in range(len(remove_duplicate)):
        file_obj.write(remove_duplicate[i]+" "+str(report[remove_duplicate[i]])+'\n') 
       

if __name__ == '__main__':
    menu,sales = read_data()
    main(menu,sales)    
