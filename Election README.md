**1. Overview of Election Audit**

The purpose of analyzing the election data is to find out the voter turnout for each county, the percentage of votes from each county out of the total count and to find which county had the highest voter turnout.
Compiling this information will allow for current and future candidates as well as the government to see which county's underperformed and which one's excelled in terms of voter turnout. From there they will be able to investigate as to why certain county's outperformed others and be able to adjust their strategy for future elections.

**2. Election-Audit Results:**
The following information can all be found in the file: election_analysis.txt
- There were 369,711 votes casted in this election.
County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

-Denver had the largest number of votes amongst the county's with 306,055
-This is the breakdown of the candidates results:
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

**3. Election Audit Summary**s
This code is perfect for summarizing the overall results for any election that you may hold. You can easily refactor the code to read the raw data from other elections. This code is also not constrained to read a specific number of candidates, rows, or counties. Since the code loops through and automatically accounts for all of the different candidate names and county names. The code also allows you to easily draw conclusions from the raw data as it summarized in a txt. file.
Example 1:
This code can be used to summarize the results from a city or town's mayoral election. It can summarize the candidate data as well as the riding data from the elections. Additionally, the government will be able to tell which areas had strong voter turnout and which areas did not. This will allow you to address the issue of voter turnout for future elections (IE: adjust polling stations, adjust information availability, etc.). In this scenario there could be many candidates and many ridings, but this can be easily summarized by this code. The areas that will need to be refactored would be lines 49 and line 52 which is where you get the candidate name and the county name from the spreadsheet (see image ElectionCode). 

Example 2:
You can refactor this code to collect the results for a city council election. The code can be used on each of the wards to determine the winner as well as the total number of votes for each of the municipalities.
