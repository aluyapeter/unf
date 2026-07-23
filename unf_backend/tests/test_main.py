import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.main import app, get_db

TEST_DATABASE_URL = "postgresql+asyncpg://unf:unf_dev_password@localhost:5432/unf_db"

test_engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = async_sessionmaker(bind=test_engine, expire_on_commit=False)

async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

@pytest.mark.asyncio
async def test_db_health_check():
    """
    Test that the database health endpoint returns a 200 OK 
    and confirms the connection.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/health/db")
    
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok", 
        "message": "Database connected successfully!"
    }