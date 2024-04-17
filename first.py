from bardapi import Bard
import os
import streamlit as st 
from streamlit_chat import message

# thiết lập biến môi trưong
os.environ["_BARD_API_KEY"] = "g.a000fwg1JYY1jBhY9VGCsGCE9jTs3RCiCjlMCzJhaj2nt18Xc9BHUf7SGyL5xFbWRlZttANaLwACgYKAXcSAQASFQHGX2MieMuPJxOI7pd4R3Gdyl_MxxoVAUF8yKrNCnRAm1wfz3zNSDZWkIO90076"
st.title("Han Bao AI")
st.write("Chào mừng đến với trợ lý ảo của Han Bao")

# Lấy dữ liệu từ API
def response_api(promot):
    message=Bard().get_answer(str(promot))['content']
    return message

def user_input():
    input_text = st.text_input("Nhập vào:")
    return input_text

# Lưu trữ và truy cập dữ liệu
if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
    
user_text = user_input()

# cho kết quả vào output, user_text
if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)
    
if st.session_state ['generate']:
    for i in range(len(st.session_state['generate']) -1 , -1 , -1 ):
        message(st.session_state["past"] [i] , is_user=True, key= str(i) + '_user')
        message(st.session_state["generate"] [i], key=str(i) ) 
    
    
# streamlit run first.py