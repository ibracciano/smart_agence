from pydantic import BaseModel
from datetime import datetime, date
from enum import Enum
from typing import Optional

class StatutTicket(Enum):
    EN_ATTENTE = "EN_ATTENTE"
    EN_COURS = "EN_COURS"
    VALIDE = "VALIDE"
    ECHEC = "ECHEC"

class StatutTicketSchema(BaseModel):
    agent_id: Optional[str] = None
    numero_ticket: int
    date: date
    heure: datetime.time
    # statut: StatutTicket

    class Config:
        from_attributes = True

class StatutTicketSchemaResponse(BaseModel):
    agent_id: str
    numero_ticket: int
    date: date
    heure: datetime.time
    statut: str