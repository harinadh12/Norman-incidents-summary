# cs5293sp21-project0

Author : Harinadh Appidi

Running the project from command line :
Navigate to outside of project0 folder and run the below command.
pipenv run python project0/main.py --incidents <url>

for e.g. url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

It will then print the list of incident nature  and their frequency of occurence in the alphabetical order of the nature.

There are 6 functions in the main.py file
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

How I Solved:
As the problem is divided into 5 parts for solving namely fetching incidents, extract incidents from pdf, creating sqlite3 db & table, populating db and printing the summary of incidents, 5 functions are writtend for implementng each functionality.
main function calls  each function in order and main function is being called from command line to execute the proejct.

1. In fetchincidents() method, i have taken url and used urllib module to make a url request with given sample header and got the pdf file data in stream object format.
2. In extractincidents() method, I have written the file data into a temporary file and opened the file with PyPDF2 module to extract text from pdf. This is done in a for loop for all pages of pdf to extract data from all pages. " \n" is replaced with " " to handle overflowing cells into multiple rows.
Then the data is split on "\n" and taken to a list which is then split into sublists of length 5 (as number of columns is 5).I have removed sublists whose length is less than 5 in order to clean some junk data in the first(heading info) and last page(footer location) of the pdf. we get a list of tuples(rows) which is returned from this method.
3. In createdb() method a new db is created or overidden if its already created and a new 'incidents' table is created  everytime we run the project.
4. In populateddb() 'incidents' table created in above step is populated with list of rows we get from extractincidents() method above.
5. In status() function i have queried the db to get nature of incidents, count of nature of incidents and ordered in ascending order of nature which is then printed to standard out of the terminal.

Test Cases:
Every function is tested for 1 passing and 1 failing test case.
1. For findincidnets() function, 1 correct url and one incorrect url is passed to test the method.
2. For extractincidents() function, 1 correct url is passed to get incident data from findincidents() and then to test extracting incidents for successful test case and 1 incorrect url to findincidents() method for null data and then it is passed to extractincidents to tet for failed test case
3. For createdb() a dummy db is sent to test failed case and correct db is sent to test successful test case.
4. For populatedb() an incorrect db, None data is sent to test failed test case and correctdb, incidents rows are sent to test successful test case scenario.
5. for status() correct db is sent to test successful test case, dummy db is sent to test failed test case scenario.
 	
References :
https://stackoverflow.com/questions/37058984/insert-multiple-rows-into-db-with-python-list-of-tuples

