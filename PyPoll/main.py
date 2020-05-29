import os
import csv

print("Election Results")
print("-----------------------")

def print_votes(votes_data):
    print(f"Total Votes: {votes_data}")

def count_votes(list_of_all_votes, cand_name):
    count = 0
    for vote in list_of_all_votes:
        if(vote == cand_name):
            count += 1
    return count

def print_winner(election_winner):
    print(f"Winner: {election_winner}")

election_csv = os.path.join('election_data.csv')
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    count_of_votes = 0
 
    cand_list = []
    list_of_all_votes =[]
    
    for row in csvreader:
        count_of_votes += 1
        list_of_all_votes.append(row[2])
        
        cand_name = row[2]

        if cand_name not in cand_list:
            cand_list.append(cand_name)
    
    vote_dict = {}
    for cand_name in cand_list:
        votes_per_cand = count_votes(list_of_all_votes, cand_name)
        votes_perc = (votes_per_cand/count_of_votes)
        formatted_perc = format(votes_perc, ".2%")
        vote_dict[cand_name] = ((formatted_perc), (votes_per_cand))
        keymax = max(vote_dict, key=vote_dict.get)

    print_votes(count_of_votes)
    print("-----------------------")
    print(str(vote_dict))
    print("-----------------------")
    print_winner(keymax)
    print("-----------------------")

file_to_output = os.path.join("..", "PyPoll" "Election_Analysis.txt")

output = "Election_Analysis.txt"
with open(output, 'w') as textfile:
    textfile.write(str("Election Results"))
    textfile.write("\n")
    textfile.write(str("----------------"))
    textfile.write("\n")
    textfile.write(str("Total Votes: ") + str(count_of_votes))
    textfile.write("\n")
    textfile.write(str("----------------"))
    textfile.write("\n")
    textfile.write(str(vote_dict))
    textfile.write("\n")
    textfile.write(str("----------------"))
    textfile.write("\n")
    textfile.write(str("Winner: ") + str(keymax))
    textfile.write("\n")
    textfile.write(str("----------------"))
