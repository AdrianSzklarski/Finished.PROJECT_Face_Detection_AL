import moviepy.editor as moviepy
import os

def mp4():
    clip = moviepy.VideoFileClip("/home/adrian/Pulpit/GitHub_Public/Dectenion_face/avi/fecedetection.avi")
    clip.write_videofile("/home/adrian/Pulpit/GitHub_Public/Dectenion_face/avi/fecedetection.mp4")

if __name__=='__main__':
    path = r'/home/adrian/Pulpit/GitHub_Public/Dectenion_face/avi'
    if os.listdir(path):
        mp4()
    else:
        pass


