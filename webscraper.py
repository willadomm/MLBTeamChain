import re
import json
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.retrosheet.org/boxesetc/2024/UANA02024.htm")

soup = BeautifulSoup(page.text, 'html.parser')


roster = soup.find_all('a')

roster = roster[52:]


playersarray = []

for pre in roster:
   firstnamelastnamearray = pre.get_text().split()
   

   if len(firstnamelastnamearray) > 1:
        playername = str(firstnamelastnamearray[0] + " " + firstnamelastnamearray[1] )
        playersarray.append(playername)


playersarray = list(set(playersarray))

playersarray.sort()
playersarray.remove("Read Me")
print(playersarray)

data = {
    "team": "ANA 2024",
    "players": playersarray
}

with open ("data.json", "w") as file:
    json.dump(data, file)

   


    
    






