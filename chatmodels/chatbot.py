from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

mist = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9
)

print("Welcome! Type 0 to exit the application.")
print("Choose AI personality:")
print("1 - Angry")
print("2 - Sad")
print("3 - Funny")

user = input("Enter choice: ")

if user == "1":
    mood = "You are an angry AI agent. Respond in an angry tone."

elif user == "2":
    mood = "You are a sad AI agent. Respond in a sad tone."

elif user == "3":
    mood = "You are a funny AI agent. Respond in a humorous way."

else:
    mood = "You are a helpful AI assistant."

messages = [
    SystemMessage(content=mood)
]

while True:

    prompt = input("You: ")

    if prompt == "0":
        print("Bot: Bye!")
        break

    messages.append(
        HumanMessage(content=prompt)
    )

    response = mist.invoke(messages)

    messages.append(
        AIMessage(content=response.content)
    )

    print("Bot:", response.content)