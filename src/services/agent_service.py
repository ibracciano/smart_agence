from src.schemas.agent_schema import AgentSchema, AgentSchemaResponse, AgentUpdate
from config.config import db
from typing import List

class AgentService:
    # creer un agent
    async def creer_agent(self, agent:AgentSchema) -> AgentSchemaResponse:
        # print("agent", agent)
        agen_dict = agent.model_dump()
        # print(agen_dict)
        # data_search = await db.agent.find_first(where={"email" : agen_dict['email']})

        # print(data_search)
        # if not data_search:
        #     return None
        
        data = await db.agent.create(data=agen_dict)
        print("retour ", data)
        return AgentSchemaResponse(**data.model_dump())
    
    # obternir tous les agents
    async def all_agent(self) -> List[AgentSchemaResponse]:
        datas = await db.agent.find_many()
        if not datas:
            return []
        return [AgentSchemaResponse(**data.model_dump()) for data in datas]
    
    # mettre à jour un agent
    async def update_agent(self, agent_id: str, agent: AgentUpdate) -> AgentSchemaResponse:
        data_search = await db.agent.find_first(where={"agent_id" : agent_id})
        if not data_search:
            return None
        data_updated = await db.agent.update(where={"agent_id" : agent_id}, data=agent.model_dump())
        return AgentSchemaResponse(**data_updated.model_dump())
    
    # supprimer un agent
    async def delete_agent(self, agent_id: str) -> AgentSchemaResponse:
        data_search = await db.agent.find_first(where={"agent_id" : agent_id})
        # print(data_search)
        if not data_search:
            return None
        if data_search.role != "ADMINISTRATEUR":
            return "NOT PERMITTED"
        data_delete = await db.agent.delete(where={"agent_id" : agent_id})
        return AgentSchemaResponse(**data_delete.model_dump())
    

    #route pour connecter un agent
    async def connect_agent(self, email: str) -> AgentSchemaResponse:
        data_searh = await db.agent.find_first(where={
            "email": email
        })

        if not data_searh:
            return None
        
        return AgentSchemaResponse(**data_searh.model_dump())
