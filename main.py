# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-large")

# Make a prediction
result = pipe("Who is Elon Musk? Give your answer in detail.", max_length=50)
print(result)