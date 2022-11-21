import os
import time
import youtube_dl
def download_ytvid_as_mp3():
    start=time.time()
    video_url = "https://youtu.be/4jTy5jnMkYc"
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    stop = time.time()
    print(stop-start)
    print("Download complete... {}".format(filename))
    os.remove(filename)
download_ytvid_as_mp3()
