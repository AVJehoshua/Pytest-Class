# File: lib/track.py
# Example of a data class, primary function adding info and 
# represent a 'track' and 'title', and then format it into a 
# nice sentence
class Track():
    # Public properties:
    #   title: a string
    #   artist: a string

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def format(self):
        return f"{self.title} by {self.artist}"
