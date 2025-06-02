from src.schemas.ticket_schema import TicketSchema, TicketSchemaResponse, TicketStatusSchema
from src.utils.extract_hour import extraire_heure
from config.config import db
from typing import List
from datetime import datetime


class TicketService:

    # creer un ticket
    async def creer_ticket(self, ticket: TicketSchema) -> TicketSchemaResponse:
        ticket_dict = ticket.model_dump()
        # print("Données du ticket à créer:", ticket_dict)

        # ticket_dict.pop("id", None)

        # print("Tentative de création du ticket dans la base de données...")
        ticket_created = await db.ticket.create(data={
            "categorie_service_concernee": ticket_dict["categorie_service_concernee"],
            "numero_ticket": ticket_dict["numero_ticket"],
            "description": ticket_dict["description"],
            "status":{
                "create":{
                    "numero_ticket":ticket_dict["numero_ticket"],
                    "statut": "EN_ATTENTE",
                }
            }
            
        })
        # print("Ticket créé:", ticket_created)

        ticket_created_dict = ticket_created.model_dump()
        
        print("Statut initial créé pour le ticket:", ticket_created_dict)

        return TicketSchemaResponse(**ticket_created_dict)
    
    # obternir tous les tickets
    async def all_ticket(self) -> List[TicketSchemaResponse]:
        datas = await db.ticket.find_many(include={
            "status": True,
            "agent": True
        })
        if not datas:
            return []
        return [TicketSchemaResponse(**data.model_dump()) for data in datas]
    

# creer un ticket
    async def update_status(self, agent_id: str, status: TicketStatusSchema) -> str:
        status_dict = status.model_dump()
        # print("Données du statut à mettre à jour:", status_dict.get('status'), agent_id)

        agent_exist = await db.agent.find_first(where={"agent_id": agent_id})
        # print("agent_exist", agent_exist.model_dump())

        if not agent_exist:
            return "NOT PERMITTED"
        
        
        await db.ticket.update(
            where={
                "numero_ticket": status_dict["numero_ticket"]
            },
            data={
                "agent_id": agent_id
            }
        )
        
        await db.status.update(
            where={
                # "agent_id": agent_id,
                "numero_ticket": status_dict.get("numero_ticket")
            },
            data={
                'agent_id' : agent_id,
                'statut' : status_dict['status']
            }
            
        )
        # print('result', result)
        return "OK"