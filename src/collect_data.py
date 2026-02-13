import pandas as pd

def collect_ads_data():
    # Read the CSV file into a DataFrame
    data = pd.read_csv("data/ads.csv")
    
    return data
