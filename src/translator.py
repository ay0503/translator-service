import string

from openai import AzureOpenAI
from constants import *

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key="A3jAqgnw7S5tWR1x6RyhTPcRJADK8mV7pN5WondwLRI4bEzssq6yJQQJ99AJACYeBjFXJ3w3AAABACOGLpjw",
    api_version="2024-02-15-preview",
    azure_endpoint="https://tbd-andrew-openai.openai.azure.com/"
)

# Make a request to your Azure OpenAI model
response = client.chat.completions.create(
    model="gpt-4o-mini",  # This should match your deployment name in Azure
    messages=[
        {
            "role": "user",
            "content": "I'm here to use you as a translator."
        }
    ]
)

def get_translation(post: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # This should match your deployment name in Azure
        messages=[
            {
                "role": "system",
                "content": NODEBB_TRANSLATION_CONTEXT
            },
            {
                "role": "user",
                "content": post
            }
        ]
    )
    return response.choices[0].message.content

def get_language(post: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # This should match your deployment name in Azure
        messages=[
            {
                "role": "system",
                "content": NODEBB_CLASSIFICATION_CONTEXT
            },
            {
                "role": "user",
                "content": post
            }
        ]
    )

    return response.choices[0].message.content

def translate_content(content: str) -> tuple[bool, str]:
    try:
        is_english = get_language(content).strip().lower() == ENGLISH
        if is_english:
            return (True, content)

        translation = get_translation(content)
        if isinstance(translation, str) and translation.strip():
            return (False, translation)
        else:
            raise ValueError("Invalid format: Translation is not a valid string.")
    except Exception as e:
        return (False, "Error processing the request")
