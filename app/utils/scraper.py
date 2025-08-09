import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_wiki_data():
    url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    table = soup.find_all("table", {"class": "wikitable"})[0]
    df = pd.read_html(str(table))[0]
    df.columns = [col.strip() for col in df.columns]
    df = df.rename(columns={"Worldwide gross (millions)": "Worldwide"})
    df["Worldwide"] = df["Worldwide"].replace('[\$,]', '', regex=True).astype(float) * 1e6
    df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
    df["Rank"] = df.index + 1
    df["Peak"] = df["Rank"]  # Use same as Rank temporarily
    df["Title"] = df[df.columns[1]]  # Title column
    return df