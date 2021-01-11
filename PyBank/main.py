import os
import csv
from statistics import mean
# import budget_data.csv as csv
budget_data= os.path.join("Resources", "budget_data.csv")
#assign empty lists to be reassigned later
mon_total = []
max_mon= []
min_mon= []
dol_total= []
big_change= []
delta_list= []
#open csv file, encoding as UTF-8. 2 columns of data: Date and Profit/Losses
#Date format is MMM-YYYY
#Profit/Losses format is a postive or negative integer sum for the Month
with open(budget_data, newline='', encoding= "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    data_header = next(csv_file)
    #check data_header to look for format
    #print(f"{data_header}")
#cycle through rows
    for row in csv_reader:
        #print(row)
        mon_total.append(row[0])
        dol_total.append(int(row[1]))
        #debug by printing row
        #AVG_CHANGE calculate after finding individual changes
        #append change answer to big_change
        big_change.append(row)

        #max of new_list_Change, also need MMM-YYYY
        max_mon.append(int(row[1]))

        #min of new_list_Change, also need MMM-YYYY
        min_mon.append(int(row[1]))

        #big_change is a long list of rows combined.
        # [][] grabs the latter element in the former index
        #then do operation of average(big_change) ?
    #print(big_change)
    for idx, value in enumerate(big_change):
        #delta=big_change[1][1]-big_change[0][1]
        #print(idx, value)
        if idx == 85:
            break
        delta= int(big_change[idx+1][1])-int(big_change[idx][1])
        delta_list.append(delta)
#calculate average of delta_list
#round to 2 decimal places for cents
AVG_CHANGE= round(mean(delta_list),2)
#print(AVG_CHANGE)
    #print(delta)
    #another way
    #for i in len(big_change):
    #    delta= big_change[i][1] - big_change[i-1][1]
    # number of rows to get MONS_TOTAL
MONS_TOTAL= len(mon_total)
dol_total= sum(dol_total)
#print(dol_total)
# max_mon needs to be in format Greatest_Increase MMM-YYYY (value)
# find index at max(delta)??
max_mon_val= max(delta_list)
max_mon_ind=delta_list.index(max_mon_val)

#print(max_mon_val)
greatest_increase=mon_total[max_mon_ind+1]
#print(greatest_increase)
min_mon= min(delta_list)
min_mon_ind= delta_list.index(min_mon)
greatest_decrease= mon_total[min_mon_ind+1]
#print(min_mon)
#print(greatest_decrease)
#min_mon also need MMM-YYYY
#print(MONS_TOTAL)
#save information in new text file
#zipped= zip(MONS_TOTAL, dol_total, AVG_CHANGE, greatest_decrease, max_mon_val,
# greatest_decrease, min_mon)
output_file= os.path.join("PyBank.txt")
#write new results to text file
#method obtained from Stack Overflow
#https://stackoverflow.com/questions/5214578/print-string-to-text-file
with open(output_file, "w", newline='') as processed:
    print("Financial Analysis", file=processed)
    print("----------------------------------------", file= processed)
    print(f"Total Months: {MONS_TOTAL}", file= processed)
    print(f"Total: {dol_total}", file= processed)
    print(f"Average Change: ${AVG_CHANGE}", file= processed)
    print(f"Greatest Increase in Profits: {greatest_increase}({max_mon_val})", file= processed)
    print(f"Greatest Decrease in Profits {greatest_decrease}({min_mon})", file= processed)
    #writer= csv.writer(processed)
    #writer.writerow("Month_Total","Average_Change","Greatest_Increase","Greatest_Decrease")
    #writer.writerows(zipped)


#final print statement
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {MONS_TOTAL}")
print(f"Total: {dol_total}")
print(f"Average Change: ${AVG_CHANGE}")
print(f"Greatest Increase in Profits: {greatest_increase}({max_mon_val})")
print(f"Greatest Decrease in Profits {greatest_decrease}({min_mon})")
