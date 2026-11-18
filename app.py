import streamlit as st
from database.init_db import criar_banco
criar_banco()
if "logado" not in st.session_state: st.session_state.logado=False
if not st.session_state.logado:
 st.title("💇 SalonPro")
 u=st.text_input("Usuário"); s=st.text_input("Senha",type="password")
 if st.button("Entrar") and u=="admin" and s=="123456": st.session_state.logado=True; st.rerun()
else:
 st.set_page_config(page_title="SalonPro",layout="wide")
 st.title("💇 SalonPro Dashboard")
 st.success("Sistema carregado")
