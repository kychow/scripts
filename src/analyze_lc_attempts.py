'''
Script to analyze your LC submisison history

How to use this script: 
1. Go to your leetcode submission history: https://leetcode.com/submissions/#/1 \ 
(it should look like this: https://imgur.com/a/Ln8GuTs).
2. Scrape your submission history into a CSV file and name it `lc_arguments.py`.
3. Run this script on the command line: 
```
python3 analyze_lc_attempts.py
```

The script should run successfully if you see this output: 
```
kychow@mac scripts % python3 analyze_lc_attempts.py 
Processing complete. The output CSV is at: lc_attempts_analysis.csv
```
4. Navigate to `lc_attempts_analysis.csv` and ensure data looks correct. 
5. Import into a google spreadsheet as a template to start practicing! 
'''

import argparse
from datetime import datetime 
from dateutil.relativedelta import relativedelta
import pandas as pd


# Constants
DEFAULT_INPUT_CSV_PATH = 'example_lc_attempts.csv'
DEFAULT_OUTPUT_CSV_PATH = 'example_lc_attempts_analysis.csv'


def relative_time_to_date(relative_time):
    '''
    Converts relative times ("2 weeks, 3 days ago") to dates (11/3/23)
    '''
    time_strs = relative_time[:-4].split(', ') # ["2 weeks", "3 days"]
    rd_kwargs = {}
    for num, unit in map(str.split, time_strs): 
        if int(num) == 1: # relativedelta uses plural keys
            unit += 's'
        rd_kwargs[unit] = int(num)
    time = datetime.now() - relativedelta(**rd_kwargs)
    return time.date()


def process_leetcode_csv(input_csv_path, output_csv_path):
    # 1. Read the input CSV into a DataFrame
    df = pd.read_csv(input_csv_path, header=None)
    df.columns = ["Time Attempted", "Problem Name", "Status", "Runtime", "Language"]

    # 2. Convert dates
    df['Time Attempted'] = df['Time Attempted'].apply(relative_time_to_date)

    # 3. Process DataFrame by problem
    output = []
    for problem in df['Problem Name'].unique():
        problem_df = df[df['Problem Name'] == problem]
        status = "Accepted" if any(problem_df['Status'] == "Accepted") else "Not Accepted"
        first_attempt = problem_df['Time Attempted'].min()
        solved_date = problem_df[problem_df['Status'] == "Accepted"]['Time Attempted'].min() if status == "Accepted" else None
        num_attempts = problem_df.shape[0]
        output.append([problem, status, first_attempt, solved_date, num_attempts])

    # 4. Convert output to a dataframe
    output_df = pd.DataFrame(output, columns=["Problem Name", "Status", "First Attempted", "Solved Date", "Number of Attempts"])

    # 5. Write dataframe to a CSV
    # 5.1 convert dates to strings
    output_df['First Attempted'] = output_df['First Attempted'].astype(str)
    output_df['Solved Date'] = output_df['Solved Date'].fillna("Not Solved").astype(str)
    output_df.to_csv(output_csv_path, index=False)

    return output_df


def main(input_csv_path=DEFAULT_INPUT_CSV_PATH, output_csv_path=DEFAULT_OUTPUT_CSV_PATH): 
    process_leetcode_csv(input_csv_path, output_csv_path)
    print("Processing complete. The output CSV is at:", output_csv_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a CSV file containing LeetCode problem attempts.')
    parser.add_argument('input_csv_path', nargs='?', default=DEFAULT_INPUT_CSV_PATH,
                        help='The input CSV file path. Default is defined by DEFAULT_INPUT_CSV_PATH.')
    parser.add_argument('output_csv_path', nargs='?', default=DEFAULT_OUTPUT_CSV_PATH,
                        help='The output CSV file path. Default is defined by DEFAULT_OUTPUT_CSV_PATH.')

    args = parser.parse_args()

    main(args.input_csv_path, args.output_csv_path)