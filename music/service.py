from ShazamAPI import Shazam
import requests
def qoshiqtext(filepath):
    file = open(filepath,'rb').read()
    info = Shazam(file)
    recognizer = info.recognizeSong()
    for data in recognizer:     
      try:
        name_singer = data[1]['track']['subtitle']
      except:
        name_singer = None
        pass
      try:
        name_song = data[1]['track']['title']
      except:
        name_song = None
      try:
        data = requests.get(data[1]['track']['sections'][1]['url'])
        jsoni = data.json()
        lyrics = jsoni['syncedtext']
      except:
        lyrics = None   
        pass
      try:
        music_img = data[1]['track']['images']['background']
      except:
        music_img=None
        pass
      break

    x = dict({
      'singer':name_singer,
      'song_name':name_song,
      'lyrics':lyrics,
      'music_img':music_img,
    })
    return x
