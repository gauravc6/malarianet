from flask import Blueprints, render_template
from malarianet.predict.forms import UploadImage
from model_handler import loadmodel, final_predict, preprocess

predict = Blueprint("predict",__name__)

@predict.route('/upload',methods=['GET','POST'])
def upload():
    form = UploadImage()

    if form.validate_on_submit():
        global image = preprocess(form.picture.data)
        return redirect(url_for('predict.result'))
    return render_template('upload.html')

@def.route('/result',methods=['GET','POST'])
def result():
    result = final_predict(image)
    render_template('result.html',result=result)
