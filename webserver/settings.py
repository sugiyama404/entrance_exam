import configparser
import os

conf = configparser.ConfigParser()
conf.read('settings.ini')

img_dir_name = conf['DEFAULT']['img_dir_name']
web_port = int(conf['web']['port'])

dbuser=os.getenv('MYSQL_USER')
dbpassword=os.getenv('MYSQL_PASSWORD')
dbhost=os.getenv('MYSQL_HOST')
dbname=os.getenv('MYSQL_DB')

api_base_url = os.getenv('API_BASE_URL')

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
