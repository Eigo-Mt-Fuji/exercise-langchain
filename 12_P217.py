# ・AgentモジュールのToolを自作する（Agentができることを増やす）P217

def min_limit_random_number(min_number):
    return random.randint(min_number, 100000)

def main():
    chat = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model = "gpt-4-0613", temperature = 0)

    tools = []

    tools.append(WriteFileTool(root_dir="./"))

    tools.append(
        Tool(
            name = "Random", 
            description = "特定最小値以上のランダム値生成", 
            func = min_limit_random_number
        )
    )

    agent = initialize_agent(
        tools,
        chat,
        agent = AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose = True
    )

    result = agent.run("10以上のランダムな数字を生成して、random.txtというファイルに保存してください。")
    return result

print(main())
