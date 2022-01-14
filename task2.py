readings_list = [] #creating a list

def split(reading): 
    '''takes in string and split string into characters'''
    return [char for char in reading]
       
try:
    print("\nSwallow Speed Analysis: Version 1.0\n")
        
    while True: #iterate while true
        reading = input("Enter the Next Reading: ") #takes input
        split_reading=split(reading)

        if reading=="" and len(readings_list)!=0: #checks if there is not input and the list is not empty
            print("\nResults Summary\n")
            break
        else:
            total = str('') #gives string version of the input

        for num in range(1, len(split_reading)):
            total = total + split_reading[num]
        a_string = str(reading[0])#assigns the value in one
        number=float(total)#assigns the value in two
        print("Reading saved.")

        if "U" in reading: #checks if U in reading
            y=number
        elif "E" in reading:#checks if E in reading
            y=number/1.61
        else:
            print("INVALID INPUT")
        readings_list.append(y) #append the value in list 

    print(len(readings_list),"Reading Analysed.\n" if len(readings_list)==1 else "Readings Analysed.\n") #checks and prints if readings_list has only one value 

    all_sum=0
    #iterate over the length of reading_list
    for i in range(0, len(readings_list)):
        all_sum = all_sum + readings_list[i]
        avg=all_sum/len(readings_list)

    #sorts the list in ascending order    
    readings_list.sort()

    #printing the results
    print("\nMax Speed:",'%0.1f' %(readings_list[-1]),"MPH,",'%0.1f' %((readings_list[-1])*1.61),"KPH.")
    print("Min Speed:",'%0.1f' %(readings_list[0]),"MPH,",'%0.1f' %((readings_list[0])*1.61),"KPH.")
    print("Avg Speed:",'%0.1f' %avg,"MPH,",'%0.1f' %(avg*1.61),"KPH.")

# handle IndexError exception
except IndexError :
    print("No readings entered. Nothing to do.")

# handle ValueError exception
except:
    print("Sorry!, Invalid Input.")