import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
data_dir = (
    os.getenv("DATA_DIR") or "./datas"
)  # use environment variable if set, otherwise use the data directory

with open(".gitignore", "r") as f:
    gitignore = f.read()

if data_dir not in gitignore:
    with open(".gitignore", "a") as f:
        f.write(f"\n{data_dir}")
        f.close()


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Bot(intents=intents)
