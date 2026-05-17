"""
ConnectX Flask application entry point.
Creates the app instance, loads config, initializes extensions, and registers routes.
"""
from flask import Flask

from config import Config
from extensions import db


def create_app(config_class=Config):
    """Application factory."""
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    app.config.from_object(config_class)

    db.init_app(app)

    # Register blueprints
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.profile import profile_bp
    from routes.posts import posts_bp
    from routes.likes import likes_bp
    from routes.comments import comments_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(likes_bp)
    app.register_blueprint(comments_bp)

    # ---- AUTOMATICALLY CREATE DATABASE TABLES ----
    with app.app_context():
        try:
            # Explicitly importing all models matching your singular naming scheme
            from models.user import User
            from models.profile import Profile
            from models.post import Post
            from models.comment import Comment
            from models.like import Like          
            from models.connection_test import ConnectionTest
            from models.reported_content import ReportedContent  # <-- Added for automatic table initialization
            
            db.create_all()  # Generates all missing tables at once in MySQL
            print("Database tables verified/created successfully.")
        except Exception as e:
            print(f"Error creating database tables: {e}")
    # -----------------------------------------------

    # Inject current_user from session for nav and access control.
    @app.context_processor
    def inject_current_user():
        from flask import session
        from models.user import User
        user_id = session.get("user_id")
        current_user = db.session.get(User, user_id) if user_id else None
        return {"current_user": current_user}

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=5001)