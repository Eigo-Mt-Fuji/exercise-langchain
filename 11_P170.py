# ・複数の会話履歴を持てるチャットbotを作成する P170 
import chainlit as cl
import os
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory, RedisChatMessageHistory
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage

chat = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model = "gpt-4-0613")

@cl.on_chat_start
async def on_chat_start():
    thread_id = None

    while not thread_id:
        res = await cl.AskUserMessage(
            content = "私は会話の文脈を考慮した返答ができるチャットボットです。スレッドIDを入力してください。", 
            timeout = 600
        ).send()
        if res:
            thread_id = res['content']
    history = RedisChatMessageHistory(
        session_id = thread_id, 
        url = os.environ["REDIS_URL"]
    )
    memory = ConversationBufferMemory(
        return_messages = True,
        chat_memory = history,
        k =
    )
    # memory = ConversationBufferWindowMemory(
    #     return_messages = True,
    #     chat_memory = history,
    #     k = 3
    # )
    # memory = ConversationSummaryMemory(
    #     llm =chat,
    #     return_messages = True,
    #     chat_memory = history,
    #     k = 3
    # )

    chain = ConversationChain(
        memory = memory,
        llm = chat
    )

    memory_message_result = chain.memory.load_memory_variables({})
    messages = memory_message_result["history"]

    for message in messages:
        if isinstance(message, HumanMessage):
            await cl.Message(
                author = "User", 
                content = f"{message.content}"
            ).send()
        else:
            await cl.Message(
                author = "ChatBot",
                content = f"{message.content}",
            ).send()
    cl.user_session.set("chain", chain)

@cl.on_message
async def on_message(input_message):
    
    chain = cl.user_session.get("chain")
    result = chain(input_message)
    await cl.Message(content = result["response"]).send()   
