# ・Memoryモジュールで会話履歴をもとにした返答をさせる処理を具体的に確認する P154
from langchain.memory import ConversationBufferMemory

def main():
    memory = ConversationBufferMemory(return_messages = True)
    memory.save_context(
        {
            "input": "こんにちは！"
        },
        {
            "output": "こんにちは！お元気ですか？何かご質問があればお知らせください。どのようにお手伝いできますか？"
        }
    )
    memory.save_context(
        {
            "input": "今日はいい天気ですね"
        },
        {
            "output": "私はAIなので実際の天候を感じることはできませんが、いい天気ですね！"
        }
    )
    print(
        memory.load_memory_variables({})
    )
main()