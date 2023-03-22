from flask import Flask

app = Flask(__name__)


from .intro.routes import resume_b

app.register_blueprint(resume_b)
