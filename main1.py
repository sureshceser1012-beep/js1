from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime
import time

app = FastAPI()

# Cache
prime_cache = None

# Rate limit
request_log = {}


def generate_primes(limit=10000):
    primes = []

    for num in range(2, limit + 1):
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


@app.get("/status")
def status():
    return {
        "message": "Server is healthy",
        "timestamp": datetime.now()
    }


@app.get("/primes")
def get_primes(request: Request):
    global prime_cache

    client_ip = request.client.host
    current_time = time.time()

    # Rate limiting
    if client_ip not in request_log:
        request_log[client_ip] = []

    request_log[client_ip] = [
        t for t in request_log[client_ip]
        if current_time - t < 60
    ]

    if len(request_log[client_ip]) >= 5:
        return JSONResponse(
            status_code=429,
            content={"error": "Rate limit exceeded. Try again later."}
        )

    request_log[client_ip].append(current_time)

    # In-memory cache
    if prime_cache is None:
        prime_cache = generate_primes()

    return {
        "count": len(prime_cache),
        "primes": prime_cache
    }