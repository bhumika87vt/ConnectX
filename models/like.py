"""Like model — maps to likes table (Task 12). Connects a user to a post."""
from datetime import datetime
from extensions import db


class Like(db.Model):
    """Maps to likes table. Handles user likes on individual posts."""

    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships linking back to User and Post models
    user = db.relationship("User", backref=db.backref("likes", lazy="dynamic"))
    post = db.relationship("Post", backref=db.backref("likes", lazy="dynamic"))

    def __repr__(self):
        return f"<Like user_id={self.user_id} post_id={self.post_id}>"