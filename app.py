#import os
import requests

import llmrag_query_response

#API_TOKEN=env_variables.api_token()
#API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta" #Add a URL for a model of your choosing
#headers = {"Authorization": f"Bearer {API_TOKEN}"}

#def query(prompt):
#    payload = {
#        "inputs": prompt,
#        "parameters": { #Try and experiment with the parameters
#            "max_new_tokens": 1024,
#            "temperature": 0.6,
#            "top_p": 0.9,
#            "do_sample": False,
#            "return_full_text": False
#        }
#    }
#    response = requests.post(API_URL, headers=headers, json=payload)
#    return response.json()[0]['generated_text']

#if __name__ == "__main__":
#    question = "What is the population of Jacksonville, Florida?"
#    context = "As of the most current census, Jacksonville, Florida has a population of 1 million."
#    prompt = f"""Use the following context to give a concise answer the question at the end.

#    {context}

#    Question: {question}
#    """

#    #print(query(prompt))
#    #print(llmrag_query_response.query(prompt))
#    print(llmrag_query_response.llmrag_query(question))

question = "What is the population of Jacksonville, Florida?"
context = "As of the most current census, Jacksonville, Florida has a population of 1 million."
prompt = f"""Use the following context to give a concise answer the question at the end.

{context}

Question: {question}
"""

#print(llmrag_query_response.query(prompt))
print(llmrag_query_response.llmrag_query(question))