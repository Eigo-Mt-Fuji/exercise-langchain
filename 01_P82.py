# Output parsers - 出力を構造化する P82

# from langchain root module is no longer supported. Please use langchain.prompts.PromptTemplate instead.
from langchain.prompts import PromptTemplate
# LangChainDeprecationWarning: The class `langchain_community.chat_models.openai.ChatOpenAI` was deprecated in langchain-community 0.0.10 and will be removed in 0.2.0. An updated version of the class exists in the langchain-openai package and should be used instead. To use it run `pip install -U langchain-openai` and import as `from langchain_openai import ChatOpenAI`.
from langchain_openai import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser
from langchain.schema import HumanMessage
import os
def main():
    output_parser = DatetimeOutputParser()
    chat = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model = "gpt-4-0613")

    prompt = PromptTemplate.from_template("{product}のリリース日を教えて！")

    result = chat.invoke([
        HumanMessage(content = prompt.format(product = "iPhoneXR")),
        HumanMessage(content = output_parser.get_format_instructions())
    ])

    output = output_parser.parse(result.content)
    return output

print(main())
