import json
import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('Book.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('부산소프트웨어마이스터고 학교안내 챗봇')
st.subheader("소마고 챗봇")

with st.form('form', clear_on_submit=True):
    user_input = st.text_input('입력 : ', '')
    submitted = st.form_submit_button('전송')

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if submitted and user_input:
    embedding = model.encode(user_input)

    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]

    st.session_state.past.append(user_input)
    if answer['distance'] > 0.5:
        st.session_state.generated.append(answer['답변'])
    else:
        st.session_state.generated.append('잘 모르겠어요. 자세한 내용은 학교로 연락주세요. 051-971-2153')

for i in range(len(st.session_state['past'])):
    # message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    # if len(st.session_state['generated']) > i:
    #     message(st.session_state['generated'][i], key=str(i) + '_bot')
    st.markdown[
        
    ]
    
