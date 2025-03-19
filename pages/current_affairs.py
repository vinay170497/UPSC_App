import streamlit as st
from utils.api_fetch import fetch_current_affairs

def show_current_affairs():
    st.title("📰 Current Affairs Analysis")
    st.write("Latest News Related to Governance and Policy:")

    if st.button("Fetch Latest News"):
        news_list = fetch_current_affairs()
        for news in news_list:
            st.markdown(f"🔗 [{news['title']}]({news['url']})")
