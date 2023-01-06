import streamlit as st

from app.data import Database


def main():
    st.header("Hello, world")
    render_nav()


def render_nav():
    pages = {
        "Home": render_home,
        "About": render_about,
        "Contact": render_contact,
    }
    choice = st.sidebar.radio("Nav", pages.keys())
    render_func = pages.get(choice)
    render_func()


def render_home():
    st.subheader("Home")
    st.write("""
    - One
    - Two
    - Three
    """)


def render_about():
    st.subheader("About")


def render_contact():
    st.subheader("Contact")
    db = Database()
    df = db.dataframe()
    options = df["Type"].unique().tolist()
    options.insert(0, "All Monsters")
    selection = st.selectbox("Filter By Type", options)
    if selection == "All Monsters":
        st.dataframe(df)
    else:
        st.dataframe(df[df["Type"] == selection])


if __name__ == '__main__':
    main()
