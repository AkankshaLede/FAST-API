from fastapi import FastAPI, APIRouter, Depends, Request, status
from psycopg.rows import dict_row
from typing import List
import logging

from api.account.model import Account


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

router = APIRouter()
app = FastAPI()

'''@app.post("/newpost")
def postdata(account: Account):
    post_dict = dict(account)
    return {"account": post_dict}

@app.get("/newcreate")
def getaccounts(account: Account):
    get_dict = dict(account)
    return {"account": get_dict}


'''

@router.get('/account/{id}', status_code=status.HTTP_200_OK, name="Get account by accountid", response_model=List[Account])
async def get_account(id: str, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT * 
                FROM account.accounts WHERE id = %s""", (id,))
            results = await cur.fetchall()
            logger.info(results)
            return results



@router.post('/accounts', status_code=status.HTTP_200_OK, name="Get all accounts", response_model=List[Account])
async def get_account(
        request: Request
        
    ):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                SELECT *
                FROM account.accounts"""
            )
            results = await cur.fetchall()
            logger.info(results)
            return results



@router.post('/account', status_code=status.HTTP_201_CREATED, name="Create an account")
async def create_account(account: Account, request: Request):
    async with request.app.async_pool.psyco_async_pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
                INSERT INTO
                account.accounts (account_id, account_name, account_email)
                VALUES (%s, %s, %s)""", (account.id, account.account_name, account.account_email)
            )
            await conn.commit()
            logger.info(f"Account created: {account.id}")
            return {"message": "Account created successfully", "account_id": account.id}

