from typing import List
from openai import AsyncOpenAI
from app.core.config import settings


class EmbeddingClient:
    """
    Client for generating embeddings using OpenAI.
    Uses text-embedding-3-small model with 1536 dimensions.
    """
    
    MODEL = "text-embedding-3-small"
    DIMENSIONS = 1536
    
    _instance: "EmbeddingClient" = None
    _client: AsyncOpenAI = None
    
    @classmethod
    def get_instance(cls) -> "EmbeddingClient":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self._client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    
    async def embed(self, text: str) -> List[float]:
        """
        Generate embedding for a single text string.
        
        Args:
            text: Input text to embed
            
        Returns:
            List of floats representing the embedding vector (1536 dimensions)
        """
        response = await self._client.embeddings.create(
            model=self.MODEL,
            input=text,
            dimensions=self.DIMENSIONS,
        )
        return response.data[0].embedding
    
    async def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple texts.
        
        Args:
            texts: List of input texts
            
        Returns:
            List of embedding vectors
        """
        response = await self._client.embeddings.create(
            model=self.MODEL,
            input=texts,
            dimensions=self.DIMENSIONS,
        )
        return [item.embedding for item in response.data]
