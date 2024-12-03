import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "defaultsecretkey")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///todo.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False