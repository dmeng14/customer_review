from unittest.mock import patch
from ingester.tasks import ingest_data_to_db


@patch('ingester.tasks.download_file')
@patch('ingester.tasks.load_review')
def test_ingest_data_to_db(mock_load, mock_filepath):
    mock_filepath.return_value = 'temp_path'
    ingest_data_to_db('temp_key')
    mock_load.assert_called_with('temp_path')
