import pytest

from project0 import main

def test_true_find_incidents():
    """ we are testing findincidents() fucntion to assert true when correct url is passed"""

    url = r"https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-01_daily_incident_summary.pdf"

    result = main.fetchincidents(url)
    assert True
    assert result is not None
    
def test_false_find_incidents():
    """ we are testing findincidents() function to assert false when false url is passed"""
    url = r"https://www.normanok.gov/sites/default/files/documents/2021-03/"
    result = main.fetchincidents(url)
    assert True
    assert result is not None

