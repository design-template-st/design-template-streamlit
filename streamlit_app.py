
import streamlit as st


pages = {
    "menu": [
        st.Page("pages/00_top.py", title="top"),
        st.Page("pages/01_page.py", title="ページ"),
    ],
}

pg = st.navigation(pages)
pg.run()



