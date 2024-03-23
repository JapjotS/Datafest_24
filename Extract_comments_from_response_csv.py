import pandas as pd
from tqdm import tqdm


#CHANGE ME

# Correct the filepath based on your directory structure
filepath = 'C:\\Users\\Japjot\\Downloads\\OneDrive_1_3-22-2024\\full_03_04\\responses.csv'

# Load the data into a DataFrame, adding low_memory=False to avoid DtypeWarning
df = pd.read_csv(filepath, low_memory=False)

# Define a function to safely extract comments
def extract_comments(x):
    # Check if x is a string to avoid AttributeError
    if isinstance(x, str):
        # Split by '#' and strip spaces
        return ' '.join([part.strip() for part in x.split('#') if part.strip()])
    else:
        # Return an empty string or placeholder if x is not a string
        return ''

# Apply the function to the 'response' column
comments = df['response'].apply(extract_comments)

# Open a text file for writing comments
with open('comments.txt', 'w', encoding='utf-8') as file:
    # Iterate over comments with a progress bar
    for i, comment in tqdm(enumerate(comments, start=1), total=comments.shape[0], desc="Writing comments"):
        file.write(f"Comment {i}: {comment}\n\n")
