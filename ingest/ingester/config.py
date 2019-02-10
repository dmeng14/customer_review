class CELERY(object):
    BrokerUrl = 'redis://broker-backend:6379//0'
    ResultBackend = 'redis://broker-backend:6379//0'


class AWS(object):
    bucket = 'amazon-reviews-pds'
    prefix = 'tsv'


class MYSQL(object):
    host = 'mysql'
    port = 3306
    user = 'dbuser'
    passwd = 'userpass'
    db = 'reviews'


def get_db_config(db_key):
    return dict(
        host=db_key.host,
        user=db_key.user,
        passwd=db_key.passwd,
        db=db_key.db,
        port=db_key.port,
    )
