from flask import Blueprint, render_template
from malarianet.predict.forms import UploadImage
from malarianet.predict.model_handler import final_predict, preprocess

predict = Blueprint("predict",__name__)

@predict.route('/upload',methods=['GET','POST'])
def upload():
    form = UploadImage()

    if form.validate_on_submit():
        image = preprocess(form.picture.data)
        return redirect(url_for('predict.result'))
    return render_template('upload.html')

@predict.route('/result',methods=['GET','POST'])
def result():
    if upload.image:
        result = final_predict(upload.image)
    else:
        redirect(url_for('predict.upload'))

    render_template('result.html',result=result)
