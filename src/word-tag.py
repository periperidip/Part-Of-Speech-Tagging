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
		for element in root.iter('w'):
			word_tag = element.attrib.get('hw') + "_" + \
				   element.attrib.get('c5')
			output_f.write(word_tag + "\n")
