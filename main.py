import streamlit as st
import random

# 🧁 페이지 설정
st.set_page_config(
    page_title="오늘 저녁 뭐 먹지? 🍽️",
    page_icon="🍜",
    layout="centered"
)

# 🎀 타이틀
st.markdown(
    """
    <h1 style='text-align: center; color: #ff9966;'>오늘 저녁 뭐 먹지? 🍽️💭</h1>
    <h4 style='text-align: center; color: #666;'>고민은 이제 그만! 버튼을 누르면 메뉴가 딱! 🍱✨</h4>
    <br>
    """,
    unsafe_allow_html=True
)

# 🍛 메뉴 리스트
menus = {
    "한식 🇰🇷": ["김치찌개 🍲", "불고기 🍖", "비빔밥 🥘", "삼겹살 🐷", "된장찌개 🫕", "제육볶음 🌶️"],
    "중식 🇨🇳": ["짜장면 🍜", "짬뽕 🌶️", "탕수육 🍖", "마라탕 🔥", "꿔바로우 🥢"],
    "일식 🇯🇵": ["초밥 🍣", "우동 🍲", "돈카츠 🍱", "규동 🐮", "라멘 🍜"],
    "양식 🇺🇸": ["피자 🍕", "스테이크 🥩", "파스타 🍝", "버거 🍔", "치킨 윙 🍗"],
    "분식 🎈": ["떡볶이 🌶️", "순대 🍢", "김밥 🍙", "라볶이 🍜", "오뎅 🍢"]
}

# 🌍 카테고리 선택
category = st.selectbox("먹고 싶은 음식 스타일을 골라보세요! 😋", list(menus.keys()))

# 🍽️ 추천 버튼
if st.button("✨ 저녁 메뉴 추천 받기! ✨"):
    selected_menu = random.choice(menus[category])
    st.markdown(
        f"""
        <h2 style='text-align: center; color: #ff6699;'>오늘의 추천 메뉴는...!</h2>
        <h1 style='text-align: center; font-size: 60px;'>🎉 {selected_menu} 🎉</h1>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown("<p style='text-align: center; color: #aaa;'>👇 카테고리를 선택하고 버튼을 눌러보세요!</p>", unsafe_allow_html=True)

# 🐾 푸터
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #bbb;'>Made with 🍣 by ChatGPT</div>",
    unsafe_allow_html=True
)
