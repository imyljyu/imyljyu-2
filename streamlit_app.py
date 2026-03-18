import streamlit as st
from study_timer import render_study_timer

# =========================
# Personal introduction page
# =========================

st.set_page_config(
    page_title="자기소개 페이지", 
    page_icon="👋", 
    layout="centered"
)

st.title("👋 자기소개 페이지")
st.markdown("여기에 자기소개를 작성하세요. 아래 섹션을 채워주세요.")

# 1. 기본 정보
st.header("1. 기본 정보")
name = st.text_input("이름", "홍길동")
role = st.text_input("현재 역할/직무", "예: 데이터 분석가")
location = st.text_input("위치(선택)", "예: 서울")

# 2. 한 줄 소개
st.header("2. 한 줄 소개")
summary = st.text_area("한 줄로 나를 소개하는 문장", "# 여기에 작성")

# 3. 경력/경험
st.header("3. 주요 경력 · 경험")
st.write("- 회사/기관 1: 역할, 기간, 핵심 성과")
st.write("- 회사/기관 2: 역할, 기간, 핵심 성과")

# 4. 기술 스택
st.header("4. 기술 스택")
st.write("- 프로그래밍: Python, JavaScript, ...")
st.write("- 도구/프레임워크: Streamlit, Pandas, ...")

# 5. 목표 및 비전
st.header("5. 목표 및 비전")
goal = st.text_area("향후 목표/비전", "# 여기에 작성")

# 6. 연락처
st.header("6. 연락처")
email = st.text_input("이메일", "example@example.com")
linkedin = st.text_input("LinkedIn/사이트", "https://")

st.markdown("---")

st.header("📚 빠른 학습: 공부 타이머")
st.write("공유 URL로 들어올 때 바로 타이머를 쓰고 싶은 경우 아래 타이머를 사용하세요.")
st.write("또는 상단 메뉴에서 '공부 타이머'에 들어갈 수 있습니다.")
render_study_timer()

st.markdown("---")
st.write("✅ 준비가 완료되면 내용을 저장하고 공유하세요.")
