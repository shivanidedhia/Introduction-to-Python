##The Springfork Amateur Golf Club has a tournament every weekend. The club
##president has asked you to write a program that will read each player's name
##and score as keyboard input, and then save these as records in a file named
##golf.txt.

##First, have the program ask the user how many players they want to add to their
##record. Then, ask the user for each name and score individually.

##golf.txt should be structured so that there is a line with the player's name,
##folowed by their score on the next line.


num_players = int(input("Enter number of players:"))

outfile = open("golf.txt",'w')

for i in range(num_players):
	name = input("Enter name of player number "+str(i+1)+":")
	score = input("Enter score of player number "+str(i+1)+":")
	outfile.write(name)
	outfile.write('\n')
	outfile.write(score)
	outfile.write('\n')

outfile.close()
