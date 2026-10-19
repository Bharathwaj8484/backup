

import pandas as pd
import random

# Load the CSV file into a DataFrame
csv_file_path = "C:/Users/bhara/Downloads/output_file.csv"  # Replace with the path to your CSV file
data = pd.read_csv(csv_file_path)

# Define a function to generate random votes based on decision type
def generate_random_vote(decision_type):
    if decision_type == 'majority opinion':
        return random.randint(1, 30)
    elif decision_type == 'minority opinion':
        return random.randint(30, 70)
    elif decision_type == 'judge':
        return random.randint(70, 100)
    else:
        return None

# Update the 'majority_vote' column based on 'decision_type'
data['majority_vote'] = data.apply(lambda row: generate_random_vote(row['decision_type']), axis=1)

# Save the modified DataFrame back to a CSV file
output_csv_path = 'output_file1.csv'  # Replace with the desired output file path
data.to_csv(output_csv_path, index=False)

print("Column 'majority_vote' values changed based on 'decision_type' and data saved to", output_csv_path)
