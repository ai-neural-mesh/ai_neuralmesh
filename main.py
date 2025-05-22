
import os
from openai import AzureOpenAI

def llm_init_test(user_question):
    os.environ["AZURE_OPENAI_API_VERSION"] = "2024-12-01-preview"
    os.environ["AZURE_OPENAI_API_KEY"] = "BrOQIgoSXHXmhAGZFdAu1bohLvVHA5U5captEcD7dz21zor6YGeXJQQJ99BEACHYHv6XJ3w3AAAAACOGDo6M"
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://ratec-mas3pb9u-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2025-01-01-preview"
    os.environ["AZURE_OPENAI_DEPLOYMENT"] = "gpt-4.1"       
    api_version="2024-12-01-preview"
    subscription_key='BrOQIgoSXHXmhAGZFdAu1bohLvVHA5U5captEcD7dz21zor6YGeXJQQJ99BEACHYHv6XJ3w3AAAAACOGDo6M'
    #endpoint='https://ratec-∏u-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2025-01-01-preview'
    endpoint='https://ratec-mas3pb9u-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2025-01-01-preview'
    #endpoint = "https://ratec-mas3pb9u-eastus2.cognitiveservices.azure.com/"
    deployment = "gpt-4.1"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": f'{user_question}',
            }
        ],
        max_completion_tokens=800,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model=deployment
    )

    return(response.choices[0].message.content)

if __name__ == "__main__":
    user_question = input("Please enter your question: ")
    response = llm_init_test(user_question)
    print(response)
