# 2. Compute similarity between two sentences
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 = "The cat sits on the mat."
sentence2 = "A cat is sitting on the rug."

embedding1 = model.encode(sentence1, convert_to_tensor=True)
embedding2 = model.encode(sentence2, convert_to_tensor=True)

similarity = cos_sim(embedding1, embedding2)

print(similarity.item())