from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name="fk_expense_user"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', name="fk_expense_category"), nullable=False)

    def __repr__(self):
        return f"<Expense {self.amount}>"

class Status(Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in progress"

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',name="fk_goal_user"), nullable=False)
    amount = db.Column(db.Float, nullable=False,default=0.0)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    collected_amount = db.Column(db.Float, nullable=False,default=0.0)
    status = db.Column(db.Enum(Status), name="goal_status_enum", nullable=False, default=Status.IN_PROGRESS)
    
    def __repr__(self):
        return f"<Goal {self.amount}>"

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',name="fk_income_user"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id',name="fk_income_category"), nullable=False)

    def __repr__(self):
        return f"<Income {self.amount}>"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"




