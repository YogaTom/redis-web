from flask import Flask
import redis
import os

app = Flask(__name__)

# 从环境变量获取 Redis 配置
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("counter")  # 每次访问 +1
    return f"<h1>Hello! This page has been viewed {count} times.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

