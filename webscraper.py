import webbrowser
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.baseball-almanac.com/teamstats/roster.php?y=2025&t=CLG")

soup = BeautifulSoup(page.text, 'html.parser')
