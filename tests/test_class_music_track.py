"""
When we create a new track, we 
can get it's title and artist 
returned back

"""
from lib.class_music_track import *

def test_create_track_return_title_and_artist():
    track = Track("Water", "Tyla")
    assert track.title == "Water"        #title in this instance is a property, no bracket needed
    assert track.artist == "Tyla"



"""
returns a nice formatted sentemce of the title and artist
"""


def test_formats_title_and_artist():
    track = Track("Water", "Tyla")
    assert track.format() == "Water by Tyla"