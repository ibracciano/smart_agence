# importer prisma
from prisma import Prisma

# creer une instance de Prisma
db = Prisma()

# connecter prisma
async def connect_db():
    #verifier si prisma est connectée 
    if not db.is_connected():
        await db.connect()
    print("Connexion à la base de donnée")

# deconnecter prisma
async def disconnect_db():
    if db.is_connected():
        await db.disconnect()
    print("Deconnexion à la base de donnée")