# -*- coding: utf-8 -*-
# Example main.py
import argparse
import urllib.request
import tempfile
import PyPDF2
import sqlite3

#import project0

def main(url):
    # Download data
    incident_data = fetchincidents(url)

    # Extract data
    incidents = extractincidents(incident_data)
	
    # Create new database
    db = createdb()
	
    # Insert data
    populatedb(db, incidents)
	
    # Print incident counts
    status(db)

def fetchincidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    
    return data

def createdb():
    
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE if not exists incidents (
                incident_time TEXT,
                incident_number TEXT,
                incident_location TEXT,
                nature TEXT,
                incident_ori TEXT
)   ''')
    con.commit()
    con.close()
    return 'normanpd.db'

def extractincidents(incident_data):
    fp = tempfile.TemporaryFile()
    fp.write(incident_data)
    fp.seek(0)
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    no_of_pages =  pdfReader.getNumPages()
    combined_data = []
    for i in range(no_of_pages):
        pagei = pdfReader.getPage(i).extractText()
        data = pagei.replace(" \n"," ").split("\n")
        row_wise = [tuple(data[x:x+5]) for x in range(0, len(data), 5)]
        clean_data = [d for d in row_wise if len(d) == 5]
        combined_data.extend(clean_data)
    return combined_data

def populatedb(db,incidents):
    con = sqlite3.connect(db)
    cur = con.cursor()
    stmt = """ INSERT INTO incidents (incident_time,incident_number,incident_location,nature,incident_ori) VALUES (?,?,?,?,?)"""
    cur.executemany(stmt,incidents)
    con.commit()
    con.close()
    
def status(db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    stmt = """ select Nature ,count(Nature)from incidents group by Nature order by Nature """
    cur.execute(stmt)
    result = cur.fetchall()
    for row in result:
        print(row[0].strip(),"|",row[-1])
    cur.execute("drop table incidents")
    cur.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
