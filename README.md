# tzineIMDBProject
Project 1 Sprint 2
1. Tristan Zine
2. Requirements.txt contains the packages needed to run the program. Specifically requests,
sqlite3, sys, and from typing import Tuple. You also need to create a python file
titled "secrets.py" housing a variable titled "secret_key" with your imdb api key as the value.
3. The project connects to the IMDb API, first to retrieve the list of the top 250 TV shows. 
Second to retrieve the 5 specific shows User ratings listed in the project specifications. 
It then creates a database with 2 tables, 1 for each of the queried information from sprint 1.
There is also integration with flake8 and pytest. pytest has 2 tests, one that confirms the retrieval
of the top 250 shows, and the second testing the creation and adding of information to a database.
4. The first table is filled with the information from the top 250 TV shows, the 2nd containing
the 5 shows we retrieved user rating information for. The first table has the following columns
(the id (primary key), the title, the full title, the year, crew, imdb rating, imdbrating count).
The second has columns for id, total rating, total rating votes and each rating 1-10 with both 
percentage of the total votes and vote
count for each rating.
5. I don't believe there is anything missing from the project at the moment.