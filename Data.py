import pandas as pd

# Load CSV version of MPCORB (you may need to preprocess raw MPCORB.DAT to CSV)
data = pd.read_csv("MPCORB.csv")

# Keep only necessary columns
asteroids = data[['a','e','i','node','peri','M']]