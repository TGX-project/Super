import pprint
import spotipy
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL

creds = spotipy.SpotifyClientCredentials(client_id="4954e32a6c834467a5a3a5d4f22b13a3",client_secret="06987dc45ae64b44833d57abf9e63524")


sp = spotipy.Spotify(client_credentials_manager=creds)
offset = 0
link = input("playlist : ")

track = sp.track(link)
song_name = sp.track(link)["name"]
artist = track["artists"][0]["name"]
pprint.pprint(track)
print(f"\n\n\n{song_name}{artist}")
result = VideosSearch(f"{song_name} {artist}",limit=1).result()
print(result["result"][0]["link"])
#response = sp.playlist_items(link,offset=offset,fields='items.track.id,total',additional_types=['track'])
#completed = 0                                               



'''for i in range(0,len(response["items"])):
    song_id = response["items"][i]["track"]["id"]
    track = sp.track(song_id)
    song_name = sp.track(song_id)["name"]
    artist = track["artists"][0]["name"]
    prpnt(f"\n\n{song_name}\n{artist}\n\n")'''
