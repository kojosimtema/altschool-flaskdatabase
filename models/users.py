from app import db
from sqlalchemy.sql import func

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    # registerd_on = db.Column(db.DateTime, default=func.now())
    # updated_on = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # password_hash = db.Column(db.String(100))
    # role = db.relationship('Role', secondary='user_role', backref=db.backref('users', lazy='joined'), uselist=False)

    def __repr__(self):
        return '<user %r>' % self.username

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}


# class Role(db.Model):

#     __tablename__ = "roles"

#     id = db.Columns(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Columns(db.String(50), unique=True)

#     def as_dict(self):
#         return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}


# class UserRoles(db.model):

#     __table__name = "user_roles"

#     id = db.Columns(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Columns(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
#     role_id = db.Columns(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))

#     def as_dict(self):
#         return {c.name: getattr(self, c.name) for c in self.__tablename__.columns}
