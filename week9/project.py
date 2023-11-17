import json
import spotipy
import pandas as pd
import os
import ast
from utils import parse_song_name
from pytube import YouTube
from youtube_search import YoutubeSearch
from spotipy.oauth2 import SpotifyClientCredentials
from mutagen.easyid3 import EasyID3

DOWNLOAD_FOLDER = "./downloads/"

class DownloadFile:
    def __init__(self, search_term: str) -> None:
        self.search_term = search_term
        self.yt_link = youtube_searcher(self.search_term)
        self.initial_filepath = DOWNLOAD_FOLDER + self.search_term + ".mp4"
        self.final_filepath = DOWNLOAD_FOLDER + self.search_term + ".mp3"

    def mp4tomp3(self) -> None:
        command = f'ffmpeg -loglevel panic -i "{self.initial_filepath}" "{self.final_filepath}"'
        os.system(command)
        os.remove(self.initial_filepath)

def youtube_searcher(search_term: str) -> str:
    results = json.loads(YoutubeSearch(search_term, max_results = 1).to_json())
    id_ = results["videos"][0]['id']
    return f"https://youtu.be/{id_}"

def download_youtube(downloadfile : DownloadFile) -> None:
#https://www.tutorialspoint.com/download-video-in-mp3-format-using-pytube
    try:
        if os.path.exists(downloadfile.final_filepath):
            print(f"The file '{downloadfile.search_term}.mp3' already exists")
        else:
            video = YouTube(downloadfile.yt_link)
            stream = video.streams.filter(only_audio = True).first()
            stream.download(filename = downloadfile.initial_filepath)
            downloadfile.mp4tomp3()
            print(f"The file '{downloadfile.search_term}.mp3' was downloaded in MP3")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")

def get_all_songs(filepath : str) -> list:
    try:
        dataframe = pd.read_csv(filepath)[["artist", "song"]]
        list_songs =  dataframe.to_json(orient = "records", force_ascii = False)
        list_songs = list_songs.replace('\\/', ' ')
        return ast.literal_eval(list_songs)
    except:
        return ["The route doesn't exist"]

def obtain_sp_client() -> spotipy.Spotify:
#https://medium.com/@michaelmiller0998/extracting-song-data-from-spotify-using-spotipy-167728d0a924
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
    return spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def search_metadata(sp : spotipy.Spotify, downloadfile : DownloadFile) -> dict:
    spoti_result = sp.search(downloadfile.search_term)
    spoti_result = spoti_result['tracks']['items'][0]
    return {
        "song_name" : spoti_result["name"].strip(),
        "type" : spoti_result["type"].strip(),
        "album" : spoti_result["album"]["name"].strip(),
        "artist" : spoti_result["album"]["artists"][0]["name"].strip(),
        "relase" : spoti_result["album"]["release_date"].strip()
        }

def modify_metadata(downloadfile : DownloadFile, metadata: dict) -> None:
    tags = EasyID3(downloadfile.final_filepath)
    tags['title'] = metadata["song_name"]
    tags['albumartist'] = metadata["artist"]
    tags['album'] = metadata["album"]
    tags['date'] = metadata["relase"]
    tags.save()
    print(f"Metadata modified for '{downloadfile.final_filepath}' done")

def download_massive(list_dicts : list):
    actual_songs = list(map(lambda xx : xx.replace(".mp3", ""), os.listdir(DOWNLOAD_FOLDER)))
    to_download = [ii for ii in list_dicts if parse_song_name(ii) not in actual_songs]
    sp = obtain_sp_client()
    if len(to_download) == 0:
        print("The whole list was already downloaded")
    else:
        for element in to_download:
            search_term = parse_song_name(element)
            downloadfile = DownloadFile(search_term)
            download_youtube(downloadfile)
            metadata = search_metadata(sp, downloadfile)
            modify_metadata(downloadfile, metadata)

def main():
    try:
        os.makedirs(DOWNLOAD_FOLDER)
    except:
        print(f"'{DOWNLOAD_FOLDER}' already exist.")
    song_list = "songs.csv"
    list_songs = get_all_songs(song_list)
    download_massive(list_songs)

if __name__ == "__main__":
    main()
