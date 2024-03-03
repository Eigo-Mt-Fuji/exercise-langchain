# ・検索: ユーザからの入力をベクトル化し、事前準備したデータベース（Pinecone,ChromaDBなど）でベクトルを検索して、文章を取得する P110

    # ・言語モデルを使ってテキストをベクトル化する　→ ベクトルデータベースを使って検索する
    #     ・手元のPDFやExcelファイルを情報源とした検索を行うには？（WikipediaやGoogle検索を使う場合と比べて、検索が難しい）情報源の中身に対応するテキストをベクトル化し、検索可能にしていく　P92
    #     ・SpaceyTextSplitterで日本語として適切な位置で分割する P104
    #     ・言語モデルのAPI（OpenAIEmbeddingsやLlamaCppEmbeddingsなど）を使って、テキストのベクトル化する P93
    # 　　    OpenAIの例で言うと、text-embedding-ada-002という言語モデルをAPI経由で使用できる。このAPIを使うと意味を考慮したテキストのベクトル化が行える。
    #     ・テキストと関連づけてベクトルデータベース（Vector storesといえば、Pinecone,ChromaDBなど）に保存する P107
    #     ・検索: ユーザからの入力をベクトル化し、事前準備したデータベース（Pinecone,ChromaDBなど）でベクトルを検索して、文章を取得する P110
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def search(persist_directory):
    embeddings = OpenAIEmbeddings(model = "text-embedding-ada-002")
    database = Chroma(
        persist_directory = persist_directory, 
        embedding_function = embeddings
    )
    documents = database.similarity_search("飛行機の最高速度は?")
    return documents

def main():
    documents = search("./.data")
    print(len(documents))
    for document in documents:
        print(document.page_content)

main()