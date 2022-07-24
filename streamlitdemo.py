import streamlit as st

st.title ("this is the app title")
st.write("Tutorial [link](https://www.datacamp.com/tutorial/streamlit#display-texts-with-streamlit)")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.audio("https://actions.google.com/sounds/v1/alarms/medium_bell_ringing_near.ogg")
st.video("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4")
st.image("https://picsum.photos/200/300?random=0")