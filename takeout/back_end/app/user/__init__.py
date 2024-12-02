from flask import Blueprint

from .login.login import user_login_bp
from .login.register import user_register_bp
from .login.forget import user_forget_bp

from .userinfo.profilephoto import user_profile_photo_bp
from .userinfo.info import user_info_bp

user_bp = Blueprint('user', __name__)

# 注册子蓝图
user_bp.register_blueprint(user_login_bp, url_prefix='/login', name='user_login')
user_bp.register_blueprint(user_register_bp, url_prefix='/register', name='user_register')
user_bp.register_blueprint(user_forget_bp, url_prefix='/forget', name='user_forget')

user_bp.register_blueprint(user_profile_photo_bp, url_prefix='/profilePhoto', name='user_profile_photo')
user_bp.register_blueprint(user_info_bp, url_prefix='/info', name='user_info')
