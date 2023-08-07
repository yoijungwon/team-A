from pathlib import Path
import csv

#create a file to csv file.
fp = Path.cwd()/"csv_reports"/"cash_on_hand.csv"

#read the csv file to append day and cash on hand from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)#skip header

    #create an emply list to store the cash on hand and the 90 days
    cash_on_hand = []

    #append net profit and days into the cash_on_hand list
    for row in reader:
        #get the cash on hand and days
        #and append to cash_on_hand list
        cash_on_hand.append([row[0], row[1]])

# print(cash_on_hand)

def cash_deficit():
    """
    Find all the days which has cash deficit happened, and the amount.
    Parameters are not required.
    """

    coh_list = []  # create a coh_list to store the different cash on hand value
    day_list = []   # store all the days from 0 to 90.
    cash_diff_list = []   #to store the difference in cash on hand between the present day and the previous day
    index_list = []   #to store the index of the difference in cash on hand from cash_diff_List to flag out the days with cash deficit
    cash_deficit_list = [] #create a list to store the negative value. 
    # Note: negative value means the value is a cash deficit.

    for item in cash_on_hand:
        #iterate each row of data in cash_on_hand list
        day = item[0]
        day_list.append(day) #append all days (0 to 90 days) into day_list
        coh = int(item[1])  #typecast cash on hand into integer
        coh_list.append(coh) #append all the cash on hand value into value list

        
        for i in range(len(coh_list)):
            #calculate the cash deficit by subtracting the previous day's cash on hand from the present day's cash on hand
            cash_diff = coh_list[i] - coh_list[i-1]
        cash_diff_list.append(cash_diff) #append all the calculated cash difference


    for cash in cash_diff_list:
        if cash < 0:
            cash_deficit_list.append(cash) #append all the negative value from cash_diff_list into cash_deficit_list
            index_list.append(cash_diff_list.index(cash)) #append the index of the negative values
        
       
    summary_report = "" #create an empty string
    for i in range(len(index_list)):
        summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[i]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[i]).replace("-", "")
   
    with open("summary_report.txt", "a") as file:
        file.write(summary_report)

cash_deficit()