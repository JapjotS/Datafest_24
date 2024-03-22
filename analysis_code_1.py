import pandas as pd

def read_and_analyze_csv(filepath):
    """
    Reads a CSV file containing teaching stats and prints out some basic analysis.
    
    :param filepath: Path to the CSV file.
    """
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(filepath)
    
    # Basic data cleaning: dropping any rows with missing values for simplicity
    data.dropna(inplace=True)
    
    # Analysis 1: Average EOC score per book
    avg_eoc_per_book = data.groupby('book')['EOC'].mean()
    
    # Analysis 2: Average number of attempts per chapter
    avg_attempts_per_chapter = data.groupby('chapter_number')['n_attempt'].mean()
    
    # Analysis 3: Overall average of correct vs possible answers
    overall_avg_correct = data['n_correct'].mean()
    overall_avg_possible = data['n_possible'].mean()
    
    # Printing out the results
    print("Average EOC Score per Book:")
    print(avg_eoc_per_book)
    print("\nAverage Number of Attempts per Chapter:")
    print(avg_attempts_per_chapter)
    print("\nOverall Average of Correct vs Possible Answers:")
    print(f"Correct: {overall_avg_correct}, Possible: {overall_avg_possible}")

# Example usage
if __name__ == "__main__":
    # Replace 'your_file_path.csv' with the path to your actual CSV file
    # Correct the filepath based on the actual location of your CSV file
    filepath    = 'Random Sample of Data Files_03_04/checkpoints_eoc.csv'

    read_and_analyze_csv(filepath)
