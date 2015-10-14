#Python Problem 2
#hamming.py
#Introduction to Bioinformatics Assignment 2
#Purpose:Calculate Hamming Distance
#Your Name: Michael Thomas
#Date: 10/10/15

#stores 3 database sequences
seqList = ["AGGATACAGCGGCTTCTGCGCGACAAATAAGAGCTCCTTGTAAAGCGCCAAAAAAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGGCCCCGGGAGCGGAGAGCGAGGGGAGGCAGATTCGGAGGAAGGTCTGAAAAG",
           "AAAATACAGGGGGTTCTGCGCGACTTATGGGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCACAGACTATGGCAGCAGCGTTGGCCCGGCAAAAGGAGCGGAGAGCGAGGGGAGGCGGAGACGGACGAAGGTCTGAGCAG",
           "CCCATACAGCCGCTCCTCCGCGACTTATAAGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGCCCAAAACAGCGGAGAGCGAGGGGAGGCGGAGACGGAGGAAGGTCTGAGCAG"]
#your query sequence
s1 = "AGGATACAGCGGCTTCTGCGCGACTTATAAGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGGCCCCGGGAGCGGAGAGCGAGGGGAGGCGGAGACGGAGGAAGGTCTGAGGAG"
count=[0,0,0]
#outer loop to go through seqList[]
for i in range(len(seqList)):
	#save each string to iterate trough on secondary loop
	seqi = seqList[i]
	#checks for non-matches between s1 and seqi and iterates count
	for j in range(len(s1)):
		if s1[j] != seqi[j]:
			count[i] = count[i] + 1
#Results 
#hamming distance for each sequence
print "The Hamming distance dh(s1,seqList[0]) =", count[0]
print "The Hamming distance dh(s1,seqList[1]) = ", count[1]
print "The Hamming distance dh(s1,seqList[2]) = ", count[2]
