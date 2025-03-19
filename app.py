import streamlit as st

# Set page configuration
st.set_page_config(page_title="UPSC Prep Bot", layout="wide")

# Page Labels
PAGE_HOME = "🏠 Home"
PAGE_PRACTICE = "📄 Practice Papers"
PAGE_DISCUSSION = "💬 Discussion Q&A"
PAGE_AFFAIRS = "📰 Current Affairs"
PAGE_JOBS = "📌 Govt. Job Openings"

# Function to display homepage with larger tiles
def show_home():
    st.title("🧠 UPSC Preparation Bot")
    st.markdown("Welcome to **UPSC Prep Hub** – Your all-in-one resource for UPSC preparation. Explore the following sections:")

    col1, col2 = st.columns(2)

    if col1.button(PAGE_PRACTICE, use_container_width=True):
        st.session_state.page = PAGE_PRACTICE
        st.rerun()

    if col2.button(PAGE_DISCUSSION, use_container_width=True):
        st.session_state.page = PAGE_DISCUSSION
        st.rerun()

    if col1.button(PAGE_AFFAIRS, use_container_width=True):
        st.session_state.page = PAGE_AFFAIRS
        st.rerun()

    if col2.button(PAGE_JOBS, use_container_width=True):
        st.session_state.page = PAGE_JOBS
        st.rerun()

# Sidebar Navigation
def navigation_menu():
    st.sidebar.title("📌 Navigation")
    options = [PAGE_HOME, PAGE_PRACTICE, PAGE_DISCUSSION, PAGE_AFFAIRS, PAGE_JOBS]
    choice = st.sidebar.radio("", options, index=options.index(st.session_state.page), label_visibility='collapsed')

    if choice != st.session_state.page:
        st.session_state.page = choice
        st.rerun()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = PAGE_HOME

# Display navigation and content
navigation_menu()

# Page Handling
if st.session_state.page == PAGE_HOME:
    show_home()
elif st.session_state.page == PAGE_PRACTICE:
    from pages.practice_papers import show_practice_papers
    show_practice_papers()
elif st.session_state.page == PAGE_DISCUSSION:
    from pages.discussion_qa import show_discussion_qa
    show_discussion_qa()
elif st.session_state.page == PAGE_AFFAIRS:
    from pages.current_affairs import show_current_affairs
    show_current_affairs()
elif st.session_state.page == PAGE_JOBS:
    from pages.govt_jobs import show_govt_jobs
    show_govt_jobs()
