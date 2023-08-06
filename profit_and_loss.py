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

print(profit_and_loss)


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
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[0]) + ", AMOUNT: " + "USD" + str(day_amount_list[0]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[1]) + ", AMOUNT: " + "USD" + str(day_amount_list[1]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[2]) + ", AMOUNT: " + "USD" + str(day_amount_list[2]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[3]) + ", AMOUNT: " + "USD" + str(day_amount_list[3]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[4]) + ", AMOUNT: " + "USD" + str(day_amount_list[4]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[5]) + ", AMOUNT: " + "USD" + str(day_amount_list[5]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[6]) + ", AMOUNT: " + "USD" + str(day_amount_list[6]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[7]) + ", AMOUNT: " + "USD" + str(day_amount_list[7]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[8]) + ", AMOUNT: " + "USD" + str(day_amount_list[8]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[9]) + ", AMOUNT: " + "USD" + str(day_amount_list[9]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[10]) + ", AMOUNT: " + "USD" + str(day_amount_list[10]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[11]) + ", AMOUNT: " + "USD" + str(day_amount_list[11]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[12]) + ", AMOUNT: " + "USD" + str(day_amount_list[12]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[13]) + ", AMOUNT: " + "USD" + str(day_amount_list[13]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[14]) + ", AMOUNT: " + "USD" + str(day_amount_list[14]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[15]) + ", AMOUNT: " + "USD" + str(day_amount_list[15]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[16]) + ", AMOUNT: " + "USD" + str(day_amount_list[16]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[17]) + ", AMOUNT: " + "USD" + str(day_amount_list[17]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[18]) + ", AMOUNT: " + "USD" + str(day_amount_list[18]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[19]) + ", AMOUNT: " + "USD" + str(day_amount_list[19]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[20]) + ", AMOUNT: " + "USD" + str(day_amount_list[20]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[21]) + ", AMOUNT: " + "USD" + str(day_amount_list[21]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[22]) + ", AMOUNT: " + "USD" + str(day_amount_list[22]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[23]) + ", AMOUNT: " + "USD" + str(day_amount_list[23]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[24]) + ", AMOUNT: " + "USD" + str(day_amount_list[24]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[25]) + ", AMOUNT: " + "USD" + str(day_amount_list[25]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[26]) + ", AMOUNT: " + "USD" + str(day_amount_list[26]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[27]) + ", AMOUNT: " + "USD" + str(day_amount_list[27]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[28]) + ", AMOUNT: " + "USD" + str(day_amount_list[28]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[29]) + ", AMOUNT: " + "USD" + str(day_amount_list[29]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[30]) + ", AMOUNT: " + "USD" + str(day_amount_list[30]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[31]) + ", AMOUNT: " + "USD" + str(day_amount_list[31]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[32]) + ", AMOUNT: " + "USD" + str(day_amount_list[32]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[33]) + ", AMOUNT: " + "USD" + str(day_amount_list[33]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[34]) + ", AMOUNT: " + "USD" + str(day_amount_list[34]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[35]) + ", AMOUNT: " + "USD" + str(day_amount_list[35]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[36]) + ", AMOUNT: " + "USD" + str(day_amount_list[36]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[37]) + ", AMOUNT: " + "USD" + str(day_amount_list[37]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[38]) + ", AMOUNT: " + "USD" + str(day_amount_list[38]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[39]) + ", AMOUNT: " + "USD" + str(day_amount_list[39]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[40]) + ", AMOUNT: " + "USD" + str(day_amount_list[40]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[41]) + ", AMOUNT: " + "USD" + str(day_amount_list[41]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[42]) + ", AMOUNT: " + "USD" + str(day_amount_list[42]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[43]) + ", AMOUNT: " + "USD" + str(day_amount_list[43]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[44]) + ", AMOUNT: " + "USD" + str(day_amount_list[44]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[45]) + ", AMOUNT: " + "USD" + str(day_amount_list[45]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[46]) + ", AMOUNT: " + "USD" + str(day_amount_list[46]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[47]) + ", AMOUNT: " + "USD" + str(day_amount_list[47]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[48]) + ", AMOUNT: " + "USD" + str(day_amount_list[48]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[49]) + ", AMOUNT: " + "USD" + str(day_amount_list[49]).replace("-", "")
    summary_report_pl +=  "\n" + "[PROFIT DEFICIT] DAY: " + str(amount_index[50]) + ", AMOUNT: " + "USD" + str(day_amount_list[50]).replace("-", "")

    with open("summary_report.txt", "a") as file:
        file.write(summary_report_pl)

profit_deficit()

    
