# streamlit_app.py
import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 직업 추천기 ✨",
    page_icon="🧠",
    layout="centered"
)

# 🎨 스타일 적용
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        text-align: center;
        color: #FF6EC7;
        font-weight: bold;
    }
    .subtitle {
        font-size: 24px;
        text-align: center;
        color: #6A5ACD;
    }
    .job-box {
        background-color: #FFF0F5;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        border: 2px solid #FFB6C1;
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 타이틀
st.markdown('<div class="title">🔮 MBTI로 알아보는 나의 미래 직업 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격 유형을 선택하고, 어울리는 직업을 찾아보세요! 🚀</div>', unsafe_allow_html=True)

# 📊 MBTI 리스트
mbti_list = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", mbti_list)

# 💼 직업 추천 데이터
job_recommendations = {
    "INTJ": ("🔬 데이터 과학자", "분석적이고 전략적인 성향을 살려 복잡한 문제를 해결하는 일을 좋아합니다."),
    "INFP": ("🎨 작가 / 예술가", "상상력과 감수성이 풍부하여 창의적인 작업에 적합합니다."),
    "ENFP": ("🧑‍🏫 교육자 / 퍼실리테이터", "사람들과의 소통을 즐기고 영감을 주는 일에 탁월합니다."),
    "ISTJ": ("📊 회계사 / 관리자", "체계적이고 신중하며 신뢰할 수 있는 업무에 강합니다."),
    "ESFP": ("🎤 엔터테이너 / 이벤트 플래너", "즐거움을 주고 현장을 이끄는 능력이 뛰어납니다."),
    # ... 다른 유형들도 추가 가능
}

# 결과 보여주기
if mbti in job_recommendations:
    job, desc = job_recommendations[mbti]
    st.markdown(f"""
        <div class="job-box">
            <h2>{job}</h2>
            <p>{desc}</p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ 해당 MBTI에 대한 추천 정보가 아직 없습니다. 업데이트를 기다려 주세요!")

# 🎁 추가 기능 아이디어
st.markdown("💡 **팁:** 친구들과 공유하고 서로의 MBTI를 비교해보세요! 😊")

# 📌 푸터
st.markdown("---")
st.markdown("Made with ❤️ by [당신의 이름] · © 2025 CareerMatch")
