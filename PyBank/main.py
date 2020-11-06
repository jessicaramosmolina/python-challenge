#main script to run analysis
#total months in csv file
#sum of of total net profit and loss
#calculate the average change
#pull max value in csv file
#pull min value in csv file

import csv
import os
import sys


csv_path = os.path.join('Resources/budget_data.csv')

month_count = 0
total_profit = 0
last_profit = 0
max_value = -9999999
max_month = "" 
min_value = 9999999
min_month = ""
total_change = 0
average = 0
profit = 0
profit_list=[]
profit_change_list=[]
total_profit_change=0
month_list=[]

with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_reader = next(csvreader) 


    for row in csvreader:
        month_count += 1
        if month_count == 1:
            last_profit = int(row[1])
            total_profit += int(row[1])
        else:
            if (int(row[1]) - last_profit) > max_value:
                max_value = int(row[1]) - last_profit
                max_month = row[0]
            if (int(row[1]) - last_profit) < min_value:
                min_value = int(row[1]) - last_profit
                min_month = row[0]
            total_change += int(row[1]) - last_profit
            total_profit += int(row[1])
            last_profit = int(row[1])


    average = total_change/(month_count-1)
    average = round(average,2)

print('Financial Analysis')
print("--------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {max_month}  (${max_value})')
print(f'Greatest Decrease in Profits: {min_month} (${min_value})')

stdoutOrigin=sys.stdout 
txtPath = os.path.join("Analysis/financial_analysis.txt")
sys.stdout = open(txtPath, "w")
