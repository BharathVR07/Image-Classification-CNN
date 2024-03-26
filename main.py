from src.ImageClassifier import logger
from src.ImageClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ImageClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.ImageClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.ImageClassifier.pipeline.stage_04_model_evaluation_mlflow import EvaluationPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Prepare Base Model'

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Training'

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Evaluation'

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e