# File: lib/diary.py
from lib.class_diary_entry2 import *
import math
class Diary():
    def __init__(self):
        self._list = []

    def add(self, entry):
        self._list.append(entry)
        print(self._list)

    def all(self):
        return self._list

    def count_words(self):
        contents1 = self._list[0]
        contents2 = self._list[1]
        contents3 = self._list[2]
        return contents1.count_words() + contents2.count_words() + contents3.count_words()
        # word_count = [entry.count_words() for entry in self._list]
        # return sum(word_count)
        

    def reading_time(self, wpm):
        contents1 = self._list[0]
        contents2 = self._list[1]
        contents3 = self._list[2]
        time_to_read = contents1.reading_time(wpm) + contents2.reading_time(wpm) + contents3.reading_time(wpm)
        return time_to_read
        # word_count = self.count_words()
        # return math.ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        readable_words = wpm * minutes
        most_readable = None
        longest_words_so_far = 0
        readable_entries = []
        for entry in self._list:
            if entry.count_words() == readable_words or entry.count_words() < readable_words:
                most_readable = entry
                longest_words_so_far = entry.count_words()
        return most_readable


    