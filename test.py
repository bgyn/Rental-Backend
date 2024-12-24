from decouple import config

username = config('USER_NAME')
print(username)

print(config('DB_NAME'))