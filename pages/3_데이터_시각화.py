import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import altair as alt

# 한글 폰트 경로: fonts/NotoSansKR-Bold.ttf
FONT_PATH = Path(__file__).resolve().parents[1] / "fonts" / "NotoSansKR-Bold.ttf"
FONT_URI = FONT_PATH.as_uri()

st.markdown(
    f"""
    <style>
    @font-face {{
        font-family: 'NotoSansKR';
        src: url('{FONT_URI}') format('truetype');
        font-weight: bold;
        font-style: normal;
    }}
    html, body, [class*='css'] {{
        font-family: 'NotoSansKR', sans-serif;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Altair 테마 등록
alt.themes.register('noto_ks', lambda: {
    'config': {
        'title': {'font': 'NotoSansKR', 'fontSize': 20},
        'axis': {'labelFont': 'NotoSansKR', 'titleFont': 'NotoSansKR'},
        'legend': {'labelFont': 'NotoSansKR', 'titleFont': 'NotoSansKR'},
    }
})
alt.themes.enable('noto_ks')

st.set_page_config(page_title="데이터 시각화", page_icon="📊", layout="wide")

st.title("📊 데이터 시각화 샘플")
st.write("모든 표와 그래프는 한국어 레이블로 표시됩니다.")

# 예시 데이터프레임 생성
data = {
    "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
    "매출": [120, 150, 170, 130, 180, 200],
    "비용": [80, 90, 100, 85, 95, 110],
    "고객수": [30, 35, 40, 37, 45, 50],
}

df = pd.DataFrame(data)

st.header("1. 기본 표")
st.dataframe(df)

st.header("2. 매출 vs 비용 추세")
chart_data = df.set_index("월")[['매출', '비용']]
st.line_chart(chart_data)

st.header("3. 월별 매출 파이 차트")
pie_data = df.set_index("월")['매출']
st.write("월별 매출 점유율")

# Altair 기반 파이 차트 (matplotlib 불필요)
import altair as alt
pie_df = pie_data.reset_index().rename(columns={"매출": "값"})
pie_chart = alt.Chart(pie_df).mark_arc().encode(
    theta=alt.Theta(field="값", type="quantitative"),
    color=alt.Color(field="월", type="nominal", title="월"),
    tooltip=[alt.Tooltip("월", title="월"), alt.Tooltip("값", title="매출")]
).properties(width=600, height=400)

st.altair_chart(pie_chart, use_container_width=True)

st.header("4. 고객수 막대 그래프")
bar_data = df.set_index("월")['고객수']
st.bar_chart(bar_data)

st.header("5. 데이터 요약 통계")
st.table(df.describe().rename(columns={
    "매출": "매출(요약)",
    "비용": "비용(요약)",
    "고객수": "고객수(요약)"
}))

st.success("✅ 한글 표와 그래프 시각화 예시가 완료되었습니다.")
