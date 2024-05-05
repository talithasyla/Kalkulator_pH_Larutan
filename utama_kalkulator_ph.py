import streamlit as st
from st_pages import show_pages_from_config, add_page_title

# Either this or add_indentation() MUST be called on each page in your app to add indendation in the sidebar
add_page_title()

show_pages_from_config()

[[pages]]
path = "streamlit_app.py"
name = "Home"
icon = "🏠"
add_page_title("Home")

[[pages]]
path = "other_pages/page2.py"
name = "Page 2"
icon = ":books:"

[[pages]]
name = "My second"
icon = "🎈️"
is_section = true

# Pages after an `is_section = true` will be indented
[[pages]]
name = "Another page"
icon = "💪"

# Unless you explicitly say in_section = false`
[[pages]]
name = "Not in a section"
in_section = false
