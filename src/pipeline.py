from src.chains.base import AppPipeline, HistorySaver, SessionLoader
from src.chains.refine import RefineQuery
from src.chains.retrieval import MultiRetriever
from src.config import AppConfig, logger
from src.chains.jewelry_agent import Agent

pipe_config = [
    SessionLoader(),
    RefineQuery(),
    Agent(),
    HistorySaver(),
]


pipeline = None


def initialize_pipeline(config: AppConfig, verbose=False):
    """Initialize the pipeline"""
    global pipeline
    config.verbose = verbose or config.verbose
    if pipeline is None:
        pipeline = AppPipeline(config)
        pipeline.graph = pipe_config
    return pipeline
