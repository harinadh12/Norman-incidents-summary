# cs5293sp21-project0

Author : Harinadh Appidi
References :
https://stackoverflow.com/questions/37058984/insert-multiple-rows-into-db-with-python-list-of-tuples

Running the project from command line :
Navigate to outside of project0 folder and run the below command.
pipenv run python project0/main.py --incidents <url>

for e.g. url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

It will then print the list of incident nature  and their frequency of occurence in the alphabetical order of the nature.

There are 4 functions in the main.py file
1. main() function - This function calls all the other fucntions and executes the flow of the project. It takes url as input.

2. fetchincidents() - This function takes url as input and returns data from the url location in byte stream format to the main function.

3. extractincidents() - This function takes incident data returned from fetchincidents() function above and returns the incidents data as list of tuples.
In this function, stream data is written to a temporary file and that file is opened with PyPDF2 package to extracted text data from incident pdf. Incident data is then cleaned up to organize it into a list of rows (tuples). This function returns list of rows as list of tuple i.e., each tuple corresponds to each incident row.

4. createdb() - This function doesn't take any input. It only creates the .db file in sqlite3 and a new incidents table is inserted. Here normanpd.db file is being created. This function returns the db file.

5. populatedb() - This function takes db file and incidents data as input and inserts them in the incidents table created in the above function.
It returns None.

6. status() - This function takes db file location as input and prints the summary of incidents i.e., Nature of the incident and its frequency of occurence on that particular day across Norman.

Possible Bugs:
1. As splitting the data and reformatting into list of rows has been done based on '\n' if any cell is empty then there is a chance of misalignment and rows could get inserted incorrrectly.
