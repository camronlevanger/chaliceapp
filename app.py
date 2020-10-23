from chalice import Chalice


app = Chalice(app_name='chalice-app')

from base import Session, engine, Base
from models import User, UserTeams, Team

session = Session()

@app.route('/create_schema')
def create_schema():
    Base.metadata.create_all(engine)

@app.route('/teams/{name}', methods=['POST'])
def create_team(name):
    session.add(Team(name))
    return {"team": name}

@app.route('/users/{team_id}', methods=['GET'])
def list_users(team_id, sort=False):
    if app.current_request.query_params['sort'] == "true":
        sort = True
    users = session.query(UserTeams) \
    .filter(UserTeams.team_id == team_id) \
    .all()
    return users
    #select team, users, position filter by position and active

@app.route('/teams/{user_id}', methods=['GET'])
def list_teams(user_id, sort=False):
    if app.current_request.query_params['sort'] == "true":
        sort = True
    users = session.query(UserTeams) \
    .filter(UserTeams.user_id == user_id) \
    .all()
    return users
    #select users, teams sort by active, sort

@app.route('/users/{email}', methods=['POST'])
def create_user(email):
    session.add(User(email=email))
    return {'user': email}

def team_add_member(team_id, user_id, position):
    return True
    # find team, user and create association

def team_update_member(team_id, user_id, position, active):
    return True
    # find user, team update position and active
@app.route('/')
def index():
    return {'hello': 'world'}

session.commit()
session.close()
