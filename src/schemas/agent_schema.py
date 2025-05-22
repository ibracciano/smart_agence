from pydantic import BaseModel, Field, constr
from enum import Enum
from datetime import datetime


class AgentCategorie(Enum):
    TRANSACTION = "TRANSACTION"
    CONSEIL = "CONSEIL"
    SERVICE_CLIENT = "SERVICE_CLEINT"
    CREDIT = "CREDIT"
    CONFORMITE = "CONFORMITE"


class AgentSchema(BaseModel):
    nom: str
    prenoms: str
    annee_de_naissance: str  # Utilisez str pour correspondre à Prisma
    categorie: str = "TRANSACTION"
    date_enregistrement: datetime = Field(default_factory=datetime.now)
    email: str
    telephone: str = None

    class Config:
        from_attributes = True

class AgentSchemaResponse(AgentSchema):
    agent_id: str

class AgentUpdate(BaseModel):
    nom: str
    prenoms: str
    annee_de_naissance: str
    categorie: str = "TRANSACTION"
    email: str
    telephone: str = None
    