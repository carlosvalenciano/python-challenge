import os
import csv

poll_file = os.path.join( "Resources", "election_data.csv")

# Read the election data from the csvfile
with open(poll_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)

    total_votes = 0
    
    # create empty dictionary to store the number of votes each candidate received

    candidates = {}

    for row in csvreader:
        candidate = row[2]
        total_votes += 1

        #.get is used to get value of a key from a dictionary this is ensures 
        # that we initialize the count to 0 if the candidate is not yet in the dictionary
        candidates[candidate] = candidates.get(candidate, 0) + 1

# Calculate the percantage of votes each candidate won

results = []

for candidate, votes in candidates.items():
    percentage = (votes /total_votes) * 100
    results.append((candidate, percentage,votes))

# FInd the winner of the election pased on popular vote
# lambda creates an inline function, and using max() will return the element in the array x[2] 

winner = max(results, key=lambda x: x[2])

# Printing out analysis to terminal
#\n breaks a new line

print( "Election Results")
print('\n')
print("--------------------------")
print('\n')
print(f"Total Votes: {total_votes}")
print('\n')
print("-----------------------------------")
print('\n')
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print('\n')
print("-------------------------------------------")
print('\n')
print(f"Winner: {winner[0]}")
print('\n')
print('--------------------------------------------')

# Write out to output file (txt file)

output_path = os.path.join("analysis", "Election_analysis.txt")

with open(output_path, 'w') as file:
    file.write("Election Analysis")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    for candidate, percentage, votes in results:
        file.write(f"{candidate}: {percentage:.3f}% ({votes}) " '\n' )
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f"Winner: {winner[0]}")
    file.write("\n")
 
