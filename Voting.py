candidates = ["bob smith", "pete fring", "lois jane"] #each candidate starts with one vote

def CastVote(candidateName): #Method CastVote takes the vote from user; lowers the case; and appends to list
    candidateName = candidateName.lower() #Lowers case of user inputted candidateName
    candidates.append(candidateName) #Appends/adds to list
def DisplayResults(): #Method DisplayResults prints out everyone's votes by counting what is in the list
    candidate1 = candidates.count("bob smith") #Bob Smith is counted in list
    print("Bob Smith: "+ str(candidate1)) #Print out Bob Smith votes by converting candidate1 to string instead of integer
    candidate2 = candidates.count("pete fring") #Pete Fring is counted in list
    print("Pete Fring: "+str(candidate2)) #Print out Pete Fring votes by converting candidate2 to string instead of integer
    candidate3 = candidates.count("lois jane") #Lois Jane is counted in list
    print("Lois Jane: "+str(candidate3)) #Print out Lois Jane votes by converting candidate3 to string instead of integer
def ResetVotes(): #Method ResetVotes clears out list and appends names back in list
    candidates.clear() #Clears all elements in list
    candidates.append("bob smith") #Append candidates back into list; since each start with one
    candidates.append("pete fring") #Append candidates back into list; since each start with one
    candidates.append("lois jane") #Append candidates back into list; since each start with one


# Main Program
print("Voting Simulator") #Title of Program
print() #Space for better visibility
print("Press 1 to cast vote, press 2 to see results, press 3 to reset votes.") #Output options to user
print("To exit program, press 4.") #Seperate line to exit program for better visibility
selection = int(input("Select choice: ")) #Prompts and takes user input and stores in selection variable (changes to integer variable for better comparison)
print() #Space for better visibility

while (selection != 4): #While loop; switch-case structure; takes selection variable and goes to designated nested if-elseif statements
    if selection == 1: 
        print("Bob Smith") #Print out candidate names
        print("Pete Fring") #Print out candidate names
        print("Lois Jane") #Print out candidate names
        vote = input("Vote with candidate's name: ") #Prompt and takes user input and stores in vote variable
        CastVote(vote) #Calls CastVote method which lowers user input and appends to candidates list
    elif selection == 2: 
        DisplayResults() #Calls DispalyResults method which prints out results from candidate list by counting how many of votes for each in list
    elif selection == 3:
        ResetVotes() #Calls ResetVotes method which clears the list and appends back the candidates names to candidates list
    elif selection == 4:
        break #Exit variable called and ends program
    else:
        print("Invalid selection; please try again.") #Serves as a buffer to ensure a correct selection is made
    print() #Space for better visibility
    print("Press 1 to cast vote, press 2 to see results, press 3 to reset votes.") #Output options to user again for while loop to check
    print("To exit program, press 4.") #Seperate line to exit program for better visibility
    selection = int(input("Select choice: ")) #Prompts and takes user input and stores in selection variable (changes to integer variable for better comparison)
    print() #Space for better visibility
print("Program Completed.") #When program is terminated it will output this statement to signify end of program