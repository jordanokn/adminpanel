from dependency_injector import containers, providers
from core.db import AsyncDB
from config.envs import Envs

class Container(containers.DeclarativeContainer):
    envs = providers.Singleton(Envs)

    db = providers.Singleton(
        AsyncDB,
        host=providers.Callable(lambda e: e.db_host, envs),
        port=providers.Callable(lambda e: e.db_port, envs),
        dbname=providers.Callable(lambda e: e.db_dbname, envs),
        user=providers.Callable(lambda e: e.db_user, envs),
        password=providers.Callable(lambda e: e.db_password, envs),
        connection_pool_min_size=providers.Callable(lambda e: e.db_connection_pool_min_size, envs),
        connection_pool_max_size=providers.Callable(lambda e: e.db_connection_pool_max_size, envs),
    )

container = Container()

def get_db() -> AsyncDB:
    return container.db()

def get_envs() -> Envs:
    return container.envs()

