from app import db
from enum import Enum

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