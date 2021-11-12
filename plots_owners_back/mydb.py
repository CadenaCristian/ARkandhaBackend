import psycopg2.pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager


host1 = 'localhost'
port1 = '5432'
dbname1 = 'plots_owners'
username = 'postgres'
passwordG = '1234'
dbpoolG = psycopg2.pool.ThreadedConnectionPool(
    5, 20, host=host1, port=port1, dbname=dbname1, user=username, password=passwordG)


@contextmanager
def db_cursor2():
    conn = dbpoolG.getconn()
    conn.set_client_encoding('UTF8')
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            yield cur
            conn.commit()
    except Exception as error:
        conn.rollback()
        raise
    finally:
        dbpoolG.putconn(conn)
