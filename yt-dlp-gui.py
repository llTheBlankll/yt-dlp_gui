import os
import subprocess
import sys

from time import sleep as stop


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    clear()
    youtube_url: str = str(input("Youtube URL: "))
    if youtube_url == "exit":
        sys.exit()
    elif youtube_url == "":
        print("Empty URL!")
        stop(1)
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
            ]
        )


if __name__ == "__main__":
    menu()
