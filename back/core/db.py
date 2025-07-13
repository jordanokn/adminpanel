from typing import Any, AsyncGenerator

from psycopg import AsyncCursor, sql
from psycopg_pool import AsyncConnectionPool


class AsyncDB:
    """
    Асинхронная обертка для работы с PostgreSQL через psycopg3 с пулом соединений.
    Пул инициализируется один раз при создании экземпляра класса.

    Пример использования:
    db = AsyncDB(
        host="localhost",
        port=5432,
        dbname="your_db",
        user="your_user",
        password="your_password",
        connection_pool_min_size=2,
        connection_pool_max_size=10
    )
    TODO: для доступа к другим дб нужно еще сделать асинхронный контекстный менеджер, для удобства
    """

    _connection: Any = None

    def __init__(
        self,
        host: str,
        port: int,
        dbname: str,
        user: str,
        password: str,
        connection_pool_min_size: int = 1,
        connection_pool_max_size: int = 10,
    ) -> None:
        conninfo = (
            f"host={host} port={port} dbname={dbname} user={user} password={password}"
        )
        self._pool = AsyncConnectionPool(
            conninfo=conninfo,
            min_size=connection_pool_min_size,
            max_size=connection_pool_max_size,
            open=False,
        )

    async def connect(self):
        await self._pool.open()
        async with self._pool.connection() as con:
            self._connection = con

    async def cursor(self, row_factory) -> AsyncGenerator[AsyncCursor, None]:
        if not self._connection:
            raise RuntimeError(
                "Database pool is not initializated. Please use .connect()"
            )

        async with self._connection.cursor(row_factory=row_factory) as cur:
            yield cur


if __name__ == "__main__":
    import asyncio

    async def test(db):
        r = db.cursor()
        async for c in r:
            await c.execute(
                sql.SQL("select * from users order by datetime_created desc")
            )
            print(await c.fetchone())

    async def main():
        db = AsyncDB("localhost", 5432, "fiah", "postgres", "pass")
        await db.connect()
        await asyncio.gather(*[test(db) for _ in range(10)])

    asyncio.run(main())
