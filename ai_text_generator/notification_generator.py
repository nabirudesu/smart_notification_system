import os
import sys
sys.path.append('./')
from openai import AzureOpenAI
from ai_text_generator.prompt_data import bot_context, applicaiton_context
def generate_notification_message(query,user_data):
  client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-15-preview"
  )
  response = client.chat.completions.create(
      model="notification-generator-deployment", 
      messages=[
          {"role": "system", "content": bot_context},
          {"role": "user", "content": applicaiton_context},
          {"role": "user", "content": str(user_data)},
          {"role": "user", "content": query}
      ],
      max_tokens=40,
      temperature=1,
      top_p=0.5,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None)
  print(response.choices[0].message.content)
  return response.choices[0].message.content
