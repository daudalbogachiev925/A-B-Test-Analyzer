import streamlit as st
from analyzer import ABResult

st.title("🧪 A/B Test Analyzer")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Control")
    cc = st.number_input("Конверсии (A)", 0, value=100)
    ct = st.number_input("Всего (A)", 1, value=1000)
with c2:
    st.subheader("Variant")
    vc = st.number_input("Конверсии (B)", 0, value=130)
    vt = st.number_input("Всего (B)", 1, value=1000)

r = ABResult(cc, ct, vc, vt)
st.metric("Конверсия A", f"{r.p_control*100:.2f}%")
st.metric("Конверсия B", f"{r.p_variant*100:.2f}%")
st.metric("Uplift", f"{r.uplift*100:.2f}%")
st.metric("p-value", f"{r.p_value:.5f}")
st.metric("Значимо (α=0.05)", "✅ Да" if r.significant else "❌ Нет")
