
import streamlit as st
import requests
from log_analyzer import analyze_log

# App title
st.title("Log Analyzer")
st.write("Upload a log file to check for errors.")

# Ollama settings
model = "llama3.2"
ollama_url = "http://localhost:11434"

# Show Ollama connection status in the sidebar
st.sidebar.header("Ollama Connection")

try:
    response = requests.get(ollama_url, timeout=3)

    if response.status_code == 200:
        st.sidebar.success("Connected to Ollama")
    else:
        st.sidebar.error("Ollama is not responding")

except requests.RequestException:
    st.sidebar.error("Ollama is not connected")

st.sidebar.write("Model:", model)

# Upload a log file
file = st.file_uploader("Choose a log file")

if file is not None:
    # Read the uploaded file
    log = file.getvalue().decode("utf-8", errors="replace")

    st.write("File:", file.name)
    st.write("Total lines:", len(log.splitlines()))

    # Analyze the log when the button is clicked
    if st.button("Analyze Log"):
        try:
            # Analyze only the first 100 lines for faster testing
            short_log = "\n".join(log.splitlines()[:100])

            with st.spinner("Analyzing the first 100 lines... This may take a minute."):
                result = analyze_log(
                    short_log,
                    file.name,
                    model,
                    ollama_url
                )

            st.subheader("Analysis Result")
            st.markdown(result)

            st.info("For now, only the first 100 lines were analyzed.")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
