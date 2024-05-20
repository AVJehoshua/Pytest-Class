
from lib.class_diary_entry2 import *
import pytest
"""
Given a title and contents, we can 
return the title and contents back
"""
def test_creation_of_title_and_contents():
    diary_entry = DiaryEntry("An absurd day", "I embraced the absurd")
    assert diary_entry.title == "An absurd day"
    assert diary_entry.contents == "I embraced the absurd"


"""
Given there are diary contents,
it returns the length of words of one diary
entry

"""

def test_count_of_words_in_diary_entry_contents():
    diary_entry1 = DiaryEntry("An absurd day", "I embraced the absurd")
    assert diary_entry1.count_words() == 4

"""
Given there are multiple diary entries,
it returns the length of words of all diary
entries
"""

def test_count_of_all_entry_words_in_diary():
    diary_entry1 = DiaryEntry("An absurd day", "I embraced the absurd")
    diary_entry2 = DiaryEntry("The myth of Sisyphus", "The repeated struggle")
    assert diary_entry1.count_words() == 4
    assert diary_entry2.count_words() == 3


"""
Given a wpm of 2, 
and a text of 2 words,
reading_time 1 minute
"""

def test_if_wpm_is_2_return_estimate():
    diary_entry = DiaryEntry("The myth of Sisyphus", "Some contents")
    assert diary_entry.reading_time(2) == 1
    

"""
Given a wpm of 2 
and a text of 4 words
reading time returns 4 mins

"""

def test_if_wpm_is_2_return_estimate():
    diary_entry = DiaryEntry("The myth of Sisyphus", "Some contents and more")
    assert diary_entry.reading_time(2) == 2


"""
Given a wpm of 2
and a text of 3 words
reading time returns 2 mins (rounded up)
"""

def test_reading_time_with_2_wpm_3_words():
    diary_entry = DiaryEntry("The myth of Sisyphus", "Some absurd contents ")
    assert diary_entry.reading_time(2) == 2


"""
Given a wpm of 0
reading time raises an exception error
"""

def test_reading_time_wpm_of_0():
    diary_entry = DiaryEntry("The myth of Sisyphus", "Some absurd contents")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "No time to read!"
    

"""
Given a diary entry with no title and
no contents, return an exception message

"""

def test_no_title_no_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry(" ", " ")
    assert str(e.value) == "Diary entry must have title and contents!"


"""
Given a diary entry with a title but no contents,
raise exception error

"""

def test_yes_title_no_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("The myth of Sisyphus", " ")
    assert str(e.value) == "Diary entry must have title and contents!"



"""
Given a diary entry with no title, but some contents
raise an exception error

"""

def test_no_title_yes_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry(" ", "An absurd struggle")
    assert str(e.value) == "Diary entry must have title and contents!"


"""
Given a text(contents) of 4 words, a wpm of 2
and a 1 minutes
reading chunk returns first 2 words
"""

def test_reading_chunk_2_wpm_1_minutes():
    diary_entry = DiaryEntry("The myth of Sisyphus", "The absurd is eternal")
    assert diary_entry.reading_chunk(2, 1) == "The absurd"

"""
Given a text(contents) of 6 words, a wpm of 2
and minutes of 2
reading chunk returns first 4 words
"""

def test_reading_chunk_4_wpm_2_minutes():
    diary_entry = DiaryEntry("The myth of Sisyphus", "The absurd is eternal embrace it")
    assert diary_entry.reading_chunk(2, 2) == "The absurd is eternal"


"""
Given a text(contents) of 6 words, a wpm of 2
and minutes of 2
first time reading_chunk returns first 2 words
if called again, next 2 words
"""

def test_reading_chunk_2_wpm_1_min_called_multiple_times():
    diary_entry = DiaryEntry("The myth of Sisyphus", "The absurd is eternal embrace it")
    assert diary_entry.reading_chunk(2, 1) == "The absurd"
    assert diary_entry.reading_chunk(2, 1) == "is eternal"
    assert diary_entry.reading_chunk(2, 1) == "embrace it"
    

"""
Given a text(contents) of 6 words, a wpm of 2
if reading chunk is called repeatedly
and all chunks of words have been read,
it starts from beginning again

"""

def test_reading_chunk_loops_around_multiple_calls():
    diary_entry = DiaryEntry("The myth of Sisyphus", "The absurd is eternal embrace it")
    assert diary_entry.reading_chunk(2, 2) == "The absurd is eternal"
    assert diary_entry.reading_chunk(2, 2) == "embrace it"
    assert diary_entry.reading_chunk(2, 2) == "The absurd is eternal"

"""
Given a text(contents) of 6 words, a wpm of 2
if reading chunk is called repeatedly
has an exact ending
it starts from beginning again
"""

def test_reading_chunk_loops_around_multiple_calls_exact_ending():
    diary_entry = DiaryEntry("The myth of Sisyphus", "The absurd is eternal embrace it")
    assert diary_entry.reading_chunk(2, 2) == "The absurd is eternal"
    assert diary_entry.reading_chunk(2, 1) == "embrace it"
    assert diary_entry.reading_chunk(2, 2) == "The absurd is eternal"