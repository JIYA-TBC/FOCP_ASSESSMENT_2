# imports random
import random

Names=["Jiya","Priya","Prince","Rashi","Tanya"]
print("\nWelcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")

def split(email):
    '''takes in string and split string into characters'''
    return [char for char in email]

email=input("Please enter your Poppleton email address: ")#takes input

if "@" in email:#checks if @ is in input
    a=email.split('@') #splits input(email) at @ into two parts
    first_part=a[0]
    name=first_part.capitalize()
    second_part=a[1]
    if len(first_part)>=2:# checks if the length of the first_part is 2 or more 
        if second_part=="pop.ac.uk":# checks if the second_part has pop.ac.uk
            print(f"Hi, {name}! Thank you, and Welcome to PopChat!")
        else:
            print("Invalid at pop.ac.uk.")
            exit()#exits the program if input is invalid
    else:
        print("Invalid at pop.ac.uk.")
        exit()#exits the program if input is invalid
else:
    print("Invalid at pop.ac.uk.")
    exit()#exits the program if input is invalid
    
print("My name is",random.choice(Names),", and it will be my pleasure to help you.")

#responses lists
end_lst=["bye","quit","goodbye","help","thanks","You should try working on this system.","ok"]
response=["Hhmmm","I see","Tell me more","Oh, my.","Yes.","That is interesting."]
library_response=["The library is close today.","The library is open till 5pm."]
wifi_response=["WiFi is excellent across the campus.","You can contact with IT depertment.","You must be in WiFi range for good network."]
deadline_response=["Your deadline has been extended by two working days.","Your deadline is 6 working days after the assignment is assigned."]
Coffee_response=["Teekee is open until 9pm this evening.","There is 15% OFF for students on Coffee."]
tea_response=["Chiya-Ghar is open for 24/7.","You can use your student's card to get discount on tea."]
Canteen_response=["Canteen is just opposite to IT department.","Canteen is open till 5pm."]
book_response=["You can get your syllabus books at library.","You can buy books from the college stationary to get discounts."]
admission_response=["You can consult with admission department.","Our students service department is open till 5pm."]

#iteratres according to inputs
while 1:
    que=input("--->")
    if "library" in que: #checks if library is in input
        print(random.choice(library_response))
    elif "wifi" in que: #checks if Wifi is in input
        print(random.choice(wifi_response))
    elif "deadline" in que: #checks if deadline is in input
        print(random.choice(deadline_response))
    elif "coffee" in que: #checks if coffee is in input
        print(random.choice(Coffee_response))
    elif "tea" in que: #checks if tea is in input
        print(random.choice(tea_response))
    elif "canteen" in que: #checks if canteen is in input
        print(random.choice(Canteen_response))
    elif "book" in que: #checks if book is in input
        print(random.choice(book_response))
    elif "admission" in que: #checks if admission is in input
        print(random.choice(admission_response))
    elif que in end_lst: #checks if que is in list (end_lst)
        print(f"\nThanks, {name}, for using PopChat. See you again soon!\n")
        break
    else:
        print(random.choice(response)) #prints random string from the list(respone)

    x=random.randint(1,10) #Prints a random number between 1 to 10
    if x == 10: #cheaks if x is 10
        print("*** NETWORK ERROR ***")
        print(f"\nThanks, {name}, for using PopChat. See you again soon!\n")
        break #breaks the program