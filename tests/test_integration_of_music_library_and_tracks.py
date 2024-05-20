"""
Given i add 2 tracks, i see the represented in the list

"""

from lib.class_music_library import *
from lib.class_music_track import *


def test_and_adds_multiple_tracks_returns_list():
    music_library = MusicLibrary()
    track_1 = Track("Water", "Tyla")
    track_2 = Track("Nostalgia", "Odunsi")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.list() == [track_1, track_2]
    


"""
Given I add 2 tracks, if i search for a title,
it returns the track back

"""

def test_searches_by_title():
    music_library = MusicLibrary()
    track_1 = Track("Water", "Tyla")
    track_2 = Track("Nostalgia", "Odunsi")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("Nostalgia") == [track_2]


"""
given i add 2 tracks, if i search for 
part of the title of one track,
i get the matching track returned back in results

"""

def test_add_test_searches_by_part_of_title():
    music_library = MusicLibrary()
    track_1 = Track("Water", "Tyla")
    track_2 = Track("Nostalgia", "Odunsi")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("Wa") == [track_1]





