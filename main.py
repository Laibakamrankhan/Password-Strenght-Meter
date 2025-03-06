import re
import streamlit as st

st.set_page_config(page_title="🔑Password Strenght Meter", layout="centered")
st.markdown("""
<style>
   main {text-align: center;}
   .stTextInput {width: 60%;}
   .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
   .stButton button:hover {background-color: #3e8e41;}
</style>}
""",unsafe_allow_html=True)

st.title("🔐 Password Strenght Meter")
st.write("Enter Your Password to Check it's Strenght. 🔍")

def check_password_strenght(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be 8 character long")
    if re.search(r"[A-Z]" , password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper-case🔠 and lower-case🔡")

    if re.search(r"\d" , password ):
        score += 1
    else:
        feedback.append("❌ Password should alteast one Number")
    if re.search(r"[!@#$%^&*]" , password):
        score += 1
    else:
        feedback.append("❌ Password should contain atleast one special character 🔣")

    if score == 4:
        st.success("🟢 Strong Password...Your Password is secure")
    elif score == 3:
        st.info("🟡 Moderate Password...Need Improvement")
    else:
        st.error("🔴 Password is Week")
    
    if feedback:
        with st.expander("Imporve your Password"):
            for item in feedback:
                st.write(item)
password = st.text_input("🔑 Enter Your Password:" , type="password" , help="Ensure your password is strong")

if st.button("Check Strenght"):
    if password:
        check_password_strenght(password)
    else:
        st.warning("Please enter your password")
       
