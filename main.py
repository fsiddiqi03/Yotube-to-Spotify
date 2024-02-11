from pytube import YouTube
import os


def main():
    while True:
        try:
            yt = YouTube(input('Please paste youtube link: \n>> '))
            audio = convert(yt)
            destination = input('Please provide spotify local files destination: \n>>')

            if download(audio, destination):
                print('audio downloaded')
        except:
            print('Error')


# takes the youtube video as a param 
# returns a stream type, including res, vid type
def convert(yt):
    return yt.streams.filter(only_audio=True).first()


# downloads video, as what is available which could be video, mp3, mp4
# first need to convert mp4 to mp3 using ffmpeg 
# should not include destination,
def download(audio, destination):
    return audio.download(output_path = destination)




