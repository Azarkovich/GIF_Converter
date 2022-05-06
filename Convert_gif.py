# Create a gif converter
from moviepy.editor import VideoFileClip

clip = VideoFileClip("Video.mp4")
clip.write_gif("mygif.gif", fps=10)