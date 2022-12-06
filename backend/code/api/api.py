""" This file is the entrypoint for the backed api's"""
import os
from os import path
from fastapi import FastAPI
from .routers import users

root_path = ""


app = FastAPI(
    root_path=root_path,
    description="Documentation for External Fraud Detection  API",
)

app.include_router(users.router, tags=["Users"])
