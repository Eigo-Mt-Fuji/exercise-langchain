# ・言語モデルを使ってテキストをベクトル化する　→ ベクトルデータベースを使って検索する
#     ・手元のPDFやExcelファイルを情報源とした検索を行うには？（WikipediaやGoogle検索を使う場合と比べて、検索が難しい）情報源の中身に対応するテキストをベクトル化し、検索可能にしていく　P92
#     ・言語モデルのAPI（OpenAIEmbeddingsやLlamaCppEmbeddingsなど）を使って、テキストのベクトル化する P93
# /Users/eigofujikawa/.asdf/installs/python/3.10.13/lib/python3.10/site-packages/langchain/embeddings/__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:
# The class `langchain_community.embeddings.openai.OpenAIEmbeddings` was deprecated in langchain-community 0.0.9 and will be removed in 0.2.0. An updated version of the class exists in the langchain-openai package and should be used instead. To use it run `pip install -U langchain-openai` and import as `from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from numpy import dot
from numpy.linalg import norm

def cos_sim(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))

def main():
    embeddings = OpenAIEmbeddings(model = "text-embedding-ada-002")
    query_vector = embeddings.embed_query("飛行機の最高速度は?")

    part_of_query_vector = query_vector[:5]

    document_1_vector = embeddings.embed_query("飛行機の最高速度は時速150キロメートルです。")
    document_2_vector = embeddings.embed_query("鶏肉を適切に下味つけた後、中火で焼きながらたまに裏返し、外側は香ばしく仲は柔らかく仕上げる。")

    cos_sim_1 = cos_sim(query_vector, document_1_vector)
    
    cos_sim_2 = cos_sim(query_vector, document_2_vector)

    return {
        "cos_sim_1": cos_sim_1, 
        "cos_sim_2": cos_sim_2, 
        "part_of_query_vector": part_of_query_vector
    }

print(main())