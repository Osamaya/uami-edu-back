from datetime import datetime
from functools import lru_cache,partial
import io
import json
import re
import shutil
import uuid
from bson import ObjectId
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import logging
import os
from fastapi import Depends, File, Form, HTTPException, FastAPI, APIRouter,BackgroundTasks, Request, UploadFile
from pathlib import Path
#Super importante para liberar el peso de las tareas en un hilo de ejecución y no bloquear nuestro thread principal
# from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Any, List, Dict, Optional
executor = ThreadPoolExecutor(max_workers=2)

import time
from app.config.auth import verify_jwt  

# from modelos.reports_model import Report
# from modelos.schemas import MongoRequest 
from app.db.mongo.reports_mongo import Report


from dotenv import load_dotenv
# Cargar las variables del archivo .env
load_dotenv()
load_dotenv(override=True)

import subprocess  # ✅ Esta es la correcta

# Importa la función que necesites
logger = logging.getLogger(__name__)

from fastapi.middleware.cors import CORSMiddleware
from app.middleware.corsmiddleware import CORSMiddlewareForStatic

app = FastAPI()

# Añades el middleware personalizado
app.add_middleware(CORSMiddlewareForStatic)

origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
    "http://10.203.218.96:8000",
    "http://10.203.218.96",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,  # Or specify the frontend's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

router = APIRouter()

logging.basicConfig(level=logging.INFO)