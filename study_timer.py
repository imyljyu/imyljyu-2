import streamlit as st
import time
import pandas as pd
import altair as alt


def render_study_timer():
    if "start" not in st.session_state:
        st.session_state.start = None
    if "records" not in st.session_state:
        st.session_state.records = []

    toggle_label = "종료" if st.session_state.start else "시작"
    status_text = "⏳ 타이머 실행 중" if st.session_state.start else "🛑 대기 중 - 시작을 눌러주세요"

    st.markdown(
        """
        <style>
        .alarm-clock {
            width: 300px;
            height: 300px;
            margin: 30px auto;
            position: relative;
            border: 8px solid #ff4b4b;
            border-radius: 50%;
            background: linear-gradient(135deg, #fff5f5, #ffe0e0);
            box-shadow: 0 8px 22px rgba(0,0,0,0.25);
        }
        .alarm-clock::before,
        .alarm-clock::after {
            content: "";
            position: absolute;
            width: 80px;
            height: 60px;
            border: 8px solid #ff4b4b;
            border-radius: 50% 50% 0 0;
            top: -38px;
            background: #fff;
        }
        .alarm-clock::before { left: 28px; transform: rotate(-25deg); }
        .alarm-clock::after { right: 28px; transform: rotate(25deg); }
        .alarm-clock .clock-face {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 220px;
            height: 220px;
            border: 6px solid #ff4b4b;
            border-radius: 50%;
            background: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .alarm-clock .clock-face .button-container {
            position: relative;
            width: 140px;
            height: 70px;
        }
        .alarm-clock .clock-face .button-container .stButton>button {
            background-color: #ff4b4b !important;
            color: white !important;
            font-weight: bold;
            font-size: 1.25rem;
            width: 140px;
            height: 70px;
            border-radius: 999px;
        }
        .status-text {
            text-align: center;
            margin-top: 15px;
            font-size: 1.25rem;
            font-weight: 600;
        }
        </style>

        <div class="alarm-clock">
            <div class="clock-face">
                <div class="button-container"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    button_container = st.button(toggle_label, key="toggle_timer")
    st.markdown(f"<div class='status-text'>{status_text}</div>", unsafe_allow_html=True)

    if button_container:
        if st.session_state.start:
            duration = int(time.time() - st.session_state.start)
            st.session_state.records.append(duration)
            st.session_state.start = None
            st.success(f"{duration}초 공부 완료")
        else:
            st.session_state.start = time.time()
            st.info("공부 시작")

    st.write("### 기록")
    total = sum(st.session_state.records)
    st.write(f"총 공부 시간: {total}초")

    if st.session_state.records:
        df_records = pd.DataFrame({
            "회차": range(1, len(st.session_state.records) + 1),
            "공부 시간(초)": st.session_state.records,
        })
        df_records["공부 시간(분)"] = (df_records["공부 시간(초)"] / 60).round(2)
        df_records["누적 시간(초)"] = df_records["공부 시간(초)"].cumsum()
        df_records["누적 시간(분)"] = (df_records["누적 시간(초)"] / 60).round(2)

        st.table(df_records)

        progress_chart = alt.Chart(df_records).mark_line(point=True).encode(
            x=alt.X("회차:O", title="회차"),
            y=alt.Y("공부 시간(분):Q", title="공부 시간(분)"),
            tooltip=["회차", "공부 시간(초)", "공부 시간(분)", "누적 시간(분)"]
        ).properties(width=700, height=350)

        st.altair_chart(progress_chart, use_container_width=True)
    else:
        st.write("아직 기록이 없습니다. 타이머를 시작해보세요.")
