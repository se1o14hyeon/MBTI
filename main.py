import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 직업 추천기 ✨",
    page_icon="🧠",
    layout="centered"
)

# 🎨 스타일
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

# 타이틀
st.markdown('<div class="title">🔮 MBTI로 알아보는 나의 미래 직업 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격 유형을 선택하고, 어울리는 직업과 유명인을 알아보세요! 🚀</div>', unsafe_allow_html=True)

# MBTI 리스트
mbti_list = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", mbti_list)

# 💼 직업 추천 및 유명인
mbti_data = {
    "INTJ": {
        "jobs": ["📈 전략 컨설턴트", "🧠 데이터 과학자", "🧪 연구개발자"],
        "desc": "논리적 사고와 장기 계획 수립에 능해 복잡한 문제 해결에 탁월합니다.",
        "celebrity": "엘론 머스크 (Elon Musk)"
    },
    "INTP": {
        "jobs": ["🔬 이론 물리학자", "🧑‍💻 소프트웨어 개발자", "📚 철학자"],
        "desc": "호기심이 많고 창의적이며 독립적으로 문제를 해결하는 걸 선호합니다.",
        "celebrity": "알버트 아인슈타인 (Albert Einstein)"
    },
    "ENTJ": {
        "jobs": ["💼 CEO", "📊 사업 전략가", "🎯 프로젝트 매니저"],
        "desc": "리더십이 강하고 효율성을 중시하며 조직을 이끄는 데 적합합니다.",
        "celebrity": "마거릿 대처 (Margaret Thatcher)"
    },
    "ENTP": {
        "jobs": ["🚀 창업가", "🗣️ 마케팅 전략가", "🎤 방송인"],
        "desc": "새로운 아이디어와 변화를 좋아하며 토론과 혁신에 능합니다.",
        "celebrity": "로버트 다우니 주니어 (Robert Downey Jr.)"
    },
    "INFJ": {
        "jobs": ["🧘 심리상담가", "📖 작가", "🌿 사회운동가"],
        "desc": "깊은 통찰력과 공감 능력으로 타인을 돕는 데 보람을 느낍니다.",
        "celebrity": "마틴 루터 킹 주니어 (Martin Luther King Jr.)"
    },
    "INFP": {
        "jobs": ["🎨 일러스트레이터", "✍️ 시나리오 작가", "🎼 뮤지션"],
        "desc": "감수성이 풍부하고 내면 세계가 깊어 창작 분야에 적합합니다.",
        "celebrity": "윌리엄 셰익스피어 (William Shakespeare)"
    },
    "ENFJ": {
        "jobs": ["🧑‍🏫 교육자", "🧭 커뮤니케이션 디렉터", "💖 NGO 활동가"],
        "desc": "타인을 돕고 조화를 이끄는 데 강점을 가지며 자연스러운 리더입니다.",
        "celebrity": "바락 오바마 (Barack Obama)"
    },
    "ENFP": {
        "jobs": ["🎤 퍼포머", "📣 브랜드 마케터", "🧑‍🎤 콘텐츠 크리에이터"],
        "desc": "열정적이고 상상력이 풍부하여 자유로운 환경에서 빛을 발합니다.",
        "celebrity": "로빈 윌리엄스 (Robin Williams)"
    },
    "ISTJ": {
        "jobs": ["📊 회계사", "📂 공무원", "⚖️ 법무 담당자"],
        "desc": "신뢰할 수 있고 체계적인 업무 수행에 탁월합니다.",
        "celebrity": "조지 워싱턴 (George Washington)"
    },
    "ISFJ": {
        "jobs": ["🏥 간호사", "👩‍👧‍👦 사회복지사", "📚 사서"],
        "desc": "헌신적이고 성실하며 타인을 돕는 데에서 만족을 느낍니다.",
        "celebrity": "비욘세 (Beyoncé)"
    },
    "ESTJ": {
        "jobs": ["🛠️ 관리자", "📦 운영 책임자", "🚓 경찰"],
        "desc": "조직 내에서 질서와 효율을 유지하는 데 탁월합니다.",
        "celebrity": "미셸 오바마 (Michelle Obama)"
    },
    "ESFJ": {
        "jobs": ["🍽️ 호텔 매니저", "👩‍🏫 교사", "💐 이벤트 코디네이터"],
        "desc": "사람들과 잘 어울리고 친절하며 봉사 정신이 뛰어납니다.",
        "celebrity": "테일러 스위프트 (Taylor Swift)"
    },
    "ISTP": {
        "jobs": ["🔧 자동차 정비사", "🧰 엔지니어", "🏍️ 레이서"],
        "desc": "실용적이고 분석적인 성격으로 문제 해결에 집중합니다.",
        "celebrity": "클린트 이스트우드 (Clint Eastwood)"
    },
    "ISFP": {
        "jobs": ["📷 포토그래퍼", "🎨 패션 디자이너", "🌺 플로리스트"],
        "desc": "예술적 감각이 뛰어나고 감성적으로 일에 몰입합니다.",
        "celebrity": "마이클 잭슨 (Michael Jackson)"
    },
    "ESTP": {
        "jobs": ["📈 세일즈 전문가", "🚑 응급 구조사", "🎲 이벤트 프로듀서"],
        "desc": "도전과 즉흥적 상황에 강하고 에너지가 넘칩니다.",
        "celebrity": "어니스트 헤밍웨이 (Ernest Hemingway)"
    },
    "ESFP": {
        "jobs": ["🎬 배우", "🎉 파티 플래너", "🧚 공연 연출가"],
        "desc": "사람들과 어울리며 즐거움을 주는 일에 적합합니다.",
        "celebrity": "마일리 사이러스 (Miley Cyrus)"
    }
}

# 결과 출력
if mbti in mbti_data:
    data = mbti_data[mbti]
    st.markdown(f"""
        <div class="job-box">
            <h2>🌟 추천 직업 3가지</h2>
            <ul>
                <li>{data["jobs"][0]}</li>
                <li>{data["jobs"][1]}</li>
                <li>{data["jobs"][2]}</li>
            </ul>
            <p>📝 <strong>설명:</strong> {data["desc"]}</p>
            <p>🌍 <strong>유명인물:</strong> {data["celebrity"]}</p>
        </div>
    """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("🎁 친구들과 공유해서 서로의 MBTI를 비교해보세요!")
st.markdown("Made with ❤️ by [당신의 이름] · © 2025 CareerMatch")
