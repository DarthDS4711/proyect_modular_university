# archivo base de datos elegida por default por el programa
DATABASES_APPLICATION = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'applicationwebdata',
        'USER' : 'postgres',
        'HOST' : 'localhost',
        'PORT' : '5432',
        'PASSWORD' : '123456', 
    }
}

# En esta seccion se listaran las bases de datos secundarias del programa
