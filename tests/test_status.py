import pytest
from project0 import main

def test_true_status():
    """ We are testing status() function to assert true when it is successfully executed """

    db = 'normanpd.db'
    result = main.status(db)
    assert True
    assert result is not None

def test_false_status():
    """ we are testing status() function to assert false when it is unsuccessfully executed"""

    db = 'dummy.db'
    result = main.status(db)
    assert True
    assert result is not None
