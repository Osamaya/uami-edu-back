import jwt
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
load_dotenv(override=True)

SECRET_KEY =  os.getenv("SECRET_KEY")
ALGORITHM =  os.getenv("ALGORITHM")

# Usa la misma clave secreta que PHP
SECRET_KEY = SECRET_KEY
ALGORITHM = ALGORITHM

# Middleware de autenticación con JWT
security = HTTPBearer()

# Middleware de autenticación con JWT
def verify_jwt(request: Request):
    # Depuración: Imprime todas las cookies recibidas
    # print("Cookies recibidas:", request.cookies)

    # Obtener el token de las cookies
    token = request.cookies.get("jwt")
    # print("Token de cookies:", token)

    # Si no está en cookies, verificar headers
    if not token:
        auth_header = request.headers.get("Authorization")
        print("Authorization header:", auth_header)
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            print("Token de header:", token)

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Token no proporcionado",
            headers={"WWW-Authenticate": "Bearer"}
        )

    try:
         # Depuración: Ver el token antes de decodificar
        # print("Token a decodificar:", token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print(f"soy el payload {payload}")
        
        # print("Payload decodificado:", payload)
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except jwt.InvalidTokenError as e:
        print("Error decodificando token:", str(e))
        raise HTTPException(
            status_code=401,
            detail=f"Token inválido: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"}
        )