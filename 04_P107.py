# テキストと関連づけてベクトルデータベース（Vector storesといえば、Pinecone,ChromaDBなど）に保存する P107
# ・言語モデルを使ってテキストをベクトル化する　→ ベクトルデータベースを使って検索する
#     ・手元のPDFやExcelファイルを情報源とした検索を行うには？（WikipediaやGoogle検索を使う場合と比べて、検索が難しい）情報源の中身に対応するテキストをベクトル化し、検索可能にしていく　P92
#     ・SpaceyTextSplitterで日本語として適切な位置で分割する P104
#     ・言語モデルのAPI（OpenAIEmbeddingsやLlamaCppEmbeddingsなど）を使って、テキストのベクトル化する P93
# 　　    OpenAIの例で言うと、text-embedding-ada-002という言語モデルをAPI経由で使用できる。このAPIを使うと意味を考慮したテキストのベクトル化が行える。
#     ・テキストと関連づけてベクトルデータベース（Vector storesといえば、Pinecone,ChromaDBなど）に保存する P107
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters.spacy import SpacyTextSplitter    
from langchain_openai import OpenAIEmbeddings
# /Users/eigofujikawa/.asdf/installs/python/3.10.13/lib/python3.10/site-packages/langchain/vectorstores/__init__.py:35: LangChainDeprecationWarning: Importing vector stores from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:
from langchain_community.vectorstores import Chroma

import os

def split_documents(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = SpacyTextSplitter(
        chunk_size = 300,
        pipeline = "ja_core_news_sm"
    )
    return text_splitter.split_documents(documents)

def write_chroma_documents(splitted_documents, persist_directory):
    embeddings = OpenAIEmbeddings(model = "text-embedding-ada-002")
    database = Chroma(
        persist_directory = persist_directory,
        embedding_function = embeddings
    )
    database.add_documents(splitted_documents)

def main():
    splitted_documents = split_documents(os.environ["PDF_PATH"])
    write_chroma_documents(splitted_documents, "./.data")

main()
