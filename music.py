from pygame import mixer
mixer.init()

def set_background_music(music_path):
    mixer.music.load(music_path)
    mixer.music.play()

def play_music_for_event(music_path):
    event_music = mixer.Sound(music_path)
    event_music.play()