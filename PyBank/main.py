import os
import csv

#loading data files 
file_location = "Resources/budget_data.csv"


#assigning variables and assigning to start at 0
total_month = 0
total_revenue = 0
previous_revenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
largest_increase = 0
largest_increase_month = 0
largest_decrease = 0
largest_decrease_month = 0

#read budget_data.csv file
with open(file_location, "r") as revenueData:
   reader = csv.reader(revenueData, delimiter=",")
   
   csvheader = next(reader)
   row = next(reader)

   previous_row = int(row[1])
   total_month += 1
   total_revenue += int(row[1])
   largest_increase = int(row[1])
   largest_increase_month = row[0]

#create loop through the data to find
   for row in reader:
       #total variable assignment 
           total_month = total_month + 1
           total_revenue = total_revenue + int(row[1])

#delta revenue 
           revenue_change = int(row[1]) - previous_revenue
           month_of_change.append(revenue_change)
           previous_revenue = int(row[1])
           revenue_change_list.append(row[0])

           #largest increase assignment
           if int(row[1]) > largest_increase:
               largest_increase = int(row[1])
               largest_increase_month = row[0]


           if (int(row[1]) < largest_decrease):
               largest_decrease = int(row[1])
               largest_decrease_month= row[0]
        
# average revenue calculation after loop
revenue_avg = sum(month_of_change) / len(month_of_change)

maximum = max(month_of_change)

minimum = min(month_of_change)

#print output
output = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${revenue_avg:.2f}\n"
    f"Greatest Increase in Profits: {largest_increase_month} (${maximum})\n"
    f"Greatest Decrease in Profits: {largest_decrease_month} (${minimum})\n"
)

print(output)

output_file_location = "PyBank"


#write to text file

with open(output_file_location, "w") as txtfile:
    txtfile.write(output)


