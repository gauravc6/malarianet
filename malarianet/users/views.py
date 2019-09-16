from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_suer, logout_user, login_required
from malarianet import db
from malarianet.users import User
