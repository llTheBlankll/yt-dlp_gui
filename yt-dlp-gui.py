import os
import subprocess
import sys

from time import sleep as stop

# Settings
MUSIC_DIRECTORY: str = "music"


def clear():
    """
    Clears the console screen.

    This function checks the operating system name and uses the appropriate command to clear the console screen. On Windows, it uses the "cls" command, and on other operating systems, it uses the "clear" command.

    This function does not take any parameters.

    This function does not return any value.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def download(youtube_url: str, custom_folder: str = ""):
    """
    Downloads a YouTube video as an MP3 file.

    Args:
        youtube_url (str): The URL of the YouTube video to download.
        custom_folder (str, optional): The custom folder to save the downloaded file in. Defaults to empty string.

    """
    if custom_folder != "":
        print(f"Downloading {youtube_url} to folder {custom_folder}")

    subprocess.run(
        [
            "yt-dlp",
            "-x",
            "--audio-format",
            "mp3",
            "--audio-quality",
            "0",
            "-o",
            MUSIC_DIRECTORY + "/ " + custom_folder + "%(title)s.%(ext)s",
            "--embed-metadata",
            youtube_url,
        ],
        stdout=open("/dev/null", "wb")
    )


def download_single():
    """
    Downloads a single song from a given YouTube URL.

    Parameters:
        None

    Returns:
        None
    """
    custom_folder: str = ""
    clear()
    print("Downloading Single Song or Entire Playlist")
    youtube_url: str = str(input("Youtube URL: "))
    if youtube_url == "exit":
        sys.exit()
    elif youtube_url == "":
        print("Empty URL!")
        stop(0)
        menu()
    else:
        choice: str = str(input("Yes/No : "))
        if choice.lower() == "yes":
            custom_folder = str(input("Enter your new folder name: "))
        
        if custom_folder != "":
            download(youtube_url, custom_folder)
        else:
            download(youtube_url);


def download_multiple():
    """
    Downloads multiple songs from a list of URLs.

    This function prompts the user to enter a list of URLs of songs to download. It
    then downloads each song using the `yt-dlp` command-line tool, which extracts the
    audio in MP3 format with the best quality. The downloaded songs are saved in the
    `music/` directory with their titles as the file names.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - None
    """
    clear()
    print("Downloading Multiple Songs or Multiple Playlist")
    print("Type 'done' if you're finished listing the songs you want to download")
    songs_list: list = []
    custom_folder: str = ""
    while True:
        url: str = str(input("URL: "))
        if url == "done":
            break
        songs_list.append(url)

    print("Do you want to store the downloaded video/music files into separate folder?")
    choice: str = str(input("Yes/No : "))
    if choice.lower() == "yes":
        custom_folder = str(input("Enter your new folder name: "))

    if len(songs_list) == 0:
        print("Empty URL!")
        stop(0)
        menu()

    for song_url in songs_list:
        print("Downloading %s" % song_url)
        if custom_folder != "":
            download(song_url, custom_folder)
        else:
            download(song_url)
    print(f"{len(songs_list)} was successfully downloaded!")


def menu():
    """
    Displays a menu to the user and performs actions based on their selection.

    Parameters:
        None

    Returns:
        None
    """
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
    if not os.path.exists("./music"):
        os.mkdir("music")
    menu()
