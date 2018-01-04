import os
import csv

total_months = 0
total_revenue = 0
revenue_change_list = []
average_revenue_change = []
greatest_increase_in_revenue = []
greatest_decrease_in_revenue = []
current_month = 1154293
previous_month = 0
Greatest_month = ""
Greatest_revenue = 0
Lowest_month = ""
Lowest_revenue = 0
header_0 = "Financial Analysis"
header_1 = "Total Months"
header_2 = "Total Revenue"
header_3 = "Average Revenue Change"
header_4 = "Greatest Increase in Revenue"
header_5 = "Greatest Decrease in Revenue"

bank_data = os.path.join("budget_data_1.csv")
with open(bank_data, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
   
#    next(csv_reader)   
#    for row in csv_reader:
#        total_months = total_months + 1

#print(total_months)

#   next(csv_reader)
#   for row in csv_reader:
#       total_revenue = int(row[1]) + (total_revenue) 
        
#print(total_revenue) 

    next(csv_reader)
    for row in csv_reader:
        total_months = total_months + 1
        total_revenue = int(row[1]) + (total_revenue)
        revenue_change = int(row[1]) - (previous_month) 
        previous_month = int(row[1])
        revenue_change_list.append(revenue_change)
        average_revenue_change = (sum(revenue_change_list)/total_months)
        if Greatest_revenue < revenue_change:
            Greatest_revenue = revenue_change
            Greatest_month = (row[0])     
        if Lowest_revenue > revenue_change:
            Lowest_revenue = revenue_change
            Lowest_month = (row[0])

print(header_0 + ":")
print("-------------------------------------------------")
print(header_1 + ": " + str(total_months))
print(header_2 + ": " + "$" + str(total_revenue))
print(header_3 + ": " + "$" + str(average_revenue_change))
print(header_4 + ": " + Greatest_month + " = " + "$" + str(Greatest_revenue))
print(header_5 + ": " + Lowest_month + " = " + "$" + str(Lowest_revenue)) 

#average_revenue_change = (sum(revenue_change_list)/total_months)        
#print(average_revenue_change) 
