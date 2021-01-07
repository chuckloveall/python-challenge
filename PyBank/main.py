import os
import csv

# import budget_data.csv as csv
budget_data= os.path.join("PyBank", "Resources", "budget_data.csv")
#are empty lists necessary for all??
avg_change = []
#open csv file, encoding as UTF-8. 2 columns of data: Date and Profit/Losses
#Date format is MMM-YYYY
#Profit/Losses format is a postive or negative integer sum for the Month
with open(budget_data, newline='', encoding= "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    data_header = next(csv_file)
    #check data_header to look for format
    print(f"{data_header}")
    # number of rows to get mon_total
    # what variable to take len of??
    # will len give proper number of rows?
    # mon_total= len()
#cycle through rows
    for row in csv_reader:
        dol_total= sum(row[1])
        #avg_change iterate after appending to list, ?
        #change = ((i+1)-i) or (next - current) ?
        #append this change answer to new_list_Change ?
        #then do operation of average(new_list_Change) ?
        max_mon= max(row[1])
        min_mon= min(row[1])
#save information in new csv_file
        zipped= zip(mon_total, avg_change, max_mon, min_mon)
        output_file= os.path.join("PyBank.csv")
#write new results to text file
with open(output_file, "w", newline='') as processed:
    writer= csv.writer(processed)
    writer.writerow("Month_Total","Average_Change","Greatest_Increase","Greatest_Decrease")
    writer.writerows(zipped)


#final print statement
#print("Financial Analysis")
#print("----------------------------------------")
#print(f"Total Months: {mon_total}")
#print(f"Total: {dol_total}")
#print(f"Average Change: {avg_change}")
#print(f"Greatest Increase in Profits: {max_mon}")
#print(f"Greatest Decrease in Profits {min_mon}")
