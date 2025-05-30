import streamlit as st
from transformers import pipeline

# Page config
st.set_page_config(page_title="Text Summarizer", page_icon="🧠", layout="wide")

# Glassmorphism theme CSS with color adjustments
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #c3ecf7 0%, #e2e2e2 100%);
        background-attachment: fixed;
        padding: 2rem;
        min-height: 100vh;
    }

    /* Title style with deep navy blue */
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 900;
        color: #1a237e;  /* Deep navy blue */
        text-shadow: 1px 1px 4px rgba(0,0,0,0.15);
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #333;
        margin-bottom: 30px;
    }

    /* Stylish output summary container with navy border & shadow */
    .summary-box {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 25px;
        margin-top: 25px;
        color: #1a237e;  /* text color navy */
        font-size: 18px;
        line-height: 1.7;
        box-shadow: 0 12px 24px rgba(26, 35, 126, 0.3); /* navy shadow */
        border: 2px solid #1a237e;
        transition: box-shadow 0.3s ease-in-out;
    }
    .summary-box:hover {
        box-shadow: 0 16px 36px rgba(26, 35, 126, 0.6);
    }

    /* File uploader container styling */
    .upload-box {
        border: 2px dashed rgba(26, 35, 126, 0.4);
        border-radius: 10px;
        padding: 10px;
        background-color: rgba(26, 35, 126, 0.1);
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="weijiahaha/t5-small-summarization")

summarizer = load_model()

# Title and subtitle
st.markdown('<div class="title">📝 Text Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Summarize long English content with one click using AI</div>', unsafe_allow_html=True)

# Input and file upload
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### ✍️ Enter Text")
        input_text = st.text_area("Write or paste the content below:", height=250)

    with col2:
        st.markdown("#### 📂 Upload a Text File")
        uploaded_file = st.file_uploader("Upload a `.txt` file", type=["txt"], label_visibility="collapsed")
        if uploaded_file is not None:
            input_text = uploaded_file.read().decode("utf-8")

# Summarize button and output
if st.button("🔍 Generate Summary"):
    if input_text.strip():
        with st.spinner("Summarizing..."):
            formatted_input = "summarize: " + input_text.strip()
            summary = summarizer(formatted_input, max_length=130, min_length=30, do_sample=False)

            st.markdown("### 🧾 Summary:")
            st.markdown(f'<div class="summary-box">{summary[0]["summary_text"]}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter or upload some text to summarize.")