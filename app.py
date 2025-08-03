from langchain_openai import ChatOpenAI

local_llm = ChatOpenAI(
    model= "ai/llama3.2",
    api_key="nope",
    base_url= "http://model-runner.docker.internal/engines/llama.cpp/v1"
)

response = local_llm.invoke(
    "how are you?"
)

print(response.content)