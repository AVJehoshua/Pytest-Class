"""
Given there are no entries 
it returns an empty list
"""
from lib.class_diary import *

def test_if_entry_empty_return_empty_list():
    diary = Diary()
    assert diary.all() == []


