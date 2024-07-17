import streamlit as st
import json

try:
    html_str = f"""
    <style>
    p.a {{
      font: bold 25px Courier;
    }}
    </style>
    <p class="a">Tem {len(st.session_state['questoes'])} questões</p>
    """    
    st.markdown(html_str, unsafe_allow_html=True)
    json_data = json.dumps(st.session_state['questoes'], indent=4)
    st.download_button(label="Baixar JSON", data=json_data, file_name="dados.json",
                       mime="application/json")
    st.json(st.session_state['questoes'])
    st.markdown(html_str, unsafe_allow_html=True)
except:
    st.warning('Nenhum dado por enquanto')

