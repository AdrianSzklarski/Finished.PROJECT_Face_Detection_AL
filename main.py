import tkinter as tk

from module.clear import get_clear_dir

'''Face detection is a computer technology used in many applications that identifies 
human faces in digital images. Face detection also refers to the psychological process 
by which humans locate and pay attention to faces in a visual scene. The program 
demonstrates face detection, and performs analysis which is presented on the website. '''

from camera_strem import CameraStrem

if __name__ == '__main__':
    get_clear_dir()
    root = tk.Tk()
    CameraStrem(root)
    root.mainloop()
