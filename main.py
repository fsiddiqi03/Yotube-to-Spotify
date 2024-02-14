from pytube import YouTube
import os
import ffmpeg


def main():
    first_time = True
    while True:
        try:
            if first_time:
                destination = input('Please provide spotify local files destination: \n>>')
            yt = YouTube(input('Please paste youtube link: \n>> '))
            audio = convert(yt)
            download_path = download(audio)
            convert_to_mp3(download_path, destination)

            answer = input('Would you like to add more? y | n: \n>>').lower()
            if answer == 'n':
                break
            first_time = False
            
        except Exception as e:
            print(f'Error: {e}')


# takes the youtube video as a param 
# returns a stream type, including res, vid type
def convert(yt):
    return yt.streams.filter(only_audio=True).first()


# downloads video, as what is available which could be video, mp3, mp4
# first need to convert mp4 to mp3 using ffmpeg 
# destination should be the mp4 file folder ,
def download(audio):
    destination = 'mp4_audio'
    out_file = audio.download(output_path = destination)
    return out_file



def convert_to_mp3(file_path, destination_path):
    base, ext = os.path.splitext(file_path)
    new_file = base + '.mp3'
    # FFmpeg command to convert MP4 to MP3
    ffmpeg.input(file_path).output(new_file).run()
    # Move the MP3 file to the user specified destination
    os.rename(new_file, os.path.join(destination_path, os.path.basename(new_file)))
    # Optionally, delete the original download (MP4) to save space
    os.remove(file_path)
    print(f'Converted and moved MP3 to {destination_path}')



if __name__ == "__main__":
    main()




