
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Configuración de la URL de conexión a MySQL
URL_BASE_DATOS = "mysql+pymysql://root:123456@127.0.0.1:3306/gestion_salas_itesz"

# 2. Creación del "Motor" (Engine) de la base de datos
engine = create_engine(URL_BASE_DATOS)

# 3. Configuración de la Sesión (La que ejecutará las consultas)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Clase Base de la que heredarán nuestros modelos
Base = declarative_base()

# 5. Dependencia para inyectar la base de datos en las rutas (endpoints)
def obtener_bd():
    bd = SessionLocal()
    try:
        yield bd
    finally:
        bd.close()