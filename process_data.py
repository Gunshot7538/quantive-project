import pandas as pd
import os

# Step 1: data folder path
data_folder = "data"

# Step 2: saare CSV files read karo
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

dataframes = []

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Step 3: combine all data
combined_df = pd.concat(dataframes, ignore_index=True)

# Step 4: check product names
print("Products:", combined_df["product"].unique())

# Step 5: filter Pink Morsel
pink_df = combined_df[combined_df["product"] == "pink morsel"]

# Step 6: remove $ sign from price and convert to float
pink_df["price"] = pink_df["price"].replace("[$]", "", regex=True).astype(float)

# Step 7: create sales column
pink_df["sales"] = pink_df["quantity"] * pink_df["price"]

# Step 8: select required columns
final_df = pink_df[["sales", "date", "region"]]

# Step 9: rename columns
final_df = final_df.rename(columns={
    "sales": "Sales",
    "date": "Date",
    "region": "Region"
})

# Step 10: save output
final_df.to_csv("formatted_output.csv", index=False)

print("✅ Task 2 Done! File created: formatted_output.csv")