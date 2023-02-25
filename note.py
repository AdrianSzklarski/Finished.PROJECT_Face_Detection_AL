# TypeError: Descriptors cannot not be created directly
# pip install protobuf==3.20.*

# ---------------------------------------------------------
# 2023-02-22 23:18:31.604 WARNING root:
#   Warning: to view this Streamlit app on a browser, run it with the following
#   command:
#
#     streamlit run /home/adrian/Pulpit/GitHub_Public/Dectenion_face/camera_strem.py [ARGUMENTS]
#
# Process finished with exit code 0

# I have to run app form termial: streamlit run camera_strem.py


# $ pip install --upgrade streamlit
# $ streamlit hello

# https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace
# https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html


# Getting "TypeError: must be real number, not NoneType" whenever trying to run write_videofile to a clip in moviepy
# pip install moviepy --upgrade

# cv2.error: OpenCV(4.7.0) /io/opencv/modules/imgproc/src/color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cvtColor'
#  pip install moviepy --upgrade and delete manula all avi films from dir avi

# ---- Mój opis porblemu ---
# Traceback (most recent call last):
#   File "/home/adrian/Pulpit/GitHub_Public/Dectenion_face/main.py", line 15, in <module>
#     CameraStrem(root)
#   File "/home/adrian/Pulpit/GitHub_Public/Dectenion_face/camera_strem.py", line 29, in __init__
#     self.get_save()
#   File "/home/adrian/Pulpit/GitHub_Public/Dectenion_face/camera_strem.py", line 65, in get_save
#     self.bgr = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
# cv2.error: OpenCV(4.7.0) /io/opencv/modules/imgproc/src/color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cvtColor'

# In Polish translate:
# Przy frame dostaję None.. [[wartości]], przy None dostaję błąd ponieważ program nie wie co przy zapisnie do AVI
# ma z tym zrobić w tym miejscu:
'''def get_save(self):
    Save video to *.*avi file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('avi/fecedetection.avi', fourcc, 20, (640, 480))
    while True:
        self.ret, self.frame = self.capture.get_frames()
        # print(frame)  <----------------------------------------------------
        self.bgr = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        out.write(self.bgr)
        cv2.imshow('Streaming Video', self.bgr)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break'''
# Muszę to oprogramować !






