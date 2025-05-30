import streamlit as st
import google.generativeai as genai
import os

# Gemini API 설정
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Gemini 응답 생성 함수
def get_gemini_response(prompt):
    try:
        # gemini-1.5-flash 모델 설정
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

# 페이지 설정
st.set_page_config(
    page_title="Gemini 챗봇",
    page_icon="💬",
    layout="wide"
)

# 제목
st.title("💬 Gemini 챗봇")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 채팅 입력
user_input = st.chat_input("메시지를 입력하세요...")

# 대화 기록 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if user_input:
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # AI 응답 생성 및 표시
    with st.chat_message("assistant"):
        response = get_gemini_response(user_input)
        st.markdown(response)
        
        # AI 응답을 대화 기록에 추가
        st.session_state.messages.append({"role": "assistant", "content": response}) 
