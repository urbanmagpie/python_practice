Google Analytics Mock Data Script
This is a simple Python program that simulates pulling data from Google Analytics. Since I don’t have access to the real Google Analytics API yet, I used mock data (which just means I made up some example numbers) to practice how it would work.

The program prints a summary of website traffic data and also saves it to a JSON file.

What This Is For
I made this project to learn how to:

Practice working with Python functions

Print nice summaries with real-world-like data

Save data in JSON format (which is a common way of working with APIs)

Understand how to structure a simple script like you would when working with data from an API
Why Even Do This?
In real life, people normally just open up Google Analytics and see their data.
This script shows how you could automate pulling and using GA data in your own projects — like sending automatic reports or using the data in other tools.
This version uses mock data because I don’t have GA API access yet, but the structure of the script is similar to what you would do with real data.

How It Works
The script contains fake Google Analytics data at the top.

It uses Python to:

Print a quick summary (total users, sessions, pageviews)

Print a daily breakdown

Save the data to a file called ga_data_mock.json

You can open and check that .json file to see how structured data looks like.
How To Use It
Install Python (if you don’t have it yet).

Copy the code into a Python file, for example: ga_mock_data.py

Run it using your terminal or editor (like Mu):

bash
Copy
Edit
python ga_mock_data.py
You’ll see the summary printed in your terminal and a file ga_data_mock.json will be created in your folder.
 This project is mainly for learning purposes to practice Python and working with data.
Later on, I want to connect it to the real Google Analytics API.
