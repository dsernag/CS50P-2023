from project import (youtube_searcher,
                     get_all_songs,
                     search_metadata,
                     obtain_sp_client,
                     DownloadFile)
"""
Please run this command in terminal before running testings:
source set-envs.sh
"""

def test_youtube_searcher():
    assert youtube_searcher("Michael Jackson Thriller Official Video 4K Video") == "https://youtu.be/sOnqjkJTMaA"
    assert youtube_searcher("So fresh So Clean Outkast") == "https://youtu.be/-JfEJq56IwI"

def test_get_all_songs():
    assert get_all_songs("./test_songs.csv") == [{'artist': 'Ketekalles', 'song': 'Nieva'}, {'artist': 'Muerdo ft Perota Chingó', 'song': 'Semillas'}, {'artist': 'Tuyos (Narcos Theme)', 'song': 'Rodrigo Amarante'}, {'artist': 'Los Zafiros', 'song': 'He Venido'}, {'artist': 'Sandra Bernardo', 'song': 'Lola'}]
    assert get_all_songs("./.") == ["The route doesn't exist"]

def test_search_metadata():
    sp = obtain_sp_client()
    downloadfile1 = DownloadFile("Michael Jackson Thriller Official Video 4K Video")
    downloadfile2 = DownloadFile("So fresh So Clean Outkast")
    assert search_metadata(sp, downloadfile1) == {'song_name': 'Thriller (Steve Aoki Midnight Hour Remix)', 'type': 'track', 'album': 'Thriller (Steve Aoki Midnight Hour Remix)', 'artist': 'Michael Jackson', 'relase': '2017-09-29'}
    assert search_metadata(sp, downloadfile2) == {'song_name': 'So Fresh, So Clean', 'type': 'track', 'album': 'Stankonia', 'artist': 'Outkast', 'relase': '2000-10-31'}
