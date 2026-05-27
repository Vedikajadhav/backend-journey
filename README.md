# backend-engineering

Production-grade backend concepts, implemented from scratch.

## Stack
Linux · PostgreSQL · FastAPI · Docker · Redis · AWS

## Modules
| Module | Concepts | Status |
|--------|----------|--------|
| 01-linux | processes, signals, file descriptors | ✅ |
| 02-networking | TCP/IP, DNS, HTTP, sockets | ✅ |
| 03-databases | PostgreSQL, ACID, indexes, transactions | ✅ |
| 04-fastapi | REST, validation, auto docs | ✅ |
| 05-docker | containers, compose, networking | 🔄 |
| 06-redis | caching, TTL, eviction | ⏳ |
| 07-system-design | LB, sharding, CAP theorem | ⏳ |

## Run locally
cd 04-fastapi && uvicorn main:app --reload
