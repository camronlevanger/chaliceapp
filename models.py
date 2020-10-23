# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, Boolean, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship

from base import Session, engine, Base

class UserTeams(Base):
    __tablename__ = 'user_teams'
    team_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)
    position = Column(String(50))
    active = Column(Boolean, default=True)
    team = relationship("Team", back_populates="users")
    user = relationship("User", back_populates="teams")
    __table_args__ = (Index('idxteamposuser', team_id, user_id, position , unique=True) )
    


class Team(Base):
    __tablename__ = 'teams'
    id=Column(Integer, primary_key=True)
    name=Column('title', String(32))
    users = relationship(
        "UserTeams",
        back_populates="teams")


class User(Base):
    __tablename__ = 'users'
    id=Column(Integer, primary_key=True)
    email=Column('title', String(120), unique=True)
    teams = relationship(
        "UserTeams",
        back_populates="users")
