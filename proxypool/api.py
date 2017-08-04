from flask import Flask, g,jsonify

from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    """
    Opens a new redis connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'redis_client'):
        g.redis_client = RedisClient()
    return g.redis_client


@app.route('/')
def index():
    """
    Get a proxy
    """
    conn = get_conn()
    print(conn.queue_all)
    return jsonify(conn.queue_all)


@app.route('/get')
def get_proxy():
    """
    Get a proxy
    """
    conn = get_conn()
    return conn.pop()


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    """
    conn = get_conn()
    print(conn.queue_len)
    return str(conn.queue_len)


# @app.route('/lists')
# def get_proxy_list():
#     """
#     Get a proxy
#     """
#     conn = get_conn()
#     print(conn.queue_all)
#     return jsonify(conn.queue_all)

if __name__ == '__main__':
    app.run(debug=True)
