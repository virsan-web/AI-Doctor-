import streamlit as st
from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile",
               temperature=0.5,
               api_key="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")
st.title('!!!AI DOCTOR!!!')
age=st.text_input('Enter Age')


gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)
st.write("Selected Gender:", gender)

symptoms = st.multiselect(
    "Choose symptoms",
    ["Fever","Cough","Cold","Headache","Sore Throat","Fatigue","Body Pain","Nausea","Vomiting","Diarrhea","Stomach Pain","Chest Pain","Shortness of Breath","Dizziness","Loss of Appetite","Weight Loss","Muscle Weakness","Joint Pain","Skin Rash", "Itching","Eye Redness","Blurred Vision","Runny Nose","Sneezing","Back Pain"])



duration = st.selectbox(
    "When did the symptoms start?",
    ["Today", "Yesterday", "2–3 days ago", "1 week ago", "More than 1 week"]
)
st.write("Symptoms started:", duration)

if st.button("Submit"):
    prompt='''Act like a expert doctor . I will givee you patients deatils like age,gender,symtoms and duration.you have to recommend the list of medicines along with proper dosage.
    Dont provide any extra information. Only provide list of medicines with dosage.
    Age:{} years 
    gender:{} 
    Symptoms:{} 
    Duration:{} '''.format(age,gender,symptoms,duration)
    print("PROMPT",prompt)
    response= llm.invoke(prompt)
    st.write(response.content)
