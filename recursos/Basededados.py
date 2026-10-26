import psycopg2
from django.conf import settings


def obter_ligacao():
    db = settings.DATABASES['default']
    return psycopg2.connect(
        dbname=db['NAME'],
        user=db['USER'],
        password=db['PASSWORD'],
        host=db['HOST'],
        port=db['PORT'],
    )


def inserir_cliente(nome, nif):
    ligacao = obter_ligacao()
    try:
        with ligacao.cursor() as cursor:
            cursor.execute("CALL inserir_cliente(%s, %s);", (nome, nif))
        ligacao.commit()
    finally:
        ligacao.close()


def listar_clientes():
    ligacao = obter_ligacao()
    try:
        with ligacao.cursor() as cursor:
            cursor.execute("SELECT * FROM listarclientes;")
            return cursor.fetchall()
    finally:
        ligacao.close()