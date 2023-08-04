from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"cash_on_hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    cash_on_hand = []
    
    for row in reader:
        cash_on_hand.append([row[0], row[1]])

# print(cash_on_hand)
# print()

def cash_deficit():
    # day_amount_dict = {}
    coh_list = []  # to store the different cash on hand value
    day_list = []   # store the 90 days 
    cash_diff_list = []   #to store the difference in cash on hand for each day
    index_list = []   #to store the index of the difference in cash on hand from cash_diff_List to flag out the days with cash deficit
    cash_deficit_list = []
    for item in cash_on_hand:
        day = item[0]
        day_list.append(day)
        coh = int(item[1])
        coh_list.append(coh)
        
        for i in range(len(coh_list)):
            cash_diff = coh_list[i] - coh_list[i-1]
        cash_diff_list.append(cash_diff)


    for cash in cash_diff_list:
        if cash < 0:
            cash_deficit_list.append(cash)
            index_list.append(cash_diff_list.index(cash))
       
    summary_report = ""
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[0]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[0]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[1]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[1]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[2]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[2]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[3]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[3]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[4]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[4]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[5]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[5]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[6]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[6]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[7]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[7]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[8]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[8]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[9]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[9]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[10]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[10]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[11]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[11]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[12]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[12]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[13]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[13]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[14]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[14]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[15]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[15]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[16]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[16]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[17]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[17]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[18]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[18]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[19]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[19]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[20]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[20]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[21]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[21]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[22]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[22]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[23]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[23]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[24]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[24]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[25]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[25]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[26]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[26]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[27]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[27]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[28]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[28]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[29]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[29]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[30]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[30]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[31]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[31]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[32]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[32]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[33]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[33]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[34]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[34]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[35]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[35]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[36]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[36]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[37]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[37]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[38]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[38]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[39]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[39]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[40]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[40]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[41]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[41]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[42]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[42]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[43]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[43]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[44]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[44]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[45]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[45]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[46]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[46]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[47]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[47]).replace("-", "")
    summary_report +=  "\n" + "[CASH DEFICIT] DAY: " + str(index_list[48]) + ", AMOUNT: " + "USD" + str(cash_deficit_list[48]).replace("-", "")

    with open("summary_report.txt", "a") as file:
        file.write(summary_report)

cash_deficit()