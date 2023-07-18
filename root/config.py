"""
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo
Dont kang !!!
© Mrvishal2k2
"""
import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "8206404"))
    API_HASH = os.environ.get("API_HASH", "e935d9b56e3fd2c05c743093efb761c9")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5951942864:AAHj5HilQ7Ryu_ZOQYeUhZDtFEDfVYHSjQA")
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "858588280").split()]
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./bot/DOWNLOADS")
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Aman:<Aman>@cluster0.jf3q4pn.mongodb.net/?retryWrites=true&w=majority")
    # owner is for log cmd only owner can use (this can be multiple users)
    OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "858588280").split(" ")]
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "BotDunia")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", False)
