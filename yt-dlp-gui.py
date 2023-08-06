import os
import subprocess
import sys

from time import sleep as stop


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def download_single():
    clear()
    print("Downloading Single Song")
    youtube_url: str = str(input("Youtube URL: "))
    if youtube_url == "exit":
        sys.exit()
    elif youtube_url == "":
        print("Empty URL!")
        stop(0)
        menu()
    else:
        subprocess.run(
            [
                "yt-dlp",
                "-x",
                "--audio-format",
                "mp3",
                "--audio-quality",
                "0",
                "-o",
                "music/%(title)s.%(ext)s",
                "--embed-metadata",
                youtube_url,
            ],
            stdout=open("/dev/null", "wb")
        )
        print(f"{youtube_url} was downloaded successfully!")


def download_multiple():
    clear()
    print("Downloading Multiple Songs")
    print("Type 'done' if you're finished listing the songs you want to download")
    songs_list: list = []
    while True:
        url: str = str(input("URL: "))
        if url == "done":
            break
        songs_list.append(url)

    if len(songs_list) == 0:
        print("Empty URL!")
        stop(0)
        menu()

    for song_url in songs_list:
        print("Downloading %s" % song_url)
        subprocess.run(
            [
                "yt-dlp",
                "-x",  # Extract audio
                "--audio-format",  # Audio format
                "mp3",
                "--audio-quality",
                "0",  # 0 for best quality
                "-o",
                "music/%(title)s.%(ext)s",  # Output without random strings
                "--embed-metadata",  # Add metadata like artists
                song_url,
            ],
            stdout=open("/dev/null", "wb")  # Silent output
        )
    print(f"{len(songs_list)} was successfully downloaded!")

def menu():
    clear()
    print("Sections")
    print("1. Download Single Song")
    print("2. Download Multiple Songs")
    try:
        select: int = int(input("Select: "))
        if select == 0 or select == "":
            print("Selection cannot be empty!")
            stop(1)
            menu()
        elif select == 1:
            download_single()
        elif select == 2:
            download_multiple()
        else:
            print(f"Invalid number {select}")
            stop(1)
            menu()
    except ValueError:
        print("Only numerical values are allowed!")
        stop(1)
        menu()


if __name__ == "__main__":
    menu()
