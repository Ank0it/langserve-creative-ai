from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI  # Fixed import
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

app = FastAPI(
    title="Langchain Server",
    description="A simple API server",
    version="1.0.0"
)

# Initialize models - Fixed
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Add base route
add_routes(
    app,
    ChatGoogleGenerativeAI(model="gemini-2.5-flash"),
    path="/gemini"
)

# Prompts
prompt1 = ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("write me a poem about {topic} with 100 words")

# Fixed typo: "eassy" -> "essay"
add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)