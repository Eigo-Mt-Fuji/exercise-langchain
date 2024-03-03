```
・言語モデルを使ってテキストをベクトル化する　→ ベクトルデータベースを使って検索する
    ・手元のPDFやExcelファイルを情報源とした検索を行うには？（WikipediaやGoogle検索を使う場合と比べて、検索が難しい）情報源の中身に対応するテキストをベクトル化し、検索可能にしていく　P92
    ・SpaceyTextSplitterで日本語として適切な位置で分割する P104
    ・言語モデルのAPI（OpenAIEmbeddingsやLlamaCppEmbeddingsなど）を使って、テキストのベクトル化する P93
　　    OpenAIの例で言うと、text-embedding-ada-002という言語モデルをAPI経由で使用できる。このAPIを使うと意味を考慮したテキストのベクトル化が行える。
    ・テキストと関連づけてベクトルデータベース（Vector storesといえば、Pinecone,ChromaDBなど）に保存する P107
    ・検索: ユーザからの入力をベクトル化し、事前準備したデータベース（Pinecone,ChromaDBなど）でベクトルを検索して、文章を取得する P110
    ・プロンプト構築: 取得した類似文章を質問と組み合わせてプロンプトを作成（P59 Model I/OモジュールのPromptTemplateを使う）
・chainlinライブラリを使って、チャット画面を実装し、質問を入力できるようにする P119
・LLMChainを使って複数モジュールの組み合わせ。特にLLMRequestsChainを使って特定のURLにアクセスし情報を取得させ、その情報をもとに回答を生成させる P189
・用意されたRetriever(WikipediaRetriever)をつかってWikipediaを情報源にする P135
・Memoryモジュールで会話履歴をもとにした返答をさせる処理を具体的に確認する P154
・複数の会話履歴を持てるチャットbotを作成する P170 
・非常に長い会話履歴に対応する P176
・AgentモジュールのToolを自作する（Agentができることを増やす）P217
```