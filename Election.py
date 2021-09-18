import csv
import os
file_to_load = os.path.join("ResourcesTwo", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize the vote counter
total_votes = 0

# Declare a new list
candidate_options = []

# Empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    # Read the file objext with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match an existing candidate name...
        if candidate_name not in candidate_options:
            # Add the candidate name to the cnadidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
        # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        Votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
        vote_percentage = float(Votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({Votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # 1. Determine if the votes are greater than the winning count.
        if (Votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = Votes
            # 3. Set the winning_candidate = to the candidate's name.
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's results
    txt_file.write(winning_candidate_summary)