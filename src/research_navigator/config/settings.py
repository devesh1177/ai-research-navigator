from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    qdrant_host: str = "localhost"

    qdrant_port: int = 6333

    collection_name: str = "research_navigator"

    vector_size: int = 384

    retrieval_min_score: float = 0.55

    retrieval_confidence_threshold: float = 0.55

    embedding_model: str = "BAAI/bge-small-en-v1.5"

    recent_year_window: int = 3

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
