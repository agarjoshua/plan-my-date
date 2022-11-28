import os

databaseurl = "sqlite://pmd.db"
# databaseurl = "postgres://hello_fastapi:hello_fastapi@db:5432/hello_fastapi_dev"

TORTOISE_ORM = {
    "connections": {
        "default": os.environ.get("DATABASE_URL")
        },
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
