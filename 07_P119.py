# ・chainlinライブラリを使って、チャット画面を実装し、質問を入力できるようにする P119
import chainlit as cl
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
import os

embeddings = OpenAIEmbeddings(model = "text-embedding-ada-002")
chat = ChatOpenAI(openai_api_key = os.environ["OPENAI_API_KEY"], model = "gpt-4-0613")
prompt = PromptTemplate(template=  """文章をもとに質問に答えてください。

文章: 

{document}

質問:

{query}
""", input_variables=["document", "query"])

database = Chroma(
    persist_directory = "./.data",
    embedding_function = embeddings
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content = "準備ができました！メッセージを入力してください！").send()

@cl.on_message
async def on_message(input_message):
    print("入力されたメッセージ: " + input_message)
    documents = database.similarity_search(input_message)
    if message.content == "終了":
        await cl.Message(content = "終了しました！").send()
        return
    documents = database.similarity_search(message.content)
    documents_string = ""

    for document in documents:
        documents_string += f"""
        ------------------------
        {document.page_content}
        """
    
    result = chat.invoke([
        HumanMessage(content = prompt.format(document=documents_string, query=input_message))
    ])
    await cl.Message(content = result.content).send()
