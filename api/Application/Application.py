from fastapi import FastAPI, APIRouter, Depends, Request, status
from psycopg.rows import dict_row
from typing import List
import logging

from api.Application.model import Application


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

router = APIRouter()
app = FastAPI()

@router.post('/applications', status_code=status.HTTP_200_OK, name="Get all applications", response_model=List[Application])
async def post_application(
        request: Request
        
    ):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM application.applications"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results
        
@router.get('/application/{account_id}', status_code=status.HTTP_200_OK, name="Get account by applicationid", response_model=List[Application])
async def get_application(account_id, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT * 
                FROM application.applications WHERE account_id = %s""", (account_id,))
            results = await cur.fetchall()
            logger.info(results)
            return results