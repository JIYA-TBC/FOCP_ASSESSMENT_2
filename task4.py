# imports sys
import sys
# imports csv
import csv

try:
    values = sys.argv[1] 
    print(values)
    print("==================\n")

#handles the IndexError 
except:
    pass

#list of nations
nation = ["England","France","Ireland","Italy","Scotland","Wales"]
with open("result.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    
    #creating some lists 
    win_team=[]
    loss_team=[]
    draw_team=[]
    against_goal=[]

    #reads the csv in rows
    for row in reader_variable:
        score1=int(row[1])
        score2=int(row[3])
        
        #checks if score1 is greater than score2
        if score1>score2:
            team1=row[0]
            team2=row[2] 

            win_team.append(team1)#appends the variables in given list win_team
            win_team.append(score1)#appends the variables in given list win_team
            loss_team.append(team2)#appends the variables in given list loss_team
            loss_team.append(score2)#appends the variables in given list loss_team

            against_goal.append(team1)#appends the variables in given list against_goal
            against_goal.append(score2)#appends the variables in given list against_goal
            against_goal.append(team2)#appends the variables in given list against_goal  
            against_goal.append(score1)#appends the variables in given list against_goal      

        #checks if score1 and score2 are same
        elif score1==score2: 
            team1=row[0]
            team2=row[2]
            draw_team.append(team1)
            draw_team.append(team2)
            
        else:
            team1=row[2]
            team2=row[0]

            win_team.append(team1)#appends the variables in given list win_team
            win_team.append(score2)#appends the variables in given list win_team
            loss_team.append(team2)#appends the variables in given list loss_team
            loss_team.append(score1)#appends the variables in given list loss_team

            against_goal.append(team1)#appends the variables in given list against_goal  
            against_goal.append(score1)#appends the variables in given list against_goal  
            against_goal.append(team2)#appends the variables in given list against_goal    
            against_goal.append(score2)#appends the variables in given list against_goal    

    #creates a list of dictionary in it
    against_lst=[]
    for i in range(0,len(against_goal),2):
        against_dict={against_goal[i]:against_goal[i+1]}
        against_lst.append(against_dict)
    #creates a dictionary and adds the value of same keys
    rslt = {}
    for d in against_lst:
        for k in d.keys():
            rslt[k] = rslt.get(k, 0) + d[k]
    
    all_team=win_team+loss_team
    
    #creates a list of dictionary in it
    new_lst=[]
    for i in range(0,len(all_team),2):
        rec_dict={all_team[i]:all_team[i+1]}
        new_lst.append(rec_dict)
    result = {}
    #creates a dictionary and adds the value of same keys
    for d in new_lst:
        for k in d.keys():
            result[k] = result.get(k, 0) + d[k]
  
#getting the scores of team france
team_france=nation[1]
france_p=all_team.count(team_france)#counts how many times the team played
france_w=win_team.count(team_france)#counts how many times the team won
france_d=draw_team.count(team_france)#counts how many times the team draw
france_l=loss_team.count(team_france)#counts how many times the team loss
france_F=result.get("France")#gets the score for the team
france_A=rslt.get("France")#gets the score against the team
france_diff=france_F-france_A#gets the difference in score
france_pts=3*france_w+1*france_d#calculates the total points

#getting the scores of team Wales
team_Wales=nation[-1]
Wales_p=all_team.count(team_Wales)#counts how many times the team played
Wales_w=win_team.count(team_Wales)#counts how many times the team won
Wales_d=draw_team.count(team_Wales)#counts how many times the team draw 
Wales_l=loss_team.count(team_Wales)#counts how many times the team loss
Wales_F=result.get("Wales")#gets the score for the team
Wales_A=rslt.get("Wales")#gets the score against the team
Wales_diff=Wales_F-Wales_A#gets the difference in score
Wales_pts=3*Wales_w+1*Wales_d#calculates the total points

#getting the scores of team Ireland
team_Ireland=nation[2]
Ireland_p=all_team.count(team_Ireland)#counts how many times the team played
Ireland_w=win_team.count(team_Ireland)#counts how many times the team won
Ireland_d=draw_team.count(team_Ireland)#counts how many times the team draw
Ireland_l=loss_team.count(team_Ireland)#counts how many times the team loss
Ireland_F=result.get("Ireland")#gets the score for the team
Ireland_A=rslt.get("Ireland")#gets the score against the team
Ireland_diff=Ireland_F-Ireland_A#gets the difference in score
Ireland_pts=3*Ireland_w+1*Ireland_d#calculates the total points

#getting the scores of team Scotland
team_Scotland=nation[-2]
Scotland_p=all_team.count(team_Scotland)#counts how many times the team played
Scotland_w=win_team.count(team_Scotland)#counts how many times the team won
Scotland_d=draw_team.count(team_Scotland)#counts how many times the team draw
Scotland_l=loss_team.count(team_Scotland)#counts how many times the team loss
Scotland_F=result.get("Scotland")#gets the score for the team
Scotland_A=rslt.get("Scotland")#gets the score against the team
Scotland_diff=Scotland_F-Scotland_A#gets the difference in score
Scotland_pts=3*Scotland_w+1*Scotland_d#calculates the total points

#getting the scores of team england
team_England =nation[0]
England_p=all_team.count(team_England)#counts how many times the team played
England_w=win_team.count(team_England)#counts how many times the team won
England_d=draw_team.count(team_England)#counts how many times the team draw
England_l=loss_team.count(team_England)#counts how many times the team loss
England_F=result.get("England")#gets the score for the team
England_A=rslt.get("England")#gets the score against the team
England_diff=England_F-England_A#gets the difference in score
England_pts=3*England_w+1*England_d#calculates the total points

#getting the scores of team italy
team_Italy =nation[3]
Italy_p=all_team.count(team_Italy)#counts how many times the team played
Italy_w=win_team.count(team_Italy)#counts how many times the team won
Italy_d=draw_team.count(team_Italy)#counts how many times the team draw
Italy_l=loss_team.count(team_Italy)#counts how many times the team loss
Italy_F=result.get("Italy")#gets the score for the team
Italy_A=rslt.get("Italy")#gets the score against the team
Italy_diff=Italy_F-Italy_A#gets the difference in score
Italy_pts=3*Italy_w+1*Italy_d#calculates the total points

#creating a class named team
class team():

    #redefining the previous class to include some initialisation of instance attributes
    def __init__(self,name,play,win,draw,loss,goal_for,against,diff,pts):
        self.name=name
        self.play=play
        self.win=win
        self.draw=draw
        self.loss=loss
        self.goal_for=goal_for
        self.against=against
        self.diff=diff
        self.pts=pts

    #display function 
    def display(self):    
        print("{:8s}".format(self.name),"{:d}".format(self.play),"{:d}".format(self.win),"{:d}".format(self.draw),"{:d}".format(self.loss),"{:3d}".format(self.goal_for),"{:3d}".format(self.against),"{:4d}".format(self.diff),"{:3d}".format(self.pts))

#passing the variables to the class 
com1=team(team_Wales,Wales_p,Wales_w,Wales_d,Wales_l,Wales_F,Wales_A,Wales_diff,Wales_pts)
com2=team(team_Ireland,Ireland_p,Ireland_w,Ireland_d,Ireland_l,Ireland_F,Ireland_A,Ireland_diff,Ireland_pts)
com3=team(team_Scotland,Scotland_p,Scotland_w,Scotland_d,Scotland_l,Scotland_F,Scotland_A,Scotland_diff,Scotland_pts)
com4=team(team_france,france_p,france_w,france_d,france_l,france_F,france_A,france_diff,france_pts)
com5=team(team_England,England_p,England_w,England_d,England_l,England_F,England_A,England_diff,England_pts)
com6=team(team_Italy,Italy_p,Italy_w,Italy_d,Italy_l,Italy_F,Italy_A,Italy_diff,Italy_pts)

#output header
print("\t","P","W","D","L"," F","  A"," Diff","Pts")

#calling the display function
com1.display()
com2.display()
com3.display()
com4.display()
com5.display()
com6.display()