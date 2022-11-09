# Basics & Fundamentals

# Core Packages
import streamlit as st

# Working and Displaying Text
st.text("Hello World this is a text")
name = "Binpe"
st.text("This is {}".format(name))

# Title
st.title("This is a title")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Markdown
st.markdown("This is a markdown")

# Displaying Coloured Text/Bootstaps Alert
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("This is an error")
st.exception("This is an exception")