import os
import csv
# import election_data.csv as csv
election_data= os.path.join("Resources", "election_data.csv")
#assign empty lists to be reassigned later
total_votes= []
khan_list= []
correy_list= []
li_list = []
otooley_list= []

percentage= []

#data has 3 columns: Voter ID, County, Candidate
#open csv file, encoding as UTF-8.
with open(election_data, newline='', encoding= "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    data_header = next(csv_file)
#cycle through rows, candidate voted for is in final column
    for row in csv_reader:
        total_votes.append(int(row[0]))
        if row[2] == "Khan":
            khan_list.append(int(row[0]))
        elif row[2] == "Correy":
            correy_list.append(int(row[0]))
        elif row[2] == "O'Tooley":
            otooley_list.append(int(row[0]))
        else :
            li_list.append(int(row[0]))

    #TOTAL_VOTES is a constant, determined by the length of the voter list
    TOTAL_VOTES= len(total_votes)
    #KHAN_TOTAL is a constant, determined by the length of the voter list
    KHAN_TOTAL= len(khan_list)
    #calculate percentage of popular vote
    khan_per= (float(KHAN_TOTAL)/float(TOTAL_VOTES))*100
    #CORREY_TOTAL is a constant, determined by the length of the voter list
    CORREY_TOTAL= len(correy_list)
    #calculate percentage of popular vote
    correy_per= (float(CORREY_TOTAL)/float(TOTAL_VOTES))*100
    #LI_TOTAL is a constant, determined by the length of the voter list
    LI_TOTAL= len(li_list)
    #calculate percentage of popular vote
    li_per= (float(LI_TOTAL)/float(TOTAL_VOTES))*100
    #OTOOLEY_TOTAL is a constant, determined by the length of the voter list
    OTOOLEY_TOTAL= len(otooley_list)
    #calculate percentage of popular vote
    otooley_per= (float(OTOOLEY_TOTAL)/float(TOTAL_VOTES))*100
    #define candidate dictionary with list of candidates and their respective
    #percentage of the popular vote
    summary= {"Candidates": ["Khan", "Correy", "Li", "O'Tooley"],
    "Percentages": [khan_per, correy_per, li_per, otooley_per]}
    for i in range(4):
        if (summary["Percentages"][i]) > 50:
            winner=summary["Candidates"][i]

output_file= os.path.join("PyPoll.txt")
#write new results to text file
with open(output_file, "w", newline='') as processed:
    print("Election Results ", file=processed)
    print("----------------------------------", file= processed)
    print(f"Total Votes: {TOTAL_VOTES}", file= processed)
    print("----------------------------------", file= processed)
    print(f"Khan:{khan_per:.3f}% {KHAN_TOTAL}", file= processed)
    print(f"Correy: {correy_per:.3f}% ({CORREY_TOTAL})", file= processed)
    print(f"Li: {li_per:.3f}% ({LI_TOTAL})", file= processed)
    print(f"O' Tooley: {otooley_per:.3f}% ({OTOOLEY_TOTAL})", file= processed)
    print("----------------------------------", file=processed)
    print(f"Winner: {winner}",file=processed)
    print("----------------------------------",file=processed)

#final print statement to terminal
print("Election Results ")
print("----------------------------------")
print(f"Total Votes: {TOTAL_VOTES}")
print("----------------------------------")
print(f"Khan:{khan_per:.3f}% ({KHAN_TOTAL})")
print(f"Correy: {correy_per:.3f}% ({CORREY_TOTAL})")
print(f"Li: {li_per:.3f}% ({LI_TOTAL})")
print(f"O' Tooley: {otooley_per:.3f}% ({OTOOLEY_TOTAL})")
print("----------------------------------")
print(f"Winner: {winner}")
print("----------------------------------")
