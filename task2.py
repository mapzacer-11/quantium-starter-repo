import pandas as pd
import glob

# Step 1: Get all CSV files in data folder
files = glob.glob("data/*.csv")

dataframes = []

# Step 2: Read and process each file
for file in files:
    df = pd.read_csv(file)
    
    # Keep only Pink Morsels
    df["product"] = df["product"].str.strip()
    df = df[df["product"].str.lower() == "pink morsel"]

    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
    df["quantity"] = df["quantity"].astype(float)
    
    # Create sales column
    df["sales"] = df["quantity"] * df["price"]
    
    # Keep required columns only
    df = df[["sales", "date", "region"]]
    
    dataframes.append(df)

# Step 3: Combine all files
final_df = pd.concat(dataframes, ignore_index=True)

# Step 4: Save output
final_df.to_csv("output.csv", index=False)

print("Task completed! output.csv created.")