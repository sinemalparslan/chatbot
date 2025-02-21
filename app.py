import streamlit as st
import openai

# OpenAI API Anahtarını Gir
OPENAI_API_KEY = "sk-svcacct-cNvYpKZhEOgEjziNwJ_It3hIIUBPDIh-Koem_6q2s2DgmqCIn0Pnxx780iYnQSJT3BlbkFJaLmDnh1vtMN2ck1Iw9U7RhhsrYy4s-3XLT724KK5kFHnux4nLJ1s_62m0dWpRAA"  # Buraya OpenAI API anahtarını ekleyin

client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Streamlit Başlığı
st.title("📝 Busy Bee Vocabulary Coach")

# Kullanıcıdan mesaj alma kutusu
user_input = st.text_input("Bir kelime veya anlamını öğrenmek istediğin bir şey sor:")

# Sohbet geçmişini saklama
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Mesaj boş değilse GPT'ye gönder
if st.button("Gönder") and user_input:
    with st.spinner("Yanıt alınıyor..."):
        response = client.chat.completions.create(
            model="gpt-4-turbo",  # Yeni OpenAI API formatı
            messages=[
                {"role": "system", "content": "Sen bir kelime öğrenme koçusun, kelimeleri açıkla ve örnekler ver."},
                {"role": "user", "content": user_input}
            ]
        )
        chatbot_response = response.choices[0].message.content

    st.success("Cevap alındı!")
    st.write(chatbot_response)

    # Sohbet geçmişine ekle
    st.session_state.chat_history.append(f"**Sen:** {user_input}")
    st.session_state.chat_history.append(f"**Bot:** {chatbot_response}")

# Sohbet geçmişini göster
st.write("### 📜 Sohbet Geçmişi")
for chat in st.session_state.chat_history:
    st.write(chat)
