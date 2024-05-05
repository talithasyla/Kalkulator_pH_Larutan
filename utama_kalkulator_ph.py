import streamlit as st
from st_pages import Page, show_pages, add_page_title

show_pages(
    [ Page("streamlit_app.py", "Home", "🏠"),
      Page("other_pages/page2.py", "Page 2", ":books:"),])
