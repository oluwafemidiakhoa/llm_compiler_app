import streamlit as st
from utils import generate_code, optimize_code, correct_code, explain_code

st.title("LLM Compiler App")

st.header("Code Generation")
description = st.text_area("Describe what you want to code")
language = st.selectbox("Select programming language", ["Python", "JavaScript", "Java"])
if st.button("Generate Code"):
    code = generate_code(description, language)
    st.code(code, language.lower())

st.header("Code Optimization")
code_to_optimize = st.text_area("Code to optimize")
if st.button("Optimize Code"):
    optimized_code = optimize_code(code_to_optimize, language)
    st.code(optimized_code, language.lower())

st.header("Error Detection and Correction")
code_to_correct = st.text_area("Code to correct")
if st.button("Correct Code"):
    corrected_code = correct_code(code_to_correct, language)
    st.code(corrected_code, language.lower())

st.header("Code Explanation")
code_to_explain = st.text_area("Code to explain")
if st.button("Explain Code"):
    explanation = explain_code(code_to_explain, language)
    st.text(explanation)
