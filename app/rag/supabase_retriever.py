from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from supabase import create_client

from app.core.config import settings


def get_retriever():
    supabase = create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_KEY,
    )

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=settings.OPENAI_API_KEY,
    )

    def retrieve(query: str, k: int = 5):
        # gerar embedding da query
        query_embedding = embeddings.embed_query(query)

        response = supabase.rpc(
            "match_documents",
            {
                "query_embedding": query_embedding,
                "match_count": k,
            },
        ).execute()

        print(
            "[RAG] rpc returned rows:", 0 if not response.data else len(response.data)
        )
        if response.data:
            for row in response.data:
                print("   row:", row.get("content"), "sim=", row.get("similarity"))

        if not response.data:
            return []

        return [
            Document(
                page_content=row["content"],
                metadata={"similarity": row["similarity"]},
            )
            for row in response.data
        ]

    return retrieve
