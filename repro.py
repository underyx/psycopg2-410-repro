from gevent import monkey; monkey.patch_all()
from psycogreen.gevent import patch_psycopg; patch_psycopg()

from gevent import spawn
from gevent.pool import Pool
import psycopg2
from sqlalchemy import create_engine
import time

engine = create_engine('postgresql://postgres:postgres@db/postgres')


def killy(greenlets):
    for greenlet in greenlets:
        time.sleep(0.001)
        greenlet.kill()


def sleepy():
    try:
        conn = engine.raw_connection()
        cur = conn.cursor()
        cur.execute('SELECT pg_sleep(0.1)')
        cur.close()
        conn.close()
    except:
        import traceback; traceback.print_exc()


def main():
    pool = Pool()
    for _ in range(100):
        greenlets = [pool.apply_async(sleepy) for _ in range(100)]
        spawn(killy, greenlets)
        pool.join()


if __name__ == '__main__':
    main()
