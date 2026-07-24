from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

embedding=HuggingFaceEmbeddings(
     model_name="sentence-transformers/all-MiniLM-L6-v2"
)
documents = [
    "Virat Kohli is an Indian cricketer known for his exceptional batting skills and aggressive style of play. He has captained the Indian cricket team and is regarded as one of the greatest batsmen of his generation.",

    "MS Dhoni is a former Indian cricket captain and wicketkeeper-batsman. He led India to victory in the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy. He is famous for his calm leadership and finishing ability.",

    "Sachin Tendulkar is a legendary Indian cricketer widely regarded as one of the greatest batsmen in cricket history. He scored 100 international centuries and was the first player to score a double century in men's ODI cricket.",

    "Rohit Sharma is an Indian cricketer known for his elegant batting and ability to score big hundreds. He has scored multiple double centuries in ODI cricket and has also been a successful captain in international and IPL cricket.",

    "Jasprit Bumrah is an Indian fast bowler known for his unique bowling action, accuracy, yorkers, and ability to perform under pressure. He has been one of India's leading fast bowlers across Test, ODI, and T20 formats.",

    "Yuvraj Singh is a former Indian all-rounder famous for his powerful left-handed batting. He played an important role in India's 2007 T20 World Cup and 2011 ODI World Cup victories and was named Player of the Tournament in the 2011 World Cup.",

    "Kapil Dev is a former Indian cricket captain and one of India's greatest all-rounders. He captained India to its first Cricket World Cup victory in 1983 and was known for his fast bowling and attacking batting.",

    "AB de Villiers is a former South African cricketer known for his innovative and explosive batting. He earned the nickname Mr. 360 because of his ability to play shots all around the cricket ground.",

    "Chris Gayle is a former West Indies cricketer famous for his destructive batting and powerful six-hitting ability. He is considered one of the greatest T20 batsmen and is popularly known as the Universe Boss.",

    "Kane Williamson is a New Zealand cricketer known for his technically strong batting and calm leadership. He has been one of New Zealand's most successful batsmen and captains in international cricket."
]
query="tell me about virat kohli"

doc_emb = embedding.embed_documents(documents)
query_emb = embedding.embed_query(query)

scores = cosine_similarity([query_emb], doc_emb)[0]

index, score = max(
    enumerate(scores),
    key=lambda x: x[1]
)

print("Query:", query)
print("Most similar document:")
print(documents[index])
print("Similarity score is:", score)