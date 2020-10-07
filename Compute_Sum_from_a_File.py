

#Assume that a file containing a series of integers is named numbers.txt. Write
#a program that calculates the average of all the numbers stored in the file.



avg_nums = open('numbers.txt','r')

total = 0

numberoflines = 0
line = avg_nums.readline()

while line !="":
	numberoflines +=1
	total +=int(line)
	line = avg_nums.readline()

average = total/numberoflines

print(average)
