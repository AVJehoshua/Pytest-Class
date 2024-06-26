# File: lib/diary_entry.py
import math
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        if title == " " or contents == " ":
            raise Exception("Diary entry must have title and contents!")
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def count_words(self):
        return len(str(self.contents).split(" "))

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("No time to read!")
        contents_word_count = len(self.contents.split())
        return math.ceil(contents_word_count / wpm)


    def reading_chunk(self, wpm, minutes):
        readable_words = wpm * minutes
        words = self.contents.split()
        if self.read_so_far >= len(words):
            self.read_so_far = 0

        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + readable_words
        chunk_words = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)