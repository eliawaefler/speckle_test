import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly


def start_page():
    st.set_page_config("speckle test", ":arrow:")
    st.title("welcome")
    st.markdown("""
    <iframe title="Speckle" 
    src="https://app.speckle.systems/projects/f1363936ee/models/09ebe7db28#embed=%7B%22isEnabled%22%3Atrue%2C%22isTransparent%22%3Atrue%2C%22hideControls%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%2C%22disableModelLink%22%3Atrue%7D" 
    width="600" height="400" frameborder="0"></iframe>""",
                unsafe_allow_html=True)

if __name__ == '__main__':
    start_page()