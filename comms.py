import os
from random import randint
from datetime import datetime, timedelta

start_date = datetime(2022, 1, 1)  # Start date
end_date = datetime.now()  # End date

# Calculate the number of days between start_date and end_date
total_days = (end_date - start_date).days

# Loop through each day starting from start_date
for i in reversed(range(total_days)):
    commit_count = randint(1, 10)  # Random number of commits per day
    date = start_date + timedelta(days=i)  # Calculate the date

    # Construct the commit message
    commit_message = f"commit {commit_count} days ago"

    # Append the commit message to the file
    with open('file.txt', 'a') as file:
        file.write(commit_message + '\n')

    # Add and commit changes
    os.system('git add .')
    os.system(f'git commit --date "{date.strftime("%Y-%m-%d %H:%M:%S")}" -m "{commit_message}"')

# Push changes to remote repository
os.system('git push -u origin main')
