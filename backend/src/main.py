from fastapi import FastAPI
from .db.db_setup import engine, Base
# from .entities.todo import Todo         # Import models to register them
# from .entities.user import User         # Import models to register them
from .core.api import register_routes   
from .core.logging import configure_logging, LogLevels     

configure_logging(LogLevels.info)

app = FastAPI()     

"""Only uncomment below to create new tables, 
otherwise the tests will fail if not connected
"""
# Base.metadata.create_all(bind=engine)

register_routes(app)