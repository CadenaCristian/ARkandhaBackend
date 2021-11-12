from ..mydb import db_cursor2


def valMessage(crudMessage, word, boolRequest):
    success = 'Se {} la {} exitosamente!'.format(crudMessage, word)
    error = 'fallo al {} la {}.'.format(crudMessage, word)
    obj = {
        "error": False if boolRequest == 1 else True,
        "message": success if boolRequest == 1 else error
    }
    return obj


def executyQuery(type, query):
    with db_cursor2() as db:
        print("query: ", query)
        db.execute(query)
        result = db.fetchall() if type == 'r' else db.rowcount
        return result
