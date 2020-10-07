##Ask user to enter a score.
##Start loop 
##Scores greater than or equal to 90 is an 'A'. 
##Scores between 80 and 89 is an 'B'. 
##Scores between 70 and 79 is an 'C'. 
##Scores between 60 and 69 is an 'D'. 
##Anything else is an 'F'. 
##Ask user to enter next score or -1 to quit.
##Display the total count for each grade.

score = int(input("Enter a score. Enter -1 to quit: "))
count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0

while score != -1:
    
    if score >= 90:
        count_A += 1
        score = int(input("Enter a score. Enter -1 to quit: "))
        
    elif score >= 80 and score <= 89:
        count_B += 1
        score = int(input("Enter a score. Enter -1 to quit: "))
           
    elif score >= 70 and score <= 79:
        count_C += 1
        score = int(input("Enter a score. Enter -1 to quit: "))
        
    elif score >= 60 and score <= 69:
        count_D += 1
        score = int(input("Enter a score. Enter -1 to quit: "))            
    else:
        count_F +=1
        score = int(input("Enter a score. Enter -1 to quit: "))
        
    
print ("A = " + str(count_A))
print ("B = " + str(count_B))
print ("C = " + str(count_C))
print ("D = " + str(count_D))
print ("F = " + str(count_F))
        
        
    
