
from flask import Blueprint,make_response, render_template, redirect, session
from flask_cors import  CORS, cross_origin
from markupsafe import escape
bp_courses = Blueprint("course", __name__, url_prefix='/course')
CORS(bp_courses)

from ..token_module.userTokenModel import UserToken
from .enroll.enroll_view import EnrollView
from .course.course import CourseModel
from .enroll.enroll import EnrollModel
from .payment.payment import PaymentModel
from app.configs_package import MySecureUtils


bp_courses.add_url_rule("/enroll/<string:course>",view_func=EnrollView.as_view("enroll",EnrollModel, CourseModel, UserToken, "e_learning/enroll_to_course.html"))

