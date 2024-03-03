# ・言語モデルを使ってテキストをベクトル化する　→ ベクトルデータベースを使って検索する
#     ・手元のPDFやExcelファイルを情報源とした検索を行うには？（WikipediaやGoogle検索を使う場合と比べて、検索が難しい）情報源の中身に対応するテキストをベクトル化し、検索可能にしていく　P92
#     ・SpaceyTextSplitterで日本語として適切な位置で分割する P104
# Importing document loaders from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:
from langchain_community.document_loaders import PyMuPDFLoader
import spacy
from langchain_text_splitters.spacy import SpacyTextSplitter
import os

def main():
    loader = PyMuPDFLoader(os.environ["PDF_PATH"])
    documents = loader.load()
    # python3 -m spacy download ja_core_news_sm : https://github.com/explosion/spaCy/issues/4577
    spacy.load("ja_core_news_sm")

    text_splitter = SpacyTextSplitter(
        # ValueError: Got a larger chunk overlap (200) than chunk size (100), should be smaller.
        chunk_size = 200,
        pipeline = "ja_core_news_sm"
    )
    # AttributeError: 'SpacyTextSplitter' object has no attribute 'split' https://github.com/langchain-ai/langchain/issues/9528
    splitted_documents = text_splitter.split_documents(documents)
    return {"before": len(documents), "after": len(splitted_documents)}
print(main())
