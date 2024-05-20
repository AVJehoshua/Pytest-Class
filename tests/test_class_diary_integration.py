from lib.class_diary import *
from lib.class_diary_entry2 import *
import math

"""
given i add a diary entry, it adds that entry into the diary
"""

def test_to_add_entry_into_diary():
    diary = Diary()
    entry_1 = DiaryEntry("An absurd day", "I embraced the absurd")
    diary.add(entry_1)
    assert diary.all() == [entry_1]

"""
Given i add multiple diary entries, it adds the entry to
the diary
"""

def test_multiple_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("An absurd day", "I embraced the absurd")
    entry_2 = DiaryEntry("The myth of Sisyphus", "The repeated struggle")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]


"""
Given there are diary entries, it returns a number representing
all words in all diary entries

"""

def test_count_of_all_words_in_all_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("An absurd day", "I embraced the absurd every day")
    entry_2 = DiaryEntry("The myth of Sisyphus", "The repeated struggle over and over and over")
    entry_3 = DiaryEntry("The Fall", "A story of love, debauchery and self actualisation")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.count_words() == 22



"""
Given a string representing wpm, 
it returns an integer, representing an estimate,
of reading time in mins,
if user were to read all entries in the diary

"""

def test_reading_time_of_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("An absurd day", "I embraced the absurd")
    entry_2 = DiaryEntry("The myth of Sisyphus", "The repeated absurd struggle")
    entry_3 = DiaryEntry("The Fall", "A story of love, debauchery, and self actualisation")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.count_words() == 16
    assert diary.reading_time(2) == 8




"""
Given 2 added entries, one long one short, 
with a wpm of 2 and reading time 
'find_best_entry' returns the best entry(closest or exact) that can be read within
given time

"""

def test_best_entry_wpm_of_2_reading_time_of_3():
    diary = Diary()
    diary_entry1 = DiaryEntry("An absurd day", "Embrace the absurd")
    diary_entry2 = DiaryEntry("The myth of Sisyphus", "The repeated struggle over and over and")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == diary_entry1



"""
Given 3 added entries, 1 exact, 1 long and 1 short, 
with a wpm of 2 and reading time of 4
'find_best_entry' returns the entry with exact readable words that can be read within
given time

"""

def test_best_entry_wpm_of_2_reading_time_of_4():
    diary = Diary()
    diary_entry1 = DiaryEntry("An absurd day", "Embrace the absurd")
    diary_entry2 = DiaryEntry("The myth of Sisyphus", "The repeated struggle over and over")
    diary_entry3 = DiaryEntry("The Fall", "A story of love debauchery and self actualisation")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.find_best_entry_for_reading_time(2, 4) == diary_entry3