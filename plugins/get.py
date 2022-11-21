import os
import asyncio
from lib import config
from time import sleep
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
import spotipy
from pyrogram import Client
from spotipy.oauth2 import SpotifyClientCredentials
from pyrogram.types.messages_and_media import Message


credentials = SpotifyClientCredentials(client_id=config.CLIENT_ID,client_secret=config.SECRET)
sp = spotipy.Spotify(client_credentials_manager=credentials)


async def get(bot:Client,msg:Message) :
    chat_id = msg.chat.id
    query = msg.text.replace("/get ","")
    #message = await msg.reply("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ  ○○○")
    raw_data = sp.search(query)["tracks"]
    fltData = raw_data["items"]
    try :
        link = fltData[0]["external_urls"]["spotify"]
        artist_name = fltData[0]["artists"][0]["name"]
        song_name = fltData[0]["name"]
    except :
        await msg.reply_text("404 song not foᥙnd")
        return
    message = await msg.reply("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ  ○○○")
    #artist_name = fltData[0]["artists"][0]["name"]
    #song_name = fltData[0]["name"]
    fltsearch = f"{song_name} {artist_name}"
    """
    await bot.edit_message_text(chat_id,message.id,text="ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ  ○○●")
    results = YoutubeSearch(fltsearch, max_results=1).to_dict()[0]["url_suffix"]
    link = YouTube(f"https://youtube.com{results}")
    await bot.edit_message_text(chat_id,message.id,text="ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ  ○●●")
    video = link.streams.filter(only_audio=True).first()
    await asyncio.sleep(2)
    raw_file = video.download(output_path=".")
    await bot.edit_message_text(chat_id,message.id,text="ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ  ●●●")
    base, ext = os.path.splitext(raw_file)
    await bot.edit_message_text(chat_id,message.id,text="sᴇɴᴅɪɴɢ  ○○●")
    document = f"{base}.mp3"
    await bot.edit_message_text(chat_id,message.id,text="sᴇɴᴅɪɴɢ  ○●●")
    os.rename(raw_file,document)
    await bot.edit_message_text(chat_id,message.id,text="sᴇɴᴅɪɴɢ  ●●●")
    await msg.reply_document(document)
    await bot.delete_messages(chat_id,message.id)
    os.remove(document)"""


    results = YoutubeSearch(fltsearch, max_results=1).to_dict()[0]["url_suffix"]
    video_info = YoutubeDL().extract_info(url =f"https://youtube.com{result}",download=False)
    filename = f"{video_info['title']}.mp3"
    options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
            }

    with YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    await msg.reply_document(filename,quote=False)
    completed += 1
    os.remove(filename)
