import connexion
from api import config
from api.db import DB


app = connexion.FlaskApp(__name__)

app.add_api(
    "swagger.yaml",
    resolver=connexion.RestyResolver("customer_review.api"),
    strict_validation=True,
    validate_responses=True,
)
app = app.app

app.config.update(**config.MYSQL.params())
DB.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
