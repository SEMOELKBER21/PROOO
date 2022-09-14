from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
SESSION_NAME = getenv("SESSION_NAME", "")

# mandatory vars
BOT_NAME = getenv("BOT_NAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CC_G6")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", '').split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5183920797").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5183920797").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/556162ae99ca1043d7d47.jpg")
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/5f2e911c64cf25f99c591.jpg")
