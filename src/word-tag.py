# Week 1: Preprocess the corpus into the required format
# The format is: word_tag
# 'word' is obtained from param 'hw' of 'w'
# 'tag' is obtained from param 'c5' of 'w'
# Store the output in a TXT file.
import os
import xml.etree.ElementTree as ET

output_path = "../output/week-1.txt"
output_f = open(output_path, "w")

for subdir, dir, file in os.walk(r'../Assignment-files/Train-corups'):
	for file_name in file:
		file_path = subdir + os.sep + file_name
		tree = ET.parse(file_path)
		root = tree.getroot()

		# Handle fields with single word and tag(s)
		# For instance,
		# <w c5="NN1" hw="theory" pos="SUBST">Theory </w>
		# becomes 'theory_NN1'
		# In case a word has multiple tags, add
		# 'word_tag1' and 'word_tag2' into the TXT file
		# These are retrieved from the 'w' tag
		for element in root.iter('w'):
			word = element.text
			tag = element.attrib.get('c5')
			tag_list = tag.split('-')
			for tags in tag_list:
				word_tag = word.rstrip() + "_" + tags + "\n"
				output_f.write(word_tag)

		# Handle fields with mutliple words and tag(s)
		# For instance,
		# <mw c5="AV0">
		# 	<w c5="PRF" hw="of" pos="PREP">of </w>
		# 	<w c5="NN1" hw="course" pos="PREP">course </w>
		# </mw>
		# becomes 'of_PRF', 'course_NN1' and 'ofcourse_AV0'
		# These are retrieved from the 'mw' tag
		for element in root.iter('mw'):
			word = element.text
			mw_list = ""
			for words in element.iter('w'):
				mw_list +=  words.text
			tag = element.attrib.get('c5')
			word_tag = mw_list.rstrip() + "_" + tag + "\n"
			output_f.write(word_tag)

		# Handle fields with punctuations
		# For instance,
		# <c c5="PUN">, </c>
		# becomes ',_PUN'
		# These are retrieved from the 'c' tag
		for element in root.iter('c'):
			word = element.text.rstrip()
			tag = element.attrib.get('c5')
			word_tag = word.rstrip() + "_" + tag + "\n"
			output_f.write(word_tag)
