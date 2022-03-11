# tzineIMDBProject
Project 1 Sprint 4
1. Tristan Zine
2. Requirements.txt contains the packages needed to run the program. You also need to create a python file
titled "secrets.py" housing a variable titled "secret_key" with your imdb api key as the value.
3. The project connects to the IMDb API, first to retrieve the list of the top 250 TV shows and movies. 
Second to retrieve the 5 specific shows User ratings listed in the project specifications. Third, to retrieve
the most popular tv shows and movies. It then iterates through the RankUpDown key to find the 3 largest positive
changes and one biggest negative change. It then creates and puts these 4 movies in a table of their own.
There is also integration with flake8 and pytest. pytest has 4 tests, one that confirms the retrieval
of the top 250 shows,  the second testing the creation and adding of information to a database, the third
testing the function of the min_max method and the last testing DB table creation, foreign key usage, and the 
new table creation and insertion methods are all working. This information can all be displayed now using a very basic
GUI interface. This interface can display most pop shows/movies, as well as sort them by rank and rankUpDown. It also
cross-references between these tables and top 250 tables for movies/shows.
4. Also has the option to update the database, and display graphs corresponding to counts of most popular shows/movies
moving up or down based on the 'rankUpDown' column. 
5. The first 2 tables are filled with the information from the top 250 TV shows and movies, the 2nd containing
the 5 shows we retrieved user rating information for. The third set of 2 tables contain the most popular tv shows and
movies. These tables are the same as top 250 but also include 'rank' and 'rankUpDown' columns. There is also a table 
created to house the movies from the min_max function. The first set of tables has the following columns 
(the id (primary key), the title, the full title, the year, crew, imdb rating, imdbrating count). The second has
columns for id, total rating, total rating votes and each rating 1-10 with both percentage of the total votes and 
vote count for each rating.
6. I don't believe there is anything missing from the project at the moment. Detailed testing plan is in a word document
that should also be uploaded to GitHub alongside the normal project files. 