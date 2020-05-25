import redis
import os

host = os.getenv("REDIS_HOST") or "localhost"
port = os.getenv("REDIS_PORT") or 6379
r = redis.Redis(host, port)

r.set("test", "value")

print(r.get("test"))
# Print = b"value"
