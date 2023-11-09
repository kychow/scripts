# Scripts 

Backup for useful scripts 

# 1. Leetcode Submission History Analysis
Leetcode script to analyze your submission history and identify challenging 
(most attempted) and previously unsolved problems. This is a good starting point 
when going through an interview loop to identify problems or concepts to brush up on.

This script takes all attempts you have ever submitted for a Leetcode problem and \
tabulates the following on a per-problem basis: number of attempts made, \  
submission status (`Accepted` or `Not Accepted`), the first date the problem was \ 
attempted, and the date the problem was solved, if it has been. 

This should be useful for identifying challenging problems and following up on \
problems that have previously been attempted but not solved. 

# How to use this script: 
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