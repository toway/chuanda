
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "8b898504-5c8f-4680-aa26-d11836942b3d540a3806-f814-425b-8a7b-db10bf880762655df000-72aa-4975-9efa-df8e9f512272"
NEVERCACHE_KEY = "fb434c32-8dd8-498b-82f8-e14978abd6fbedb13251-4508-4aae-a528-0d6487cb5d07776067bf-b734-4e90-ac8a-6ec7175ca4ed"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
