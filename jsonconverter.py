import json




def checkifteammates(originplayer, potentialteammate, dictionary):
      returnlist = []
      for teamlist in dictionary[originplayer]:
            if potentialteammate in teamlist[1]:
                  returnlist.append(teamlist[0])
    

      if len(returnlist) == 0:
            return False
      
      else:
            return returnlist

    
    
players_dictionary = dict()


with open ("json data/NYA.json") as file:
        data = json.load(file)

for team in data:
    for player in team["players"]:
          if player not in players_dictionary.keys():
                players_dictionary[player] = [[team["team"], team["players"]]]
                
          else:
                players_dictionary[player].append([team["team"], team["players"]])
          


print(checkifteammates("Mickey Mantle", "Yogi Berra", players_dictionary))