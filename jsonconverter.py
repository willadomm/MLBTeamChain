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
                                    print(player)
                                    explored.append(player)
                                    incomingqueue.append(player)
                  



players_dictionary = dict()
directory = "json data"



for file in os.scandir(directory):
      with open (file.path) as file:
            data = json.load(file)


      for team in data:
            for player in team["players"]:
                  if player not in players_dictionary.keys():
                        players_dictionary[player] = [[team["team"], team["players"]]]
                
                
                  else:
                        players_dictionary[player].append([team["team"], team["players"]])
          



breathfirstsearch("Landen Roupp", "Babe Ruth", players_dictionary)
#score = determinedgameloop("Tyler Rogers", "Trevor Rogers", players_dictionary)

#print("You won!")
#print("Score: " + str(score))