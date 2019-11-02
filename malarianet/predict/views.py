import cv2
from flask import Blueprint, render_template, redirect,url_for
from flask_login import login_required
from malarianet import model
from malarianet.predict.forms import UploadImage
from malarianet.predict.image_handler import preprocess

predict = Blueprint("predict",__name__)

@predict.route('/upload',methods=['GET','POST'])
@login_required
def upload():
    form = UploadImage()

    if form.validate_on_submit():
        global image
        img_data = form.picture.data
        image = preprocess(img_data)
        return redirect(url_for('predict.result'))
    return render_template('upload.html',form=form)

@predict.route('/result',methods=['GET','POST'])
@login_required
def result():
    if image.shape!=():
        result = model.predict_classes(image)
    else:
        return redirect(url_for('predict.upload'))

    return render_template('result.html',result=result)
