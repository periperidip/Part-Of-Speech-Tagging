# Week 3: Report the top 10 frequently used words and tags.
# Store it in a TXT file. The TXT format is '{word,tag} : frequency'.
from collections import Counter

word_dict = {}
tag_dict = {}

input_file = open("../output/week-1.txt", "r")
word_tag_list = input_file.read().splitlines()

for word_tag in word_tag_list:
	wt = word_tag.split('_')
	word = wt[0]
	if len(wt) > 1:
		tag = wt[1]
	if word in word_dict:
		word_dict[word] += 1
	else:
		word_dict[word] = 1
	if tag in tag_dict:
		tag_dict[tag] += 1
	else:
		tag_dict[tag] = 1

word_dict_count = Counter(word_dict)
tag_dict_count = Counter(tag_dict)

freq_words = word_dict_count.most_common(10)
freq_tags = tag_dict_count.most_common(10)

word_output = "Top 10 most frequent words are:\n"
tag_output = "Top 10 most frequent tags are:\n"

for word in freq_words:
	word_output += word[0] + " : " + str(word[1]) + '\n'

for tag in freq_tags:
	tag_output += tag[0] + " : " + str(tag[1]) + '\n'

output_file = open("../output/week-3.txt", "w")
output_file.write(word_output + "\n" + tag_output)
