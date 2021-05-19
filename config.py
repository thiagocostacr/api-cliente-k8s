import os

JSON_SORT_KEYS = os.environ.get('JSON_SORT_KEYS', 'False').lower() in ('true')
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT"))
