import youtube_dl

def download_audio(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '1'
        }, {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }],
        'outtmpl': '%(title)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([link])
            print("Download completed successfully!")
        except youtube_dl.DownloadError as e:
            print(f"Download failed: {str(e)}")

def validate_link(link):
    # Return True if the link is valid, otherwise return False
    if link.startswith("http://") or link.startswith("https://"):
        return True
    else:
        return False

def main():
    link = input("Enter the link: ")

    if validate_link(link):
        download_audio(link)
    else:
        print("Invalid link!")

if __name__ == '__main__':
    main()

