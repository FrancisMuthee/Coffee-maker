import os 

print(os.environ.get('DB_USER'))
print(os.environ.get('DB_PASSWORD'))

print("DB_NAME:", os.environ.get('DB_NAME'))
print("DB_USER:", os.environ.get('DB_USER'))
print("DB_PASSWORD:", os.environ.get('DB_PASSWORD'))
print("DB_HOST:", os.environ.get('DB_HOST'))
print("DB_PORT:", os.environ.get('DB_PORT'))
