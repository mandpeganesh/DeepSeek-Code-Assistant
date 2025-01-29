from decouple import config
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

HUGGINGFACHUB_API_TOKEN = config('HUGGINGFACHUB_API_TOKEN')
repo_id = "deepseek-ai/deepseek-coder-1.3b-instruct"

def ask_query(query):
    llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACHUB_API_TOKEN)
    
    chat = ChatHuggingFace(llm=llm, verbose=True)
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        """
        You are a highly skilled AI coding assistant. 
        Your task is to analyze the given query and provide accurate, detailed, and optimized coding solutions. 
        Always ensure your response align with best practices, is effiecient, and considers edge cases. 
        Introduce yourself as a coding assitant.
        """
    )
    
    human_message_prompt = HumanMessagePromptTemplate.from_template('{query}')
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    formatted_chat_prompt = chat_prompt.format_messages(query=query)
    response = chat.invoke(formatted_chat_prompt)
    return response.content