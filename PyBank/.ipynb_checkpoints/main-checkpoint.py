# importing csv  module
import csv


def getAllData():
    """
    The Purpose of this function is to read file budget_data.csv, retrive data from the file and return list.
    """
    #DictReader = creates CSV object that behaves like a Python orderedDict. 
    allData = []
    with open("budget_data.csv","r",newline='') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            allData.append(row)
    return allData


def total_Months(months):
    """
    The Purpose of this function is to calculate the total months
    Parameter this function take is the list return by the getAllData function from that we only extract Date.
    This function return total months and list of the months.
    """
    months_list = []
    for dic in months:
        months_list.append(dic["Date"])
    total_months = len(months_list)
    return total_months,months_list


def nettotal_ProfitLoss(profit_loss):
    """
    The Purpose of this function is to calculate the net profit/loss
    Parameter this function take is the list return by the getAllData function from that we only extract profit/loss.
    return net profit and list of profit loss .
    """
    profit_loss_list = []
    for dic in profit_loss:
        var=dic["Profit/Losses"]
        profit_loss_list.append(int(var))
    Sum = sum(profit_loss_list)
    return Sum,profit_loss_list


def average_Change(profit_loss):
    """
    The Purpose of this function is to calculate the average of the change in profit/loss.
    Parameter this function takes is the list return by the nettotal_ProfitLoss function.
    return average of the change in profit/loss and the list of the avaerage change.
    """
    average_change_list = []
    for i in range(len(profit_loss)-1): 
        average_change_list.append(profit_loss[i+1]-profit_loss[i])
    averageChange = round(sum(average_change_list)/len(average_change_list),2)
    
    return averageChange,average_change_list

def greatest_Increase_and_Decrease_InProfits(profit_change_list,month_list):
    """
    The Purpose of this function is to calculate the greatest increase and decrease in the profit.
    The Parameter this function takes is the list of the change in profit/loss from previous month to current month and the second parameter is the list of the months return by total_Months function.
    This function return the date ... in which maximum profit is made, also return  date in which greatest decrease in losses and value of that losss.
    """
    max_value = 0
    min_value = 0
    for i in range(len(profit_change_list)):
        if max_value < profit_change_list[i]:
            max_value = profit_change_list[i]
            max_profit_month = month_list[i+1]
        if min_value > profit_change_list[i]:
            min_value = profit_change_list[i]
            min_profit_month = month_list[i+1]

    return max_profit_month,max_value,min_profit_month,min_value

def save_TO_Txt(total_months,total,average,max_increase_month,max_increase,min_increase_month,min_decrease):
    """
    The Purpose of this function is to save data into the text file.
    The parameter this function takes is the total months, net total amount of profit/loss, average change in profit/loss, date and amount of greatest increase and decrease in profit/loss.

    """
    with open("Result.txt","w") as f:
        f.write("Financial Analysis"+'\n')
        f.write("----------------------------"+'\n')
        f.write("Total Months: {} \n".format(total_months))
        f.write("Total: ${} \n".format(total))
        f.write("Total Average: ${} \n".format(average))
        f.write("Greatest Increase in Profits: {} ( ${} ) \n".format(max_increase_month,max_increase))
        f.write("Greatest Decrease in Profits: {} ( ${} ) \n".format(min_increase_month,min_decrease))

def printFuction(total_months,total,average,max_increase_month,max_increase,min_increase_month,min_decrease):
    """
    The Purpose of this function is to print data in the terminal.
    The parameter this function takes is the total months,net total amount of profit/loss, average change in profit/loss, date and amount of greatest increase and decrease in profit/loss.
    """
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: {}".format(total_months))
    print("Total: ${}".format(total))
    print("Average Change: ${}".format(average))
    print("Greatest Increase in Profits: {} (${})".format(max_increase_month,max_increase))
    print("Greatest Decrease in Profits: {} (${})".format(min_increase_month,min_decrease))



if __name__ == '__main__':
    
    budget_data = getAllData()
    months,months_list = total_Months(budget_data)
    net_profitloss,net_profitloss_list = nettotal_ProfitLoss(budget_data)
    averageChange, averageChange_list =average_Change(net_profitloss_list)
    max_increase_month,max_increase,min_increase_month,min_decrease=greatest_Increase_and_Decrease_InProfits(averageChange_list,months_list)
    save_TO_Txt(months,net_profitloss,averageChange,max_increase_month,max_increase,min_increase_month,min_decrease)
    printFuction(months,net_profitloss,averageChange,max_increase_month,max_increase,min_increase_month,min_decrease)