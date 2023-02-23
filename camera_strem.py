import tkinter as tk


class CameraStrem:
    def __init__(self, root):
        self.root = root

        self.get_set_window()

    def get_set_window(self):
        self.root.title("Face Detection create by A.Szklarski 02.2023")
        self.root.geometry('800x640')


# Test run, after delete
if __name__ == '__main__':
    root = tk.Tk()
    CameraStrem(root)
    root.mainloop()
