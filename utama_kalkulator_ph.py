import streamlit as st

from st_pages import Page, add_page_title, show_pages

"## Declaring the pages in your app:"

show_pages([    Page("utama_kalkulator_ph.py", "Home", "🏠"),
                Page("phlarutanasam_kalkulator_ph.py", "Menghitung pH Larutan Asam", ":books:"),])

add_page_title()  # Optional method to add title and icon to current page
