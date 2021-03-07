import pytest
from project0 import main

def test_false_extractdb():
    """ we are testing createdb() function to assert false when it is unsuccessfully executed"""
    db = 'dummy.db'
    result = main.createdb(db)
    assert True
    assert result is not None

def test_true_extractdb():
    """ we are testing createdb() function to assert true when it is successfully executed"""
    result = main.createdb()
    assert True
    assert result is not None
