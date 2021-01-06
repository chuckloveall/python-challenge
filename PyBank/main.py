import os
import csv

# import budget_data.csv as csv
budget_data= os.path.join("budget_data.csv")
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    data_header = next(csv_file)
    #check data_header to look for format
    print(f"{data_header}")
#assign variables
mon_total =
dol_total =
avg_change =
max_mon =
min_mon =

#final print statement
print(f"Total Months: {mon_total}")
print(f"Total: {dol_total}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {max_mon} ([])")
print(f"Greatest Decrease in Profits {min_mon}([])")
