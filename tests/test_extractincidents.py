import pytest
from project0 import main

def test_true_extract_incidents():
    """ We are testing extractincidents() function to assert true when it is successfully executed """

    url = r"https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-02_daily_incident_summary.pdf"
    incident_data = main.fetchincidents(url)
    result = main.extractincidents(incident_data)
    assert True
    assert result is not None

def test_false_extract_incidents():
    """ we are testing extractincidents() function to assert false when it is unsuccessfully executed"""
    url = r"https://www.normanok.gov/sites/default/files/documents/2021-02/"
    incident_data = main.fetchincidents(url)
    result = main.extractincidents(incident_data)
    assert True
    assert result is not None

    
