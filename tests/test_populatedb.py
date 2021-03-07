import pytest
from project0 import main

def test_false_populatedb():
    """ we are testing populatedb() function to assert false when it is unsuccessfully executed"""
    
    db = None
    result = main.populatedb(db,None)
    assert True
    assert result is not None

def test_true_extractdb():
    """ we are testing populatedb() function to assert true when it is successfully executed"""

    db = 'normanpd.db'
    url = r"https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-02_daily_incident_summary.pdf"
    incident_data = main.fetchincidents(url)
    incidents = main.extractincidents(incident_data)

    result = main.populatedb(db,incidents)
    assert True
    assert result is True

