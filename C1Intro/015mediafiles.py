# Core Packages
import streamlit as st

# Working with Media Files (videos/images/audio)
# Display images
from PIL import Image
img=Image.open("/home/binp/Desktop/learn_streamlit/C0ExtFiles/Photo/image01.jpg")
st.image(img,use_column_width=True)

# From URL
st.image("https://th.bing.com/th/id/OIP.lzq4Yxx2Z4oH6weaU0qm8AHaEl?pid=ImgDet&rs=1")


# Display Videos
video_file=open("/home/binp/Desktop/learn_streamlit/C0ExtFiles/Liên_Khúc_Nhạc_Xuân_Cringe_Năm 2021 - NTVP.mp4","rb").read()
st.video(video_file)

# Display Audio
audio_file=open("/home/binp/Desktop/learn_streamlit/C0ExtFiles/Lien_Khuc Nhac_Xuan_Cringe_Nam_2021-NTVP.mp3","rb")
st.audio(audio_file.read())