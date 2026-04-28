
import json
import time
import requests
from bs4 import BeautifulSoup



def tagfunction(tag):
    return len(tag.find_all('pre')) == 0 and ("Manager " in tag.text or "Manager: " in tag.text)

"""



teamidentifiers = [###"ANA", "LAA", "CAL", "BSN", "NY1", "BRO", "BLN", ###"MLN", "FLO", "MON", "SEA", "ARI", "ATL", "CHN", 
                   ###"CIN", "COL", "LAN", "SDN", "MIA", "MIL", ###"NYN", "PHI", "PIT", "SFN", "SLN", "WAS"
                ###"PHA", "WS1", "SLA", "KC1", "SE1", "WS2", "BAL", ###"BOS", "CHA", "CLE", "DET", "HOU"
                   ###"KCA", "MIN", "NYA", "OAK", "TBA", "TEX", "TOR", "ATH"]
"""
teamidentifiers = ["ANA", "LAA", "CAL", "BSN", "NY1", "BRO", "BLN"]

dupes = []
with open("dupes.txt", "r") as dupesfile:
    for line in dupesfile:
        dupes.append(line[:-1])
        



invalidyears = []

for team in teamidentifiers:
    datalist = []
    print(team)
    for year in range(1900, 2026):
        print(year)
        url = f"https://www.retrosheet.org/boxesetc/{year}/U{team}0{year}.htm"
        try:
            page = requests.get(url)
        except:
            invalidyears.append(year)
            continue

        time.sleep(1)

        soup = BeautifulSoup(page.text, 'html.parser')

        managertag = soup.find_all(tagfunction)

        if managertag == []:
            continue
        
        
        
        pretags = managertag[0].find_previous_siblings('pre')

        roster = []

        for tag in pretags:
            roster.extend(tag.find_all('a'))

        


        playersarray = []

        for a in roster:
            firstnamelastnamearray = a.get_text().split()

            playername = ""

            

            if len(firstnamelastnamearray) > 1:

                #MAybe move this code for more efficiency
                for name in firstnamelastnamearray:
                    playername = playername + str(name + " ")
                
                
                
                if "." in playername:
                    stringurl = str(a.get("href"))
                    stringurl = stringurl[2:]
                    newlink = "https://www.retrosheet.org/boxesetc"+stringurl
                    playerpage = requests.get(newlink)
                    playersoup = BeautifulSoup(playerpage.text, 'html.parser')
                    name = playersoup.find('h2')
                    playername = name.get_text()
                
                playername = playername.strip()
                
                
                if playername in dupes:
                    stringurl = str(a.get("href"))
                    stringurl = stringurl[2:]
                    newlink = "https://www.retrosheet.org/boxesetc"+stringurl
                    playerpage = requests.get(newlink)
                    playersoup = BeautifulSoup(playerpage.text, 'html.parser')
                    
                    tdarray = playersoup.find_all('td')
                    date = tdarray[1].text
                    playerbday = ""
                    playername = playername + " "
                    for char in date:
                        if char.isnumeric():
                            playerbday = playerbday + char
                    
                    playerbday = playerbday[-4:]
                    playername = playername + playerbday
                    
                    



                
                
                playersarray.append(playername)
                
                

            


        playersarray = list(set(playersarray))

        playersarray.sort()


        if "Read Me" in playersarray:
            playersarray.remove("Read Me")
    
        if "Team Page" in playersarray:
            playersarray.remove("Team Page")
        


        data = {
                "team": f"{team} {year}",
                "players": playersarray
        }
        
        if len(playersarray) > 0:
            datalist.append(data)


    filestring = f"{team}.json"

    with open ("json data only players/" + filestring, "w") as file:
        json.dump(datalist, file, indent=2)