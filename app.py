import os
from dotenv import load_dotenv
import streamlit as st
import openai

# .env dosyasını yükle
load_dotenv()

# API Anahtarını .env dosyasından al
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("⚠ API anahtarı bulunamadı! `.env` dosyasında tanımladığından emin ol.")
    st.stop()

openai.api_key = OPENAI_API_KEY

# Chatbot Başlığı
st.title("📚 AI Destekli Kelime Öğrenme Chatbotu")

user_input = st.text_input("Bir kelime veya anlamını öğrenmek istediğin bir şey sor:")

if st.button("Gönder") and user_input:
    with st.spinner("Yanıt alınıyor..."):
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "Sen bir kelime öğrenme koçusun, kelimeleri açıkla ve örnekler ver."},
                      {"role": "user", "content": user_input}]
        )
        chatbot_response = response["choices"][0]["message"]["content"]

    st.write("### 🤖 Bot'un Yanıtı")
    st.write(chatbot_response)
