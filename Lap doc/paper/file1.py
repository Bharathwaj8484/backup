import pandas as pd

# Load the modified CSV file
modified_file_path = "C:/Users/bhara/Downloads/modified_csv_file.csv"
df_modified = pd.read_csv(modified_file_path)

# Update "decision_type" column based on row numbers divisible by both 2 and 3
for row_number, row in df_modified.iterrows():
    if (row_number + 1) % 2 == 0 and (row_number + 1) % 3 == 0:
        df_modified.at[row_number, 'decision_type'] = "minority opinion"

# Save the updated DataFrame back to the CSV file
updated_file_path = "C:/Users/bhara/Downloads/updated_csv_file.csv"
df_modified.to_csv(updated_file_path, index=False)

print(f"Updated 'decision_type' column based on condition and saved to {updated_file_path}.")
