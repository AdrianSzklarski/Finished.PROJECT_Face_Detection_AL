import moviepy.editor as moviepy
def mp4():
    clip = moviepy.VideoFileClip("/home/adrian/Pulpit/GitHub_Public/Dectenion_face/avi/fecedetection.avi")
    clip.write_videofile("/home/adrian/Pulpit/GitHub_Public/Dectenion_face/avi/fecedetection.mp4")