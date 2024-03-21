import os
import zipfile
import gdown
from src.ImageClassifier import logger
from src.ImageClassifier.utils.common import get_size
from src.ImageClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Fetch data from url
        """

        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.unzip_dir
            os.makedirs('artifacts/data_ingestion', exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split('/')[-2]
            prefix = "https://drive.google.com/uc?export=download&id="
            gdown.download(prefix+file_id, zip_download_dir)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e


    def extract_zipfile(self):
        """
        Extracts the zip file into the directory
        
        Args:
            zip_file_path: str

        Return:
            None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.loa, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
