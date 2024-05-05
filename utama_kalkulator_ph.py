import streamlit as st
st.title("Kalkulator pH Larutan Asam")

from st_pages import show_pages_from_config

show_pages_from_config()
[[pages]]
path = "example_app/streamlit_app.py"
name = "Home"
icon = ":house:"

[[pages]]
path = "example_app/example_one.py"
name = "Example One"
icon = ":books:"

[[pages]]
path = "example_app/example_four.py"
name = "Example Four"
icon = "📖"

[[pages]]
path = "example_app/example_two.py"
name = "Example Two"
icon = "✏️"

[[pages]]
path = "example_app/example_three.py"

[[pages]]
path = "example_app/example_five.py"
name = "Example Five"
icon = "🧰"
