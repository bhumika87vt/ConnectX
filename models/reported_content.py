"""ReportedContent model — maps to reported_content table (Task 15)."""
from datetime import datetime
from extensions import db


class ReportedContent(db.Model):
    """Maps to reported_content table. Tracks flags on bad posts/comments."""

    __tablename__ = "reported_content"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_type = db.Column(db.String(50), nullable=False)  # 'post' or 'comment'
    content_id = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ReportedContent id={self.id} type={self.content_type}>"