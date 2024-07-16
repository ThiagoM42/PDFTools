import streamlit as st
import json

try:
    json_data = json.dumps(st.session_state['questoes'], indent=4)
    st.download_button(label="Baixar JSON", data=json_data, file_name="dados.json",
                       mime="application/json")
    st.json(st.session_state['questoes'])
except:
    st.warning('Nenhum dado por enquanto')

