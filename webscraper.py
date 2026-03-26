
import json
import time
import requests
from bs4 import BeautifulSoup


"""



teamidentifiers = ["LAA", "CAL", "BSN", "NY1", "BRO", "BLN", "MLN", "MON", "ARI", "ATL", "CHN", 
                   "COL","SDN", "MIL", "NYN", "PHI", "PIT", "SLN", "WAS"
                   "PHA", "WS1", "KC1", "SE1", "WS2", "BAL", "BOS", "CHA", "CLE", "DET",
                   "KCA", "MIN", "NYA", "OAK"]
"""
teamidentifiers = []

dupes = []
with open("dupes.txt", "r") as dupesfile:
    for line in dupesfile:
        dupes.append(line[:-1] + " ")



invalidyears = []
abbreviatednames = []

for team in teamidentifiers:
    datalist = []
    print(team)
    for year in range(1950, 2026):
        print(year)
        url = f"https://www.retrosheet.org/boxesetc/{year}/U{team}0{year}.htm"
        try:
            page = requests.get(url)
        except:
            invalidyears.append(year)
            continue

        time.sleep(1)

        soup = BeautifulSoup(page.text, 'html.parser')
        
        name2tag = soup.find('pre', string="Team shutouts may be more than the composite totals for all pitchers due to instances in which more than one pitcher combined for a shutout.")

        if not name2tag:
            continue

        roster = []
        while True:
            name2tag = name2tag.find_next('a')
            if not name2tag:
                break
            roster.append(name2tag)



        

        

        
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
                
                
                if playername in dupes:
                    stringurl = str(a.get("href"))
                    stringurl = stringurl[2:]
                    newlink = "https://www.retrosheet.org/boxesetc"+stringurl
                    playerpage = requests.get(newlink)
                    playersoup = BeautifulSoup(playerpage.text, 'html.parser')
                    
                    tdarray = playersoup.find_all('td')
                    date = tdarray[1]
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