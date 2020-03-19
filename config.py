
class Config:
    """Setting flask configs"""

    # # General Config like secret key, flask_app, flask env
    SECRET_KEY = '87587587'

    # Database configs(FORMAT)
    # [DB_TYPE] + [DB_CONNECTOR]: // [USERNAME]: [PASSWORD] @ [HOST]:[PORT] / [DB_NAME]
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

