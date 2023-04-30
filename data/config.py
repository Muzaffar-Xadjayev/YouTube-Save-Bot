from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
ADMINS_NAME = env.list("ADMINS_NAME")
IP = env.str("ip")  # Xosting ip manzili

CHANNELS = [
    ['1 - Kanal','1661710972',"https://t.me/vakansiya_ishbor_nam"],
    ['2 - Kanal','1611403981',"https://t.me/ishkerak_bor"]
]

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
