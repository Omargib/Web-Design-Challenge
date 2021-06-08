import pandas as pd
import numpy as np

cities_path = "Resources/cities.csv"

cities_data = pd.read_csv(cities_path)

cities_df = pd.DataFrame(cities_data)

print(cities_df.to_html("Data.html",index=False))
