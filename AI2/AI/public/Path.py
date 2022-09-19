import os

filepath = []
for path, _, files in os.walk('./'):
     if ('Program Files' not in path) and ('AiSound' in path):
        #in case of windows system replace \ with /
        filepath.extend([os.path.join(path, file).replace('\\', '/') for file in files
                         if str(file).endswith('.mp3')])
# print(filepath)


# add app name and path and use it in open local app method
class App_path:
        notepad = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
        chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        mozilla = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
# add song name and path and use it in open local app method
class Song_path:
        song_path1 = "D:\python project\AI2\jarvish\AiSound\jarvis_alarm (1).mp3"
        song_list = filepath.copy()

