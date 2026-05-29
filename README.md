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
| 04-fastapi | REST, validation, auto docs, Redis caching | ✅ |
| 05-projects | URL Shortener — FastAPI + PostgreSQL + Redis | ✅ |
| 06-docker | containers, compose, networking | ✅ |
| 07-system-design | LB, CAP, Sharding | ✅ |

## Projects
- **URL Shortener** — bit.ly clone with caching

## Run locally
cd 04-fastapi && uvicorn main:app --reload
