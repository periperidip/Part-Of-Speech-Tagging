# Week 2: Create a dictionary having entry for every unique word_tag
# combo and its frequency in the corpus. Store it in a CSV file
# The CSV format is 'word_tag,count'
dict = {}
input_file = open("../output/week-1.txt", "r")
word_tag_list = input_file.read().splitlines()

for word_tag in word_tag_list:
	if (word_tag.find(',') != -1):
        	word_tag = '"' + word_tag + '"'
	if word_tag in dict:
		dict[word_tag] += 1
	else:
		dict[word_tag] = 1

output_file = open("../output/week-2.csv", "w")
for key in dict.keys():
	output_file.write("%s,%s\n" % (key, dict[key]))
