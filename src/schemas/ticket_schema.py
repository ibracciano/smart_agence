from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional, List

from src.schemas.agent_schema import AgentSchemaResponse

class CategorieService(Enum):
    TRANSACTION = "TRANSACTION"
    CONSEIL = "CONSEIL"
    SERVICE_CLIENT = "SERVICE_CLEINT"
    CREDIT = "CREDIT"
    CONFORMITE = "CONFORMITE"


class TicketSchema(BaseModel):
    categorie_service_concernee: str = "TRANSACTION"
    description: Optional[str] = None  # Description optionnelle
    numero_ticket: str


    class Config:
        from_attributes = True

class TicketStatusSchema(BaseModel):
    numero_ticket: str
    status: str 

class StatusSchema(BaseModel):
    statut: str
    numero_ticket: str
    updated_date: datetime


class TicketSchemaResponse(BaseModel): 
    id: str
    agent_id: Optional[str] = None  # L'agent en charge peut être nul au départ
    date_heure_creation: datetime
    categorie_service_concernee: str
    description: Optional[str] = None  # Description optionnelle, avec limite de longueur

    agent: Optional[AgentSchemaResponse] = None
    status: Optional[StatusSchema]


