import requests

import env_variables

API_TOKEN=env_variables.api_token()
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta" #Add a URL for a model of your choosing
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def llmrag_query(question):
    context = "As of the most current census, Jacksonville, Florida has a population of 1 million."
    prompt = f"""Use the following context to answer the question at the end.

    {context}

    Question: {question}
    """

    #print('prompt fed to query is :')
    #print(prompt)
    query_response=query(prompt)
    return query_response

def query(prompt):
    #print('inside query prompt is :')
    #print(prompt)
    payload = {
        "inputs": prompt,
        "parameters": { #Try and experiment with the parameters
            "max_new_tokens": 1024,
            "temperature": 0.6,
            "top_p": 0.9,
            "do_sample": False,
            "return_full_text": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['generated_text']