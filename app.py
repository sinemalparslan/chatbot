import openai
import streamlit as st

# OpenAI API Anahtarını Buraya Yaz
OPENAI_API_KEY = "your-api-key"  # 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

openai.api_key = OPENAI_API_KEY

# Chatbot Başlığı
st.title("📚 AI Destekli Kelime Öğrenme Chatbotu")

# Kullanıcıdan giriş alma
user_input = st.text_input("Bir kelime veya anlamını öğrenmek istediğin bir şey sor:")

if st.button("Gönder") and user_input:
    with st.spinner("Yanıt alınıyor..."):
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Sen bir kelime öğrenme koçusun, kelimeleri açıkla ve örnekler ver."},
                {"role": "user", "content": user_input}
            ]
        )
        chatbot_response = response["choices"][0]["message"]["content"]

    st.write("### 🤖 Bot'un Yanıtı")
    st.write(chatbot_response)
