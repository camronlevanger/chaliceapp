# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, Boolean, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship

from base import Session, engine, Base

class UserTeams(Base):
    __tablename__ = 'user_teams'
    __table_args__ = (Index('idxteamposuser', team_id, user_id, position , unique=True) )
    team_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)
    position = Column(String(50))
    active = Column(Boolean, default=True)
    child = relationship("Team", back_populates="users")
    parent = relationship("User", back_populates="teams")
    


class Team(Base):
    __tablename__ = 'teams'
    id=Column(Integer, primary_key=True)
    name=Column('title', String(32))
    users = relationship(
        "User",
        secondary=user_teams,
        back_populates="team")


class User(Base):
    __tablename__ = 'users'
    id=Column(Integer, primary_key=True)
    email=Column('title', String(120), unique=True)
    teams = relationship(
        "Team",
        secondary=user_teams,
        back_populates="users")


session = Session()

def create_team(name):
    session.add(Team(name))

def list_users(name, sort):
    #select team, users, position filter by position and active

def list_teams(email, sort):
    #select users, teams sort by active, sort

def create_user(email):
    session.add(User(email=email))

def team_add_member(team_id, user_id, position):
    # find team, user and create association

def team_update_member(team_id, user_id, position, active):
    # find user, team update position and active

