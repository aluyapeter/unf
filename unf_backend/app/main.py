from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import AsyncSessionLocal

app = FastAPI()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/health")
def health():
    return {
        "status": "ok", 
        "message": "UNF backend is Healthy"
    }

@app.get("/health/db")
async def db_health(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    
    return {
        "status": "ok", 
        "message": "Database connected successfully!"
    }