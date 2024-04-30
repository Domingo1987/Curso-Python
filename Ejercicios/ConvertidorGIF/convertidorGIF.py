from moviepy.editor import VideoFileClip

# Load the video file
video_path = 'Ejercicios//ConvertidorGIF//acceso.mp4'
video = VideoFileClip(video_path)

# Trim the complete duration of the video (8 seconds)
# El video debe tener una ´duracion´.
gif_clip = video.subclip(0, video.duration)


# Define the path to save the full duration GIF
gif_path = 'Ejercicios//ConvertidorGIF//duration_clip.gif'

# Save the trimmed clip as a GIF for the full duration
gif_clip.write_gif(gif_path, fps=10)

# Output the path to the GIF file
gif_path
