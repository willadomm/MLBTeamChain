import json
import os
import random
from collections import deque

def checkifteammates(originplayer, potentialteammate, dictionary):
      returnlist = []
      for teamlist in dictionary[originplayer]:
            if potentialteammate in teamlist[1]:
                  returnlist.append(teamlist[0])
    

      if len(returnlist) == 0:
            return False
      
      else:
            return returnlist

def randomgameloop(dictionary):
      originplayerstring = random.choice(list(dictionary.keys()))
      destinationplayerstring = random.choice(list(dictionary.keys()))

      while originplayerstring == destinationplayerstring:
            destinationplayerstring = random.choice(list(dictionary.keys()))
      
      print("Starting with " + originplayerstring + ", connect to " + destinationplayerstring)

      currentplayer = originplayerstring

      count = 0

      

      while checkifteammates(currentplayer, destinationplayerstring, dictionary) == False:
            inputplayer = input("Type teammate here: ")

            resultsofteammatecheck = checkifteammates(inputplayer, currentplayer, dictionary)

            if resultsofteammatecheck == False:
                  print(inputplayer + "was not teammates with " + currentplayer)
            
            else:
                  print("Yes! The teams " + inputplayer + " and " + currentplayer + " were on together were " + str(resultsofteammatecheck))
                  print("Now, connect " + inputplayer + " to " + destinationplayerstring)
                  currentplayer = inputplayer
            
            count += 1
      
      
      


def determinedgameloop(originplayer, destinationplayer, dictionary):
      originplayerstring = originplayer
      destinationplayerstring = destinationplayer
      
      print("Starting with " + originplayerstring + ", connect to " + destinationplayerstring)

      currentplayer = originplayerstring

      count = 0

      

      while checkifteammates(currentplayer, destinationplayerstring, dictionary) == False:
            inputplayer = input("Type teammate here: ")

            resultsofteammatecheck = checkifteammates(inputplayer, currentplayer, dictionary)

            if resultsofteammatecheck == False:
                  print(inputplayer + " was not teammates with " + currentplayer)
                  print("Try again. ")
            
            else:
                  print("Yes! The teams " + inputplayer + " and " + currentplayer + " were on together were " + str(resultsofteammatecheck))
                  print("Now, connect " + inputplayer + " to " + destinationplayerstring)
                  currentplayer = inputplayer
            
            count += 1
      
      print(checkifteammates(currentplayer, destinationplayer, dictionary))
      return count


def breathfirstsearch(originplayer, destinationplayer, dictionary):
      listofmutualteams = []
      for teamlistone in dictionary[originplayer]:
            for player in teamlistone[1]:
                  if player == destinationplayer:
                        listofmutualteams.append(teamlistone[0])
      
      if len(listofmutualteams) != 0:
            print("Players have been teammates on " + str(listofmutualteams))
            return
                        
      explored = [originplayer]
      queue = deque()
      incomingqueue = deque()
      depthcount = 0
      currentplayer = originplayer

      for teamlist in dictionary[currentplayer]:
            for player in teamlist[1]:
                  incomingqueue.append(player)
      
      
      
      while incomingqueue:
            queue.extend(incomingqueue)
            incomingqueue.clear()
            depthcount += 1
            while queue:
                  currentplayer = queue.popleft()
                  
                  print(currentplayer)
                  for teamlist in dictionary[currentplayer]:
                        for player in teamlist[1]:
                              if player == destinationplayer:
                                    print(depthcount)
                                    return 
                              elif player not in explored:
                                    explored.append(player)
                                    incomingqueue.append(player)



def breathfirstsearchfulllist(originplayer, destinationplayer, dictionary):
      listofmutualteams = []
      for teamlistone in dictionary[originplayer]:
            for player in teamlistone[1]:
                  if player == destinationplayer:
                        listofmutualteams.append(teamlistone[0])
      
      if len(listofmutualteams) != 0:
            print("Players have been teammates on " + str(listofmutualteams))
            return
                        
      explored = [originplayer]
      queue = deque()
      incomingqueue = deque()
      depthcount = 0
      currentplayerchain = originplayer

      for teamlist in dictionary[currentplayerchain]:
            for player in teamlist[1]:
                  incomingqueue.append([teamlist[0], player])
      
      
      
      while incomingqueue:
            queue.extend(incomingqueue)
            incomingqueue.clear()
            depthcount += 1
            while queue:
                  currentplayerchain = queue.popleft()
                  
                  print(currentplayerchain)
                  for teamlist in dictionary[currentplayerchain[-1]]:
                        for player in teamlist[1]:
                              newchain = currentplayerchain + [teamlist[0],player]
                              if player == destinationplayer:
                                    print(depthcount)
                                    print(player)
                                    print(originplayer, "-> ", currentplayerchain, " -> ", teamlist[0], " -> ", destinationplayer)
                                    return 
                              elif player not in explored:
                                    explored.append(player)
                                    incomingqueue.append(newchain)
      
      

      

                        
      
                  



players_dictionary = dict()
directory = "json data only players"



for file in os.scandir(directory):
      with open (file.path) as file:
            data = json.load(file)


      for team in data:
            for player in team["players"]:
                  if player not in players_dictionary.keys():
                        players_dictionary[player] = [[team["team"], team["players"]]]
                
                
                  else:
                        players_dictionary[player].append([team["team"], team["players"]])
          



breathfirstsearchfulllist("Carl Yastrzemski", "Mike Yastrzemski", players_dictionary)
#score = determinedgameloop("Tyler Rogers", "Trevor Rogers", players_dictionary)

#print("You won!")
#print("Score: " + str(score))