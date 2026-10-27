import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####

st.title("𑣲⋆｡˚ ACHA CEP!")



##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####

st.sidebar.title('˚.⋆꒰১ ACHA CEP - VAMOS ACHAR SEU CEP? ໒꒱⋆.˚')
st.sidebar.image('logo.png')
st.sidebar.write('˚˖𓍢ִ໋❀ Aplicação para buscar endereços a partir do CEP e mostrar a localização no mapa ˚˖𓍢ִ໋❀')
escolha = st.sidebar.selectbox('༘⋆ selecione a opção desejada ༘⋆:', opcoes)


##### BOTÃO BUSCAR CEP #####

if escolha == "Buscar CEP": 
    st.header('˚.⋆꒰১ BUSCAR ENDEREÇO PELO CEP! ໒꒱⋆.˚')
    cep = st.text_input('. ݁⋆ ۶ digite o CEP (somente números!) ৎ ݁˖ . ݁')

    if st.button('Buscar'):
        if len(cep) != 8 or not cep.isdigit():
            st.error('݁⋆ ۶ Por favor, insira um CEP válido com 8 digitos numéricos. ৎ ݁˖ . ݁.')
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success('. ݁⋆ ۶ ENDEREÇO ENCONTRADO ! ৎ ݁˖ . ݁')
                    st.write(f'CEP : {endereco[0]}')
                    st.write(f'Endereço: {endereco[1]}')
                    st.write(f'Bairro: {endereco[2]}')
                    st.write(f'Cidade: {endereco[3]}')
                    st.write(f'Estado: {endereco[4]}')

                    ## MAPAS
                    
                    st.title('˚.⋆꒰১ LOCALIZAÇÃO NO MAPA ໒꒱⋆.˚')
                    df = pd.DataFrame({'latitude': [endereco[5]], 'longitude': [endereco[6]]})
                    st.map(df, zoom=15)
                else:
                    st.error('. ݁⋆ ۶ CEP NÃO ENCONTRADO ! ৎ ݁˖ . ݁')
            except Exception as e:
                st.error(f'. ݁⋆ ۶ OCORREU UM ERRO AO BUSCAR O CEP: {e} ৎ ݁˖ . ݁')

##### BOTÃO DESCOBRIR CEP #####

elif escolha == "Descobrir CEP":
    st.header('𑣲⋆｡˚ Descobrir CEP pelo endereço 𑣲⋆｡˚')
    endereco_usuario = st.text_input('𑣲⋆｡˚ Digite o endereço (ex: Rua Olga, Barueri, SP): ')

    if st.button('Descobrir'):
        if not endereco_usuario.strip():
            st.error('. ݁⋆ ۶ Por favor, insira um endereço válido !ৎ ݁˖ . ݁')
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success('˚˖𓍢ִ໋❀ Link de busca no Google: ')
                st.write(resultado)
            except Exception as e:
                st.error(f'˚˖𓍢ִ໋❀ Ocorreu um erro ao descobrir o CEP: {e}')