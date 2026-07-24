from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
mist = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.7
)

response = mist.invoke("Tell me about Emiway Bantai in one paragraph.")

print(response.content)