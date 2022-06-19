from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "19810037"))
API_HASH = getenv("API_HASH", "b150fc3001853f71e667ad1fd5b4e9de")
BOT_TOKEN = getenv("BOT_TOKEN", "5414874029:AAG-r8v_8HHItL9iatcOncC_GwpfpdZZYxc")
SESSION_NAME = getenv("SESSION_NAME", "BAA3SgvCTc352UOx9iBjnQsREJqJN_DF1VXfGU-BqtqpbUYO1VHjQYYNJAzG5j_CQPAzrv8vQF6hFupDhwoQ7MDJ7SaqS3s-sBW-cVi4KVCZqrnzDXJ3CfmT4gxQKiMviny3xaygo-hUQNFADWVXzQZlpQdYyCloJ-6HjaOT5DiYPnVQsLg_0pA4qioyaFAglyPEcyRdhaUD2wY9cLFcvClXY4ZRgqhuOZFCulADAzUP4vy1wPCbd4xl7JKOzSA8so-fCqjG5kLKzcZufNqjjxzg0td58JrOVYySdA6p6kBPhXb1OPhWN1hEdlvKQVMtSw_W4GQe3fXhjh95H5F7ky6_AAAAAH_idj0A")

# mandatory vars
BOT_NAME = getenv("BOT_NAME", "𝐬𝐞𝐦𝐨 𝐦𝐢𝐮𝐬𝐜 ☕🌿")
OWNER_USERNAME = getenv("OWNER_USERNAME", "S_E_M_O_E_L_K_B_E_R")
ALIVE_NAME = getenv("ALIVE_NAME", "SeMo")
BOT_USERNAME = getenv("BOT_USERNAME", "SE_MO98_BOT")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "SeMo mIuSc")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/SEMOELKBER21/PROOO")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CC_G6")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RAMAZYAT_SEMO")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://MOHAMEDMUSIC:MOHAMEDMUSIC@cluster0.xda63.mongodb.net/?retryWrites=true&w=majority")
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
