from django.db import transaction

# función que, dependiendo del caso, hacemos un rollback de los datos
def rollback_data(type : int):
    match type:
        # caso de las tres bases de datos principales
        case 1:
            transaction.set_rollback(True)
            transaction.set_rollback(True, using='stock_product')
            transaction.set_rollback(True, using='mirror_database')
        # caso de la autoreplica y la base de datos color
        case 2:
            transaction.set_rollback(True, using='color')
            transaction.set_rollback(True, using='mirror_database')
        # caso de la autoreplica y la base de datos default
        case 3:
            transaction.set_rollback(True)
            transaction.set_rollback(True, using='mirror_database')