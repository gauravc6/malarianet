from flask import Blueprints, render_template
from malarianet.predict.forms import UploadImage

predict = Blueprint("predict",__name__)
