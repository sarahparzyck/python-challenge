import os
import csv

print("Election Results")
print("-----------------------")

def print_votes(votes_data):
    print(f"Total Votes: {votes_data}")

election_csv = os.path.join('..', 'Resources', 'election_data.csv')
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    count_of_votes = 0

    for row in csvreader:
        count_of_votes += 1

    print_votes(count_of_votes)

