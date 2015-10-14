#Python Problem 1
#reverseComplement.py
#Introduction to Bioinformatics Assignment 2
#Purpose: Reverse Compliment 
#Your Name: Michael Thomas
#Date: 10/10/15

#s1 is the string you should use to generate a reverse complement sequence
#Note that your result needs to be presented in the 5' to 3' direction

s1 = "AAAAACCCCCTCGGCTAATCGACTACTACTACTACTACTTCATCATCATCAGGGGGGGGCTCTCTCTAAAAACCCCTTTTGGGGG"
#Your Code Here
#empty list for rc of s1
rs1 = []
#create dictionary containing the character for s1
#and the cooresponding  key for rs
compdic = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
#iterate through s1 and replace 
#characters for their comps from dictionary compdic
for i in s1:
	rs1.append(compdic[i])

#print rs1 (list) as a string for rc of s1
print  ''.join(rs1[::-1])
