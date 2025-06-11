import streamlit as st

# 🎨 설정
st.set_page_config(
    page_title="MBTI 진로 추천기 💼✨",
    page_icon="🧭",
    layout="centered",
)

# 💖 타이틀 & 설명
st.markdown(
    """
    <h1 style='text-align: center; color: #ff66cc;'>MBTI로 보는 나의 미래 직업 💼✨</h1>
    <h4 style='text-align: center; color: #666;'>당신의 성격에 딱 맞는 직업을 추천해드릴게요! 🧠🌟</h4>
    <br>
    """,
    unsafe_allow_html=True
)

# 🎯 MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 🔮 MBTI별 직업 추천 데이터
career_recommendations = {
    "INTJ": ["데이터 과학자 📊", "전략 컨설턴트 🧠", "소프트웨어 엔지니어 💻"],
    "INTP": ["AI 연구원 🤖", "철학자 📚", "기술 컨설턴트 💡"],
    "ENTJ": ["CEO 🧑‍💼", "프로덕트 매니저 📈", "정치가 🗳️"],
    "ENTP": ["창업가 🚀", "마케팅 전문가 📣", "기획자 🗂️"],
    "INFJ": ["상담가 💬", "심리학자 🧠", "작가 ✍️"],
    "INFP": ["예술가 🎨", "시인 📖", "사회운동가 ✊"],
    "ENFJ": ["교사 🍎", "HR매니저 👥", "정신과 의사 🧑‍⚕️"],
    "ENFP": ["디자이너 🎨", "콘텐츠 크리에이터 📸", "이벤트 플래너 🎉"],
    "ISTJ": ["회계사 📑", "경찰 👮", "엔지니어 ⚙️"],
    "ISFJ": ["간호사 🏥", "도서관 사서 📚", "초등학교 교사 🏫"],
    "ESTJ": ["프로젝트 매니저 🗂️", "공무원 🏛️", "군인 🎖️"],
    "ESFJ": ["간호조무사 👩‍⚕️", "상담교사 🧑‍🏫", "이벤트 코디네이터 🎈"],
    "ISTP": ["기술자 🔧", "파일럿 ✈️", "응급 구조사 🚑"],
    "ISFP": ["패션 디자이너 👗", "사진작가 📷", "요리사 🍳"],
    "ESTP": ["영업사원 📞", "스턴트맨 🤸", "리포터 🎤"],
    "ESFP": ["연예인 🌟", "방송인 🎬", "무대 감독 🎭"]
}

# 🎈 선택 위젯
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 🔍", mbti_types)

# 🎉 결과 표시
if selected_mbti:
    st.markdown(f"## {selected_mbti} 유형의 추천 직업 🎯")
    for job in career_recommendations[selected_mbti]:
        st.markdown(f"- {job}")
    
    st.markdown(
        """
        <br>
        <h5 style='text-align: center; color: #888;'>✨ 당신의 MBTI는 놀라운 잠재력을 가지고 있어요! ✨</h5>
        """,
        unsafe_allow_html=True
    )

# 🌈 푸터
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #bbb;'>Made with ❤️ by ChatGPT</div>",
    unsafe_allow_html=True
)
