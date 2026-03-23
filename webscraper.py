import re
import json
import time
import requests
from bs4 import BeautifulSoup




"""
teamidentifiers = ["BRO", "BLN", "MLN", "FLO", "MON", "HOU", "ARI", "ATL", "CHN", 
                   "CIN", "COL", "LAN", "SDN", "MIA", "MIL", "NYN", "PHI", "PIT", "SFN", "SLN", "WAS"
                   "PHA", "WS1", "SLA", "KC1", "SE1", "WS2", "BAL", "BOS", "CHA", "CLE", "DET", "HOU"
                   "KCA", "MIN", "NYA", "OAK", "TBA", "TEX", "TOR", "ATH"]
"""

teamidentifiers = ["NY1"]

invalidyears = []
abbreviatednames = []
datalist = []
for team in teamidentifiers:

    

    for year in range(1900, 1960):
        print(year)
        url = f"https://www.retrosheet.org/boxesetc/{year}/U{team}0{year}.htm"
        try:
            page = requests.get(url)
        except:
            invalidyears.append(year)
            continue

        time.sleep(1)

        soup = BeautifulSoup(page.text, 'html.parser')
    


        roster = soup.find_all('a')

        roster = roster[52:]


        playersarray = []

        for pre in roster:
            firstnamelastnamearray = pre.get_text().split()
        

            playername = ""

            

            if len(firstnamelastnamearray) > 1:
                for name in firstnamelastnamearray:
                    playername = playername + str(name + " ")
                
                if "." in playername:
                    stringurl = str(pre.get("href"))
                    stringurl = stringurl[2:]
                    newlink = "https://www.retrosheet.org/boxesetc"+stringurl
                    playerpage = requests.get(newlink)
                    playersoup = BeautifulSoup(playerpage.text, 'html.parser')
                    name = playersoup.find('h2')
                    playername = name.get_text()
                
                
                
                playersarray.append(playername)

            


        playersarray = list(set(playersarray))

        playersarray.sort()


        if "Read Me" in playersarray:
            playersarray.remove("Read Me")
    
        if "Read Me " in playersarray:
            playersarray.remove("Read Me ")


        data = {
                "team": f"{team} {year}",
                "players": playersarray
        }
        
        if len(playersarray) > 0:
            datalist.append(data)


filestring = f"{team}.json"

with open ("json data/" + filestring, "w") as file:
    json.dump(datalist, file, indent=2)

   


    
    






