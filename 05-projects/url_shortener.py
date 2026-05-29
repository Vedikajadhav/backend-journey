from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import psycopg2
import random
import string

app = FastAPI()
cache = redis.Redis(host='localhost', port=6379, db=0)

# Database connection
conn = psycopg2.connect(
    dbname="myapp",
    user="postgres",
    password="password123",
    host="localhost"
)
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id SERIAL PRIMARY KEY,
        short_code VARCHAR(10) UNIQUE,
        long_url TEXT,
        clicks INTEGER DEFAULT 0
    )
""")
conn.commit()

class URLRequest(BaseModel):
    long_url: str

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.post("/shorten")
def shorten_url(request: URLRequest):
    code = generate_code()
    cursor.execute("INSERT INTO urls (short_code, long_url) VALUES (%s, %s)", 
                   (code, request.long_url))
    conn.commit()
    return {"short_url": f"http://localhost:8000/{code}"}

@app.get("/{code}")
def redirect(code: str):
    # Check cache first
    cached = cache.get(f"url:{code}")
    if cached:
        return {"url": cached.decode(), "source": "cache"}
    
    # Check database
    cursor.execute("SELECT long_url FROM urls WHERE short_code = %s", (code,))
    result = cursor.fetchone()
    
    if not result:
        raise HTTPException(status_code=404, detail="URL not found")
    
    # Store in cache
    cache.setex(f"url:{code}", 3600, result[0])
    
    return {"url": result[0], "source": "database"}
