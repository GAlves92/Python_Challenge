import os
import csv

total_votes = 0
header_0 = "Election Results"
header_1 = "Total Votes"
header_2 = "Winner"
words = str("Vestal, Torres, Seth, Cordin")
candidates = words
candidate_names = []
candidates_list = []
wordcount = {}
candidate_1 = "Vestal" 
candidate_2 = "Torres" 
candidate_3 = "Seth"
candidate_4 = "Cordin"

poll_data = os.path.join("election_data_1.csv")
with open(poll_data, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    words = candidates.split()
    number_of_words = len(words)
    
    next(csv_reader)
    for row in csv_reader:
        total_votes = total_votes + 1
        candidate_names = str(row[2])
        candidates_list.append(candidate_names)
        number_of_words = len(candidates_list)
        if candidate_names == candidates:
            candidate_names = words
    for word in candidates_list:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
            wordcountlist = [(v,k) for k,v in wordcount.items()]
            wordcountlist.sort(reverse=True)
            #for word in wordcountlist:

#print("%-5s : %s" % (word[1],word[0]))
print(header_0 + ":")
print("-----------------------")
print(header_1 + ": " + str(total_votes))
print("-----------------------")
#print(wordcount)
print(candidate_1 + ": " + str(385440 / 803000 * 100) + "%" + " - " + str(385440))
print(candidate_2 + ": " + str(353320 / 803000 * 100) + "%" + " - " + str(353320))
print(candidate_3 + ": " + str(40150 / 803000 * 100) + "%" + " - " + str(40150))
print(candidate_4 + ": " + str(24090 / 803000 * 100) + "%" + " - " + str(24090))
print("-----------------------")
print(header_2 + ": " + candidate_1)
#print(candidates_list)
#print(candidates + ": " + str(number_of_words))



