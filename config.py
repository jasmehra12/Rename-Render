# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22225430")

API_HASH = os.environ.get("API_HASH", "4c5c28abd62233ef4b993fb972f83262")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7467692523:AAFEndyZsCvmCbyXLEut-FMfoG6CS7dGn7E") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Animes_Nova") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Nova Db")     

DB_URL = os.environ.get("DB_URL", "mongodb://jaskaran1230j:4ixC9jGcE6oCw7qT@ac-5j9u7mb-shard-00-00.tsktd4r.mongodb.net:27017,ac-5j9u7mb-shard-00-01.tsktd4r.mongodb.net:27017,ac-5j9u7mb-shard-00-02.tsktd4r.mongodb.net:27017/?ssl=true&replicaSet=atlas-ammy0t-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "50"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6039119180').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
