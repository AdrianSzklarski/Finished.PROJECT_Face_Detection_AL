import tkinter as tk
import cv2


class CameraStrem:
    def __init__(self, root, camera=0):
        self.root = root
        self.video_source = camera  # commit 1
        self.capture = CaptureAvi(self.video_source)

        self.get_set_window()

    def get_set_window(self):
        '''Set window of *.*avi'''
        self.root.title("Face Detection create by A.Szklarski 02.2023")
        self.root.geometry('640x480')


class CaptureAvi:
    def __init__(self, camera=0):
        self.capture = cv2.VideoCapture(camera)  # commit 2
        if not self.capture.isOpened():
            raise ValueError("Attention, video failed to open", camera)

        self.get_dimensions()
    def get_dimensions(self):
        '''Download window dimensions *.*avi'''
        self.width = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(self.width, self.height)  # test information


# Test run, after delete
if __name__ == '__main__':
    root = tk.Tk()
    CameraStrem(root)
    root.mainloop()

#  My commits:

#  no 1:
#  definition of 'cv2.VideoCapture(0)', camera=0 so:
'''This is the camera index, which is used to select different cameras if you have more 
than one connected. By default, 0 is your primary. if I had two cameras, my index = 1'''

#  no 2: define a video capture object
