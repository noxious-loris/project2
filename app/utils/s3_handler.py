import duckdb

def query_s3_data():
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs;")
    con.execute("INSTALL parquet; LOAD parquet;")

    query = """
    SELECT court, COUNT(*) as total
    FROM read_parquet('s3://indian-high-court-judgments/metadata/parquet/year=*/court=*/bench=*/metadata.parquet?s3_region=ap-south-1')
    WHERE year BETWEEN 2019 AND 2022
    GROUP BY court ORDER BY total DESC LIMIT 1
    """
    result = con.execute(query).fetchall()
    return {
        "Which high court disposed the most cases from 2019 - 2022?": result[0][0],
        "What's the regression slope of the date_of_registration - decision_date by year in the court=33_10?": "...",
        "Plot the year and # of days of delay...": "data:image/webp;base64,..."
    }