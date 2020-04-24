import os
import csv

pollcsv = os.path.join("Resources", "election_data.csv")

with open(pollcsv, newline="") as pollFile:
    csvreader = csv.reader(pollFile, delimiter=",")

    totalvotes = 0
    candidatelist = []
    totalInVote = []

    next(csvreader)
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] in candidatelist:
            # Should Add candidates to list for reading later, as well as gathering their individual votes
            totalInVote[candidatelist.index(row[2])] = totalInVote[candidatelist.index(row[2])]+1
        else:
            candidatelist.append(row[2])
            totalInVote.append(1)
    # print(candidatelist)
    # print(totalvotes)
    # print(totalInVote)
    # votepercent = totalInVote.count("Li")
    # print(totalvotes)

    winner  = totalInVote.index(max(totalInVote))
    # print(candidatelist["Khan"])
    # print(round(totalInVote.count("Khan")/totalvotes * 100, 3))

    file = open("output.txt", "w")
    file.write("Election Results \n")
    file.write("------------------------------------ \n")
    file.write(f"Total Votes: {sum(totalInVote)} \n")
    file.write("------------------------------------ \n")
    for x in candidatelist:
        nameid = candidatelist.index(x)
        votepercent = round(totalInVote[nameid]/totalvotes * 100, 3)
        file.write(f"{candidatelist[nameid]}: {votepercent}% ({totalInVote[nameid]}) \n")
        # file.write(candidatelist[name] + " : " + str(votepercent) + "% : (" + str(totalInVote[name]+ ")\n"))
    file.write("------------------------------------ \n")
    file.write(f"{candidatelist[winner]} has won the election \n")
    file.write("------------------------------------ \n")
    file.close()

    #Final Message delivered    
    file = open("output.txt", "r")  

    print (file.read())
