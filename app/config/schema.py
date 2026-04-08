from pydantic import BaseModel


class PipelineConfig(BaseModel):
    batch_size: int
    retry_count: int


class LoggingConfig(BaseModel):
    level: str


class ModelConfig(BaseModel):
    provider: str
    model_name: str
    temperature: float


class AppConfig(BaseModel):
    pipeline: PipelineConfig
    logging: LoggingConfig
    model: ModelConfig