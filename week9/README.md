<!-- **Author:** David Serna Gutiérrez -->
# DOWNLOAD MUSIC FROM YOUTUBE AND METADATA FROM SPOTIFY
#### Video Demo: https://youtu.be/SrnRcDFxgM8
#### Description:
##### Introduction

This project born thanks to CS50P Final Project and a personal pursue to automate the download process of music.
There are some issues pending to solve in further versions, but meanwhile It's a decent product which accomplish the final project request.

The main goal of this program is to download music from YouTube in mp3 format and using Spotify Developer search album and release year metadata from a long list of songs. Nonetheless it's possible to use individual functions from the code to download one specific song using a concatenated string formatted as "Artist - Song".

There are several requirements to run correctly the code, please follow the next steps.

##### Requirements

To successfully replicate this environment you will need Python >= 3.10 version installed and a couple of packages. Run the following command:

```
pip install -r requirements.txt
```
The downloaded music from YouTube naturally comes in `.mp4` format. To convert properly to `.mp3` it's not enough renaming the file. The open-source framework [ffmpeg](https://www.ffmpeg.org/) allows an easy approach to achieve the conversion. Because my developing environment is Linux you should run:

```
sudo apt update
sudo apt install ffmpeg
```

If you are using a Windows environment the easiest way it's to download the [latest Win64 build](https://github.com/BtbN/FFmpeg-Builds/releases) and add the binary folder to the Windows PATH.

Finally, because We're using Spotify Developer you must have a [Spotify Account](https://open.spotify.com/) and [Activate the Developer Mode](https://medium.com/@michaelmiller0998/extracting-song-data-from-spotify-using-spotipy-167728d0a924) to obtain the `Client_ID` and `CLIENT_SECRET` required to query the metadata.

##### How to use

After installing the requirements we're almost ready to download massively music 🤗, but first we need to:

1. Set `Client_ID` and `CLIENT_SECRET` as environmental variables in the OS (if you're using Linux, just put them as strings in `set-envs.sh` file). These credentials are secret and were obtained when we activated developer mode on Spotify.

2. Create a `songs.csv` file to store all the music you want to download in this format
    | ID | Artist | Song |
    | :-: | :-: | :-: |
    | 1 | Michael Jackson | Thriller |
    | 2 | Black Sabbath | Paranoid |
    | n | ... | ... |

3. You must ensure the secrets were saved as environmental variables no matter your OS. If don't want to deal with env vars you can replace in `obtain_sp_client` function the proper credentials:
    ```python
    client_id = "1cb**************************af8"#os.getenv("CLIENT_ID")
    client_secret = "f08**************************435"#os.getenv("CLIENT_SECRET")
    ```
    Because I'm publishing to public audience, I'll not share my credentials, so please get yours 😁

4. Now let's run 🚀:
    ```
    python project.py
    ```
    And wait to download every song. If the song was downloaded it won't overwrite it.
    Enjoy 😁
