import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly


def start_page():
    st.set_page_config("spekcle test", ":arrow:")
    st.title("welcome")


if __name__ == '__main__':
    start_page()