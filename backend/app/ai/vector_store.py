import chromadb

class VectorStore:
    def __init__(self):
        self.client=chromadb.PersistentClient(
            path="data/chroma_db"   #store vectors on disk
        )
        self.collection=self.client.get_or_create_collection(name="investor_documents")

    def add_documents(self,ids,documents,embeddings,metadatas):
        self.collection.add(ids=ids,documents=documents,embeddings=embeddings,metadatas=metadatas)

    def search(self,query_embedding,n_results=5):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

    def delete_collection(self):
        self.client.delete_collection("investor_documents")