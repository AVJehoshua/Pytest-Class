"""
Initially there are no tracks
return an empty list
* not an integration test, unit test as only tests one class
"""

from lib.class_music_library import *

def test_initially_no_tracks():
    music_library = MusicLibrary()
    assert music_library.list() == []


"""
Initially searching for tracks,
returns an empty list

"""

def test_initially_search_returns_empty_list():
    music_library = MusicLibrary()
    assert music_library.search_by_title("absurd") == []


