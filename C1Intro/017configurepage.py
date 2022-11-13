# Core packages
import streamlit as st
from PIL import Image
img = Image.open('/home/b/Desktop/learn_streamlit/C0ExtFiles/Photo/hug.jpg')
# # Must be first activity of streamlit
# METHOD 1:
# st.set_page_config(page_title='hello',
#                     page_icon='img',layout='wide',
#                     initial_sidebar_state='auto')

# METHOD 2: DICTIONARY
PAGE_CONFIG = {"page_title":"BinPe","page_icon":":smiley","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

# Additional Packages

# Func
def main():
    """All your code goes here"""
    st.title("Hello Streamlit 💜")
    st.sidebar("Menu")
    pass

if __name__ == '__main__':
    main() 