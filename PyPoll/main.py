import os
import csv

election_data_csv = os.path.join("Resources","election_data.csv")

total_votes = 0
candidates = {}
winner_votes = 0
winner = ""

with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:

        total_votes = total_votes + 1
        candidate = row[2]
        
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes)* 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes 

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_path = os.path.join("Analysis", "Analysis.txt")

with open(output_path, 'w') as txtfile:
   
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes)* 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")