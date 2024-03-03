# ・LLMChainを使って複数モジュールの組み合わせ。特にLLMRequestsChainを使って特定のURLにアクセスし情報を取得させ、その情報をもとに回答を生成させる P189
import os
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain, LLMRequestsChain
from langchain.prompts import PromptTemplate

def main():
    chat = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model = "gpt-4-0613")
    prompt = PromptTemplate(
        input_variables = ["requests_result", "query"],
        template = """文章をもとに質問に答えてください。
    文章: {requests_result}

    質問: {query}
""")

    llm_chain = LLMChain(llm = chat, prompt = prompt, verbose = True)

    chain = LLMRequestsChain(llm_chain = llm_chain)

    print(chain({
        "query": "東京の天気を教えて", 
        "url": "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json"
    }))
main()
