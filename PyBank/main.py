import os
import csv

# import budget_data.csv as csv
budget_data= os.path.join("Resources", "budget_data.csv")

avg_change = []
mon_total = []
max_mon= []
min_mon= []
dol_total= []
big_change= []
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
        #print(row)
        mon_total.append(row[0])
        dol_total.append(int(row[1]))
        #debug by printing row
        #avg_change iterate after appending to list, ?
        big_change.append(row)

        #max of new_list_Change, also need MMM-YYYY
        max_mon.append(int(row[1]))

        #min of new_list_Change, also need MMM-YYYY
        min_mon.append(int(row[1]))
        #min_mon= min(int(row[1]))
#save information in new csv_file
        #zipped= zip(mon_total, avg_change, max_mon, min_mon)
        output_file= os.path.join("PyBank.csv")
        #big_change is a long list of rows combined.
        # [][] grabs the latter element in the former index

        #append this change answer to new_list_Change ?
        #then do operation of average(new_list_Change) ?
    for idx, value in enumerate(big_change):
        #delta=big_change[1][1]-big_change[0][1]
        print(idx, value)
        delta= big_change[idx+1][1]-big_change[idx][1]
    #print(big_change)
    #another way
    #for i in len(big_change):
    #    delta= big_change[i][1] - big_change[i-1][1]
    mons_total= len(mon_total)
    dol_total= sum(dol_total)
# reassign max_mon according to prompt and new_list_Change
    max_mon= max(max_mon)
    print(mons_total)
#write new results to text file
with open(output_file, "w", newline='') as processed:
    writer= csv.writer(processed)
    writer.writerow("Month_Total","Average_Change","Greatest_Increase","Greatest_Decrease")
    writer.writerows(zipped)


#final print statement
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {mons_total}")
print(f"Total: {dol_total}")
#print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {max_mon}")
print(f"Greatest Decrease in Profits {min_mon}")
