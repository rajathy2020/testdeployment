""" This file holds all the routers required to interact with User and API key """
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
import string
import os
router = APIRouter()


@router.get("/users/me", include_in_schema=bool(os.getenv("SHOW_OPEN_API_ENDPOINTS")))
async def read_users_me(request: Request):
    """Get the system user"""
    return "hello"
