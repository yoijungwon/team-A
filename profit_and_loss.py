from pathlib import Path
import csv

#create a file to csv file.
fp = Path.cwd()/"csv_reports"/"Profit_and_loss.csv"

#read the csv file to append day and net profit from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) #skip header

    #create an emply list to store the net profit and the 90 days
    profit_and_loss = []

    #append net profit and days into the profit_and_loss list
    for row in reader:
        #get the net profit and days
        #and append to profit_and_loss list
        profit_and_loss.append([row[0], row[4]])

#print(profit_and_loss)


def profit_deficit():
    """
    Find all the days which has profit deficit happened, and the amount.
    Parameters are not required.
    """
    value = [] #create a value list to store all the net profit
    day_list = [] #create a list to store all the days from 0 to 90.
    diff_list = [] #create a list to store the amount difference of net profit between the present day and the previous day
    amount_index = [] #create a list to store the index of the negative value to find out the days with profit deficit 
    day_amount_list = [] #create a list to store the negative value. 
    # Note: negative value means the value is a profit deficit.
    
    for item in profit_and_loss:
        #iterate each row of data in profit_and_loss list
        day = item[0]
        day_list.append(day) #append all days (0 to 90 days) into day_list
        net_profit = int(item[1]) #typecast net profit into integer
        value.append(net_profit) #append all the net_profit into value list

        for i in range(len(value)):
            #calculate the profit deficit by subtracting the previous day's net profit from the present day's net profit
            diff = value[i] - value[i-1]
        diff_list.append(diff) #append all the calculated profit difference

    
    for amount in diff_list:
        if amount < 0:
            day_amount_list.append(amount) #append all the negative value from diff_list into day_amount_list
            amount_index.append(diff_list.index(amount)) #append the index of the negative values 
   
    summary_report_pl = ""  #create an empty string
    for i in range(len(amount_index)):
        summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[i]) + ", AMOUNT: " + "USD" + str(day_amount_list[i]).replace("-", "")
    
    with open("summary_report.txt", "a") as file:
        file.write(summary_report_pl)

profit_deficit()

    
