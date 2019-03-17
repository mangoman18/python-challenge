###############################################################
# PyPoll Assignment
# Date 3/11/2019
# Sanjay Mamidi
# Data Viz Class
# Description :
# This program runs at O(n). One pass thru to collect the list  and then apply the set
# operation to get distinct list. Then vote counts for the distinct list of candidates
# are done calling the list.count("candidatename") and that is inserted into
# a "candidate ,vote" list.
# This program is able to handle a generic list of candidates
# In other words the candidate list is not needed to be known before hand
# and can be potentially any number of candidates..
#################################################################

import os
import csv


listOfVoteRecords = []
candidateVotes = []  # Candidates and Votes tuple
totNumberOfVotes = 0
candidateSet = []  # Distinct set of Candidates
i = 0
maxVotes= 0
maxCandidate = ""

# path = 'c/Users/rekhapc/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instruction/PyPoll/Resources'
csvpath = os.path.join(os.pathsep, 'c:\\', 'users', 'rekhapc', 'Desktop', 'UCDSAC201902DATA4', '03-Python', 'Homework', \
                       'Instruction', 'PyPoll', 'Resources', 'election_data.csv')
fileToWrite = os.path.join(os.pathsep, 'c:\\', 'users', 'rekhapc', 'Desktop', 'UCDSAC201902DATA4', '03-Python', \
                           'python-challenge', 'PyPoll', 'PyPollout.txt')

file = open(fileToWrite, "w")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', )
    next(csvreader)
    for row in csvreader:
        listOfVoteRecords.append(row[2])
        # Incrementing the total vote count at this time
        totNumberOfVotes +=1
# Using the set function to create list of unique candidates
    candidateSet = list(set(listOfVoteRecords))
    candidateSet.sort()

#     Heart of the Program
#     This statement inserts count of distinct (unique) candidates vote
#     counts by candidate name into list of tuples called candidateVotes.
for candidates in range(len(candidateSet)):
    candidateVotes.insert(candidates,(candidateSet[candidates],listOfVoteRecords.count(candidateSet[candidates])))


print(f'Election Results')
print(f'----------------------------')
print(f'Total Votes: {totNumberOfVotes}')
for candidates in range(len(candidateSet)):
    print(f'{candidateSet[candidates]}: {round(100 * (candidateVotes[candidates][1]/totNumberOfVotes),3)}% ({candidateVotes[candidates][1]})')
print(f'----------------------------')
for candidates in range(len(candidateSet)):
    if candidateVotes[candidates][1] > maxVotes :
        maxVotes = candidateVotes[candidates][1]
        maxCandidate = candidateVotes[candidates][0]
print(f'Winner: {maxCandidate}')
print(f'----------------------------')

file.write(f'Election Results \n')
file.write(f'----------------------------\n')
file.write(f'Total Votes: {totNumberOfVotes}\n')
for candidates in range(len(candidateSet)):
    file.write(f'{candidateSet[candidates]}: {round(100 * (candidateVotes[candidates][1]/totNumberOfVotes),3)}% ({candidateVotes[candidates][1]})\n')
file.write(f'----------------------------\n')
for candidates in range(len(candidateSet)):
    if candidateVotes[candidates][1] > maxVotes :
        maxVotes = candidateVotes[candidates][1]
        maxCandidate = candidateVotes[candidates][0]
file.write(f'Winner: {maxCandidate}\n')
file.write(f'----------------------------')
file.close()