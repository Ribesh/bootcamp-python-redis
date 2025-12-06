from flask import Flask
import redis
import psycopg2

app = Flask(__name__)

r = redis.Redis(host="redis", port=6379)

@app.route("/")
def check_redis():
    try:
        r.ping()
        return "Redis is UP!"
    except:
        return "Redis is DOWN!"

@app.route("/db")
def check_postgres():
    try:
        conn = psycopg2.connect(
            host="postgres",
            #database="ribesh",
            user="postgres",
            password="P@ssw0rd01"
        )
        conn.close()
        return "Postgres is UP!"
    except:
        return "Posgres is DOWN!"
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
