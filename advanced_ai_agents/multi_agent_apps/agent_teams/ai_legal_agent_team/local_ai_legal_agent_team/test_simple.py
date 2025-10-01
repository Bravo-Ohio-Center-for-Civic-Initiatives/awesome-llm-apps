import streamlit as st
import time

st.title("🧪 Simple Test App")
st.write("If you can see this, Streamlit is working!")

# Test button
if st.button("Test Connection"):
    with st.spinner("Testing..."):
        time.sleep(2)
    st.success("✅ Connection test successful!")

st.write("Current time:", time.strftime("%Y-%m-%d %H:%M:%S"))