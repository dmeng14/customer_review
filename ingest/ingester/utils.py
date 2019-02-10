import shutil
import tempfile
from contextlib import contextmanager


@contextmanager
def tmp_dir() -> str:
    tmp_dir = tempfile.mkdtemp()
    try:
        yield tmp_dir
    finally:
        shutil.rmtree(tmp_dir)
