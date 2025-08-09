import re
from app.utils.scraper import scrape_wiki_data
from app.utils.plot import plot_scatter
from app.utils.s3_handler import query_s3_data

def process_question(text: str):
    if "highest grossing films" in text:
        df = scrape_wiki_data()
        q1 = df[(df['Worldwide'] > 2_000_000_000) & (df['Year'] < 2020)].shape[0]
        q2 = df[df['Worldwide'] > 1_500_000_000].sort_values("Year").iloc[0]["Title"]
        corr = df["Rank"].corr(df["Peak"])
        img_uri = plot_scatter(df)
        return [q1, q2, round(corr, 6), img_uri]

    elif "Indian high court" in text:
        return query_s3_data()

    return {"error": "Unrecognized question format"}