import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


GOOGLE_API_KEY = getpass.getpass("Enter your API Key: ")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

#hilangkan log warning
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GRPC_CPP_VERBOSITY"] = "ERROR"

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages = [
    SystemMessage(content="You are a funny assistant that always joking.")
]

while True:
    prompt = input("User: ")
    messages.append(HumanMessage(content=prompt))
    response = llm.invoke(messages)
    print("AI: ", response.content)
    messages.append(response)

