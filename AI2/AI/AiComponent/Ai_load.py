import random
from pygame import mixer 
from ..public.Path import Song_path


# mixer.init()
# mixer.music.load(Song_path.song_list[random.randrange(0,10)])
# mixer.music.set_volume(0.7)
# mixer.music.play()


class Ai_loading :

    def __init__(self, set_volume=0.7):
        self.set_volume = set_volume
        mixer.init()
        mixer.music.load(Song_path.song_list[random.randrange(0,10)])
        mixer.music.set_volume(set_volume)

    def start(self):
        mixer.music.play()

    def pause(self):
        mixer.music.pause()

    def stop(self):
         mixer.music.stop()
        

