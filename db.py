from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass

class Test(Base):
    __tablename__ = 'test'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


if __name__ == '__main__':
    engine = create_engine('sqlite:///data.db', echo=True)
    Base.metadata.create_all(engine)
