import os
import pprint
import json
import time
import asyncio
import spotipy
from lib import config
from yt_dlp import YoutubeDL
from pyrogram import Client
from youtubesearchpython import VideosSearch
from spotipy.oauth2 import SpotifyClientCredentials
from pyrogram.types.messages_and_media import Message


credentials = SpotifyClientCredentials(client_id=config.CLIENT_ID,client_secret=config.SECRET)
sp = spotipy.Spotify(client_credentials_manager=credentials)


async def grab(bot:Client,msg:Message) :
    chat_id = msg.chat.id
    link = msg.text.replace("/grab ","")
    try :
        link_type = link.split("/")[3]
    except :
        await msg.reply_text("\"ɢʀᴀʙ\" doᥱs not sᥙρρort thιs sᥙffιx ⚠")
        return
    if link_type == "track" :
        message = await msg.reply("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ  ○○○")
        track = sp.track(link)
        song_name = sp.track(link)["name"]
        artist = track["artists"][0]["name"]
        try :
            album = track["album"]["name"]
        except :
            print("no")
        if album :
            link = VideosSearch(f"{song_name} {artist} {album}",limit=1).result()["result"][0]["link"]
        else :
            link = VideosSearch(f"{song_name} {artist}",limit=1).result()["result"][0]["link"]
        video_info = YoutubeDL().extract_info(url=link,download=False)
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
            }

        with YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        await msg.reply_document(filename,quote=False)
        os.remove(filename)
        await bot.delete_messages(chat_id=msg.chat.id,message_ids=message.id)





    elif link_type == "playlist" :
        offset = 0
        response = sp.playlist_items(link,offset=offset,fields='items.track.id,total',additional_types=['track'])
        x = time.time()
        completed = 0 
        message = await msg.reply_text(f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ .\ncompleted : {completed}/{len(response['items'])}")

        for i in range(0,len(response["items"])):
            song_id = response["items"][i]["track"]["id"]
            track = sp.track(song_id)
            song_name = sp.track(song_id)["name"]
            artist = track["artists"][0]["name"]
            try :
                album = track["album"]["name"]
            except :
                print("no")
            if album :
                link = VideosSearch(f"{song_name} {artist} {album}",limit=1).result()["result"][0]["link"]
            else :
                link = VideosSearch(f"{song_name} {artist}",limit=1).result()["result"][0]["link"]
            video_info = YoutubeDL().extract_info(url =link,download=False)
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
            await bot.edit_message_text(chat_id=chat_id,message_id=message.id,text=f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ \n\ncoмpleтed : {completed}/{len(response['items'])}")
        y = time.time()
        z = y - x
        z = str(z).split(".")[0]
        await bot.delete_messages(chat_id,message_ids=message.id)
        await msg.reply_text(f"ᴛᴏᴛᴀʟ sᴏɴɢs : {len(response['items'])}\n\nᴛɪᴍᴇ ᴛᴏᴏᴋ : {z} sᥱᥴs")
    else :
        await msg.reply_text("oρᥱrᥲtιon not sᥙρρortᥱd ⚠")
