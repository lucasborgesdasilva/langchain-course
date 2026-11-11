from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Create a ChatOpenAI instance with the desired model and temperature
model = ChatOpenAI(model_name="gpt-4", temperature=0.9)

# Invoke the model with a prompt
message = model.invoke("Hello World!")

# Print the response from the model
print(message.content)