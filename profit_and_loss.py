from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"Profit_and_loss.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    profit_and_loss = []

    for row in reader:
        profit_and_loss.append([row[0], row[4]])

# print(profit_and_loss)


def profit_deficit():
    value = []
    day_list = []
    diff_list = []
    amount_index = []
    day_amount_list = []
    
    for item in profit_and_loss:
        day = item[0]
        day_list.append(day)
        net_profit = int(item[1])
        value.append(net_profit)

        for i in range(len(value)):
            diff = value[i] - value[i-1]
        diff_list.append(diff)

    
    for amount in diff_list:
        if amount < 0:
            day_amount_list.append(amount)
            amount_index.append(diff_list.index(amount))
    
    # print(day_amount_list)
    # print(amount_index) 
         
        
   
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

    
