from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Model
model = ChatMistralAI(model="mistral-small-latest")

# 2. Prompt Template
prompt_template = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# 3. Output Parser
parser = StrOutputParser()

# 4. Chain
chain = prompt_template | model | parser

# Run the chain
result = chain.invoke({"topic": "Machine Learning"})

print(result)