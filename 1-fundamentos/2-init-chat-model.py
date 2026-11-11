from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

gemini = init_chat_model("gemini-1.5", model_provider="google_genai")
answer_gemini = gemini.invoke("Hello World!")
print(answer_gemini.content)