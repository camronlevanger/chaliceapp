# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, Boolean, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship

from base import Session, engine, Base

user_teams = Table('userteams', Base.metadata,
    Column('team_id', Integer, ForeignKey('teams.id')),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('position_id', Integer, ForeignKey('positions.id')),
    UniqueConstraint('team_id', 'user_id', "position_id", name='uix_team_user_pos')
)

Index('idxteamposuser', user_teams.c.team_id, user_teams.c.user_id, user_teams.c.position_id , unique=True)

class UserTeams(Base):
    __tablename__ = 'user_teams'
    __table_args__ = (Index('idxteamposuser', user_teams.c.team_id, user_teams.c.user_id, user_teams.c.position , unique=True) )
    team_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
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

