from fastapi import FastAPI
import redis
import json

app = FastAPI()
cache = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # Cache check
    cached = cache.get(f"user:{user_id}")
    if cached:
        return {"source": "cache", "data": json.loads(cached)}
    
    # Database simulation
    user = {"user_id": user_id, "name": "Vedika"}
    
    # Cache store - 30 seconds TTL
    cache.setex(f"user:{user_id}", 30, json.dumps(user))
    
    return {"source": "database", "data": user}

