from jarvis_features import features
jarvis = features()
cm = jarvis.listen()
if "play" in cm or "band kar" in cm or "pause" in cm:
    jarvis.yt_play_pause()
if "close" in cm:
    jarvis.close_app()
