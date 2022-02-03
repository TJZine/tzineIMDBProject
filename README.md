# tzineIMDBProject
Project 1 Sprint 1
1. Tristan Zine
2. Requirements.txt contains the packages needed to run the program. Specifically the requests module.
Also need to create file titled "secrets.py" with a variable inside named "api_key" with your own api key as value.
4. The project connects to the IMDb API, first to retrieve the list of the top 250 TV shows. 
Second to retrieve the 5 specific shows User ratings listed in the project specifications. 
It then writes the list of shows and user ratings to a text file, each with their own line.
4. The only thing missing from the project at the moment in working with pytest on github.
First I struggled figuring out how to correctly get pytest to use the requests module that is imported in main.py
After adding requirements.txt with that module, pytest stop finding my test file alltogether. 
I then tried to make a test folder, with an init.py file to get pytest to find the test to no avail. 
I believe my test file should be close to what I need but am not able to properly test through github.
