
class adjmatrix:

    def __init__(self):
        self.playeriddict = dict()
        self.amountofplayers = 0
        self.matrix = [[]]
    
    def assignnumbertoeachplayer(self, listofplayers):
        counter = 1
        for player in listofplayers:
            if player not in self.playeriddict.keys():
                self.playeriddict[player] = counter
            
            counter = counter + 1
        
        self.amountofplayers = self.amountofplayers + counter










matrix = adjmatrix()

matrix.assignnumbertoeachplayer(["Fred Odwell",
      "Gabby Street",
      "Harry Steinfeldt",
      "Jack Harper 2187839237",
      "Jimmy Sebring",
      "Joe Kelley",
      "Johnny Siegle",
      "Mike Mowrey",
      "Miller Huggins",
      "Noodles Hahn",
      "Ollie Johns",
      "Orval Overall",
      "Rip Vowinkel",
      "Shad Barry",
      "Tom Walker 1188139510"])


for k,v in matrix.playeriddict.items():
    print(k,v)


    
    
