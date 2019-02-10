class MYSQL(object):
    host = 'mysql'
    port = 3306
    user = 'dbuser'
    passwd = 'userpass'
    db = 'reviews'

    @classmethod
    def connection_uri(cls):
        uri_template = "mysql://{user}:{password}@{host}:{port}/{name}"
        return uri_template.format(
            user=cls.user,
            password=cls.passwd,
            host=cls.host,
            port=cls.port,
            name=cls.db,
        )

    @classmethod
    def params(cls):
        return {
            "SQLALCHEMY_DATABASE_URI": cls.connection_uri(),
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
