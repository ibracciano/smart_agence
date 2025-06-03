import logging
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from src.schemas.agent_schema import AgentSchemaResponse, AgentSchema, AgentUpdate
from src.services.agent_service import AgentService

# create logger
logger = logging.getLogger(__name__)
agent_router = APIRouter()


# route pour obtenir tous les agents
@agent_router.get('/agents/', response_model=List[AgentSchemaResponse], status_code=status.HTTP_200_OK)
async def get_all_agents(agent_service : AgentService = Depends()) -> dict:
    try:
        agents = await agent_service.all_agent()
        return agents

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# route pour creer un agent
@agent_router.post('/agents/', response_model=AgentSchemaResponse, status_code=status.HTTP_201_CREATED)
async def create_agent(agent:AgentSchema, agent_service : AgentService = Depends()) -> dict:
    # agent = None
    try:
        agent = await agent_service.creer_agent(agent)
        
        return agent

    except Exception as e:
        # if not agent: 
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Agent existe déjà')
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
# route pour supprimer un agent
@agent_router.delete('/agents/{agent_id}', response_model=AgentSchemaResponse, status_code=status.HTTP_200_OK)
async def delete_agent(agent_id : str, agent_service : AgentService = Depends()) -> dict:
    try:
        agent = await agent_service.delete_agent(agent_id)
        if agent == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found")
        if agent == "NOT PERMITTED":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non autorisé")
        return agent

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

# route pour mettre à jour un agent
@agent_router.put('/agents/{agent_id}', response_model=AgentSchemaResponse, status_code=status.HTTP_200_OK)
async def update_agent(agent_id : str, agent:AgentUpdate, agent_service : AgentService = Depends()) -> dict:
    try:
        agent = await agent_service.update_agent(agent_id, agent)
        if agent == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found")
        
        return agent

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

# route pour connecter un agent
@agent_router.get("/agents/signin/{email}", response_model=AgentSchemaResponse, status_code=status.HTTP_202_ACCEPTED)
async def connect_agent(email : str, agent_sevice : AgentService = Depends()) -> dict:
    try:
        agent = await agent_sevice.connect_agent(email=email)
        if agent == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agent non trouvé")
        
        return agent
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))