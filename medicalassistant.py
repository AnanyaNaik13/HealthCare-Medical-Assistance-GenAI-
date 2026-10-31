import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
 
load_dotenv()
 
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=os.getenv("GROQ_API_KEY"), temperature=0)
 
 
def get_recommendation(symptoms):
    prompt = """Role:Act as a helpful health information assistant Task:Give general information about common over-the-counter medicines and simple home care for the given symptoms. Also mention when the person should see a doctor. symptoms:{}""".format(
        symptoms
    )
 
    response = llm.invoke(prompt)
    return response.content