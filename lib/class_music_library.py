"""
Purpose: Music library

allows to add tracks, list added tracks and, 
search tracks by title
"""

# File: lib/music_library.py

class MusicLibrary():
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self._list_tracks = []

    def add(self, track):
        self._list_tracks.append(track)


    def list(self):
        return self._list_tracks
    

    def search_by_title(self, keyword):
        # result = []
        # for track in self.list_tracks:
        #     if track.title == keyword:
        #         result.append(track)
        # return result
        return [track for track in self._list_tracks if keyword in track.title]
