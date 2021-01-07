import os
import csv

# import budget_data.csv as csv
budget_data= os.path.join("PyBank", "Resources", "budget_data.csv")

avg_change = []
max_mon = []
min_mon = []

with open(budget_data, newline='', encoding= "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    data_header = next(csv_file)
    #check data_header to look for format
    print(f"{data_header}")
    # number of rows to get mon_total
    mon_total= len()
#cycle through rows
    for row in csv_reader:

#save information in new csv_file
        zipped= zip(mon_total, avg_change, max_mon, min_mon)
        output_file= os.path.join("PyBank.csv")
#write new results to text file
with open(output_file, "w", newline='') as processed:
    writer= csv.writer(processed)
    writer.writerow("Month_Total","Average_Change","Greatest_Increase","Greatest_Decrease")
    writer.writerows(zipped)

#dol_total =
#avg_change =
#max_mon =
#min_mon =

#final print statement
#print("Financial Analysis")
#print("----------------------------------------")
#print(f"Total Months: {mon_total}")
#print(f"Total: {dol_total}")
#print(f"Average Change: {avg_change}")
#print(f"Greatest Increase in Profits: {max_mon} ([])")
#print(f"Greatest Decrease in Profits {min_mon}([])")
