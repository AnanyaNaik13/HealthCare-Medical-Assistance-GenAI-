import streamlit as st
from MedicineGen import get_recommendation
 
st.title("Medicine Recommendation System")
 
st.warning("This is general information only, not medical advice. Please consult a doctor.")
 
symptoms = st.text_input("Enter symptoms")
 
if st.button("Get recommendation"):
    if not symptoms:
        st.warning("Please enter your symptoms.")
    else:
        with st.spinner("Thinking..."):
            answer = get_recommendation(symptoms)
 
        st.subheader("Recommendation")
        st.write(answer)