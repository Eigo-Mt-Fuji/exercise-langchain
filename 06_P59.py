# ・プロンプト構築: 取得した類似文章を質問と組み合わせてプロンプトを作成（P59 Model I/OモジュールのPromptTemplateを使う）
from langchain.prompts import PromptTemplate

def make_prompt_ask_product_maker(product):
    prompt = PromptTemplate(
        template = "{product}はどこが開発した製品ですか？",
        input_variables = ["product"]
    )
    return prompt.format(product = product)
def main():
    print(make_prompt_ask_product_maker("iPhone"))
    print(make_prompt_ask_product_maker("Xperia"))

main()