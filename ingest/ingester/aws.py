import os
import logging
import urllib.request
from ingester import config as cfg


logger = logging.getLogger(__name__)


def filename_from_s3_key(key: str) -> str:
    return key.split('/')[-1]


def download_file(key: str, tmp_dir: str) -> str:
    filename = filename_from_s3_key(key)
    target = os.path.join(tmp_dir, filename)
    s3_url = f'https://s3.amazonaws.com/{cfg.AWS.bucket}/{cfg.AWS.prefix}/{key}'
    urllib.request.urlretrieve(s3_url, target)
    return target
