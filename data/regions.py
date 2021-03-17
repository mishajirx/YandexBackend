import sqlalchemy
from data.db_session import SqlAlchemyBase


class Region(SqlAlchemyBase):
    __tablename__ = 'regions'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    courier_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    region = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
