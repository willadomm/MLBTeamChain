
import json
import time
import requests
from bs4 import BeautifulSoup


"""
Problems.

1. Some pages don't have team shutouts text. Will have to rescrape all



teamidentifiers = ["LAA", "CAL", "BSN", "NY1", "BRO", "BLN", "MLN", "FLO", "MON", "SEA", "ARI", "ATL", "CHN", 
                   "CIN", "COL", "LAN", "SDN", "MIA", "MIL", "NYN", "PHI", "PIT", "SFN", "SLN", "WAS"
                   ###"PHA", "WS1", "SLA", "KC1", "SE1", ###"WS2", "BAL", "BOS", "CHA", "CLE", "DET", "HOU"
                   ###"KCA", "MIN", "NYA", "OAK", "TBA", "TEX", "TOR", "ATH"]
"""
teamidentifiers = ["PHA", "WS1", "SLA", "KC1", "SE1"]

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

        
        
        roster = soup.find_all('a')

        roster = roster[52:]


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
                    date = tdarray[1]
                    playername = playername + " "
                    for char in str(date):
                        if char.isnumeric():
                            playername = playername + char



                
                
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