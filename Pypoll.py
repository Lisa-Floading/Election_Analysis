# The data we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete lists of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate 
# 5. The winner of the election based on popular vote. 

#Add our dependencies 
import csv
import os

# Assign a variable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to save a file to a path.  
file_to_save = os.path.join("analysis", "election_analysis.txt")


#Initialize a total vote counter
total_votes = 0

#Candidate options and candidate votes
candidate_options = []
#1 . Declare the empty dictionary. 
candidate_votes = {}

#Track the winning candidate, vote count, and percentage
winning_candidate = ""
Winning_count = 0
winning_percentage = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
 
    #Print each row in the CSV file. 
    for row in file_reader: 
        # 2. Add to the total vote count. 
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any others
        if candidate_name not in candidate_options:

        #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        
         #Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1
        #Determine the percentage of votes for each candidate by looping through the counts. 
        #Iterate through the candidate list
        for candidate_name in candidate_votes:
                #Retrieve vote count of a candidate. 
                votes = candidate_votes[candidate_name]
                #Calculate the percentage of votes. 
                vote_percentage = float(votes) / float(total_votes) * 100
                # Print the candidate name and percentage of votes. 
                print(f"{candidate_name}: received {vote_percentage}% of the vote.")


    
    #Print the candidate vote dictionary 
    print(candidate_votes)
