#main script to run for each analysis
#The total number of votes cast
#a complete list of candidates who recieved votes
#the percentage of votes each candidates
#the total number of votes each candidate won
#the winner of the election based on popular vote

import csv
import os 
import sys

vote_count = 0
k_candidate = 0
c_candidate = 0
l_candidate = 0
o_candidate = 0

candidates_list = []

csvpath = os.path.join('Resources/election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        vote_count += 1
        if row[2] in candidates_list:
            candidates_list.append(row[2])
        if row[2] == "Khan":
            k_candidate += 1
        if row[2] == "Correy":
            c_candidate += 1
        if row[2] == "Li":
            l_candidate += 1
        if row[2] == "O'Tooley":
            o_candidate += 1
    

    
    print("Election Results")
    print('------------------------')
    print(f'Total Votes: {vote_count}')
    print('------------------------')
    print(f'Khan: {round((k_candidate/vote_count)*100)}% ({k_candidate})')
    print(f'Correy: {round((c_candidate/vote_count)*100)}% ({c_candidate})')
    print(f'Li: {round((l_candidate/vote_count)*100)}% ({l_candidate})')
    print(f"O'Tooley: {round((o_candidate/vote_count)*100)}% ({o_candidate})")
    print('------------------------')

    if k_candidate > c_candidate and k_candidate > l_candidate and k_candidate > o_candidate:
        print('Winner: Kahn')
    elif c_candidate > k_candidate and c_candidate > l_candidate and c_candidate > o_candidate:
        print('Winner: Correy')
    elif l_candidate > k_candidate and l_candidate > c_candidate and l_candidate > o_candidate:
        print('Winner: Li')
    elif o_candidate > k_candidate and o_candidate > c_candidate and o_candidate > l_candidate:
        print("Winner: O'Tooley")
    print('------------------------')

    stdoutOrigin=sys.stdout 
txtPath = os.path.join("Analysis/election_analysis.txt")
sys.stdout = open(txtPath, "w")

    
    
    