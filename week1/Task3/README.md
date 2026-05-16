Task 3 - Add Audio to Video

 Audio Source

https://pixabay.com/music/modern-classical-deep-sea-324392/    


Command Used

ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac final_output.mp4

Output

* Final video with audio merged

Notes

Audio successfully synced with video using ffmpeg.

