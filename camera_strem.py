import tkinter as tk


class CameraStrem:
    def __init__(self, root, camera=0):
        self.root = root
        self.video_source = camera  # commit 1

        self.get_set_window()

    def get_set_window(self):
        self.root.title("Face Detection create by A.Szklarski 02.2023")
        self.root.geometry('800x640')


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