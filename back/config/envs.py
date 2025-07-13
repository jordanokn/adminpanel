import dotenv
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Envs(BaseSettings):

    db_host: str
    db_port: int
    db_dbname: str
    db_user: str
    db_password: str
    db_connection_pool_min_size: int = 1
    db_connection_pool_max_size: int = 10

    @property
    def database_uri(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_dbname}"
