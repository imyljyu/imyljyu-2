import streamlit as st
from study_timer import render_study_timer

st.set_page_config(page_title="공부 타이머", page_icon="⏱️", layout="centered")

st.title("📚 공부 타이머")
render_study_timer()
