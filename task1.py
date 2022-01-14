print("\nStop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.\n")

Name=["ARTHUR","Arthur","arthur"]
Answer_1=input("What is your name? : ") # takes input
if Answer_1 in Name: #checks if input is in list(Name) or not
    print("My liege! You may pass!")
else:
    Answer_2=input("What is your quest? : ")
    if "grail" in Answer_2: # checks if input is in ans_list or not
        Answer_3=input("What is your favourite colour? : ")
        if Answer_1[0]==Answer_3[0]: #checks if first letter of Answer_1 is same as the first letter of Answer_3
            print("\nYou may pass!")
        else:
            print("\nIncorrect! You must now face the Gorge of Eternal Peril.")        
    else:
        print("\nOnly those who seek the Grail may pass.\nIncorrect! You must now face the Gorge of Eternal Peril.")