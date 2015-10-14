#Python Problem 3
#mode.py
#Introduction to Bioinformatics Assignment 2
#Purpose:Calculating the mode of a dataset
#Your Name: Michael Thomas
#Date: 10/12/15

#will contain all the data of a list including some unwanted carriage return symbols
tempList = []
#will contain the data as floats after it is stripped and the header is removed
myData = []
#will store the header
header = ""
#this will store the value of the mode
mode = 0

#TASK1
#We have the file data.txt read all the values of this file in the list tempList
#open data.txt and save to a tempList
text_file = open('data.txt' , 'r')
tempList = text_file.readlines()
text_file.close()
print tempList

#TASK2
#We don't want the header to be in the list Pop it and save it into the header variable
#pop out header (position 0 in list tempList) and save to header.
header = tempList.pop(0).strip()

print header

#TASK3
#for every member of tempList, clean it up from carriage return, convert it into a float and add it to the list myData
#Using list comprehension, we delete all '\r\n' from each line in tempList
myData = [line.rstrip('\r\n') for line in tempList]
#Simialr to the list comprehension above, we convert all items to floats
myData = [float(i) for i in myData] 
print myData
#print type(myData[1])

#TASK4
#Sort the list myData
myData.sort()
print myData

#TASK5
#using the list of floats myData Find the MODE of the data
#The mode of a dataset is the number that occurs most frequently.
#i.e. in the list [2,2,3,3,3,4] the mode is 3
#create dictionary myDic
myDic = {}

#using exceptions, we can incriment the key if a repeat
#value is found, except if the value is unique
#this will create a counter that will contain
#len(myData) keys and their corresponding values
#that each key repeats in myData
for i in myData:
	try:
		myDic[i] += 1
	except:
		myDic[i] = 1
print myDic
#calculate the maximum values in the dictionary
#this will represent the value of the mode
maxval =  max(myDic.values())
#for loop to print the key for the 
#corresponding value of maxval which will
#be the mode for the dataset
for key, value  in myDic.items():
	if value == maxval:
		mode = key
#print results
print "\n"
print "The mode of the:", header, " dataset is: ", mode
print "\n"
