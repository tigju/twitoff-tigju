# app/services/basilica_service.py

import os
import basilica
from dotenv import load_dotenv

load_dotenv() # parse the .env file for environment variables

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)
# print(type(connection)) #> <class 'basilica.Connection'>

if __name__ == "__main__":
    
    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]

    embeddings = list(connection.embed_sentences(sentences))
    # print(type(embeddings)) #> list
    print(embeddings) # [[0.8556405305862427, ...], ...]