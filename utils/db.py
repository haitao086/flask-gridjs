from flask_sqlalchemy import SQLAlchemy

import application

db = SQLAlchemy(application.app)