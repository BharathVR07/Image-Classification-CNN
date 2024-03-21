import os
from box.exceptions import BoxException
import yaml
from src.ImageClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        configBox: ConfigBox type
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file {path_to_yaml} loaded successfully..')
            return ConfigBox(content)
        
    except BoxException:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories

    Args: 
        path_to_directories (list): list of path of directories
    """
    for path in path_to_directories:
        os.makedirs(path, exists_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file data

    Args:
        path (Path) : path to json file

    Return:
        ConfigBox: data as class attributes instead of list
    """

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f'Binary file saved at: {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary data

    Args:
        path (Path): path to binary file

    Return:
        Any: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f'loaded binary file from: {path}')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get the size in kb

    Agrs:
        path (Path): path of the file

    Returns:
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" ~ {size_in_kb} KB"

def decodeImage(img, filename):
    imgdata = base64.b64decode(img)
    with open(filename, 'wb') as f:
        f.write(f)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
