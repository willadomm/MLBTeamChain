import re
import json
import time
import requests
from bs4 import BeautifulSoup


"""
Problems!
1. Intitals in the data set, probably manually needs fixing

"""

invalidyears = []
datalist = []
for year in range(2013, 2014):
    url = f"https://www.retrosheet.org/boxesetc/{year}/UANA0{year}.htm"
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
            playersarray.append(playername)


    playersarray = list(set(playersarray))

    playersarray.sort()

    
    if "Read Me" in playersarray:
        playersarray.remove("Read Me")


    data = {
            "team": f"ANA {year}",
            "players": playersarray
    }
    datalist.append(data)



with open ("data.json", "w") as file:
    json.dump(datalist, file, indent=2)

   


    
    






