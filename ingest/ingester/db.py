import gzip
import shutil
import contextlib
import logging
import MySQLdb
import MySQLdb.cursors as mc
from ingester.config import get_db_config, MYSQL


logger = logging.getLogger(__name__)


class DBConnectionError(Exception):
    pass


@contextlib.contextmanager
def db_connection(db_config):
    try:
        conn = MySQLdb.connect(
            db_config['host'],
            db_config['user'],
            db_config['passwd'],
            db_config['db'],
            db_config.get('port', 3306),
            charset=db_config.get('charset', 'utf8'),
            connect_timeout=60 * 5,
            local_infile=1
        )
    except MySQLdb.Error as e:
        raise DBConnectionError("Error connecting to database") from e
    else:
        cursor = conn.cursor(mc.Cursor)
        try:
            yield cursor
            cursor.close()
        except Exception as e:
            conn.rollback()
            raise e
        else:
            conn.commit()
        finally:
            conn.close()


def load_review(filepath: str) -> None:
    """ load a file into the customer_review table  """
    sql = """
        {load_data_clause}
        INTO TABLE customer_review
        CHARACTER SET UTF8
        FIELDS TERMINATED BY '\\t'
        ENCLOSED BY '"'
        LINES TERMINATED BY '\\n'
        IGNORE 1 ROWS
        (marketplace, customer_id, review_id,
        product_id, product_parent, product_title,
        product_category, star_rating, helpful_votes,
        total_votes, vine, verified_purchase,
        review_headline, review_body, review_date)
    """
    new_file = filepath[:-3]
    with gzip.open(filepath, 'r') as f_in, open(new_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    logger.debug(f'dest file location: {new_file}')

    db_config = get_db_config(MYSQL)
    with db_connection(db_config) as cursor:
        sql = sql.format(load_data_clause=f"LOAD DATA LOCAL INFILE '{new_file}'")
        cursor.execute(sql)
