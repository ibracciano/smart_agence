import logging
from fastapi import APIRouter, Depends, status, HTTPException
from src.schemas.ticket_schema import TicketSchema, TicketSchemaResponse, TicketStatusSchema
from src.services.ticket_service import TicketService
from typing import List

# create logger
logger = logging.getLogger(__name__)
ticket_router = APIRouter()


# route pour creer un ticket
@ticket_router.post('/tickets/', response_model=TicketSchemaResponse, status_code=status.HTTP_201_CREATED)
async def create_ticket(ticket:TicketSchema, ticket_service : TicketService = Depends()) -> dict:
    # print("Tentative de création du ticket...")
    try:
        ticket = await ticket_service.creer_ticket(ticket)
        # print("ticket", ticket)
        return ticket

    except Exception as e:
        # if not ticket: 
        #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Erreur de creation')
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

# route pour obtenir tous les tickets
@ticket_router.get('/tickets/', response_model=List[TicketSchemaResponse], status_code=status.HTTP_200_OK)
async def get_all_tickets(ticket_service : TicketService = Depends()) -> dict:
    try:
        tickets = await ticket_service.all_ticket()
        return tickets

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

# route pour modifier le status d'un client
@ticket_router.put('/tickets/update/{agent_id}', status_code=status.HTTP_200_OK)
async def update_status(agent_id: str, status_schema: TicketStatusSchema,  ticket_service : TicketService = Depends()):
    try:
        result = await ticket_service.update_status(agent_id, status_schema)
        print("result", result)
        if result == "NOT PERMITTED":
            return {"status_code" : status.HTTP_401_UNAUTHORIZED, "message" : "Veuillez vous connecter"}
        elif result == "OK":
            return {"status_code" : status.HTTP_200_OK, "message" : "Modification Effectuée"}
        else: 
            return {"status_code" : status.HTTP_304_NOT_MODIFIED, "message" : "Problème"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))