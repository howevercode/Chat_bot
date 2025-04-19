#IMPORTING ALL DEPENDENCIES
 
import streamlit as st
import   os
from groq import groq
import random
import random
from langchain.chains import conversationchain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import chatgroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
  
#LOADED API KEY FROM .ENV FILE I CREATED
load_dotenv()
groq_api_key= os.environ['GROQ_API_KEY']

def main():
    st.title('GROQ Chat Application')

    st.sidebar.title('Select a LLM')
    model= st.sidebar.selectbox(
        'Choose a model',
        ['mistral-saba-24b', 'compound-beta']
    )
    
    conversational_memory_length= st.sidebar.slider("conversational_memory_length", 1, 10, 5)

#I CREATED MEMORY WHERE QUES ASKED BY USER ARE SAVED TO CREATE HISTORY IF THEY NEED LATER
    user_question= st.text_area("Ask your Question") 
    if 'chat_history' not in st.session_state:
        st.session_state,chat_history=[]
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input':message['human']}, {'output': message['AI']})

    groq_chat= chatgroq(
            groq_api_key= groq_api_key,
            model_name= model
    )
    conversation= conversationchain(
        llm= groq_chat,
        memory= memory
    )

    if user_question:
        response= conversation(user_question)
        message= {'human':user_question, 'AI':response['response']}
        st.session_state.chat_history.append(message)
        st.write("Chatbot:", response['response'])

if __name__=="__main__":
    main()