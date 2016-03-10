# -*- coding: utf-8 -*-
import os


class Config(object):
    DEBUG = False
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = False
    APP_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_ROOT, os.pardir))
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = SECRET_KEY
    SECURITY_PASSWORD_HASH = os.environ.get('SECURITY_PASSWORD_HASH', 'bcrypt')
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_URI')
    }
    MAIL_SERVER = os.environ.get('MAILGUN_SMTP_SERVER')
    MAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')
    MAIL_USERNAME = os.environ.get('MAILGUN_SMTP_LOGIN')
    MAIL_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
    HOST = os.environ.get('HOST', 'localhost')
    PORT = os.environ.get('PORT', '8000')
    EMAIL_DOMAIN = os.environ.get('EMAIL_DOMAIN', 'mylog.civilservice.digital')

    OIDC = {
        # 'google': {
            # 'domain': 'accounts.google.com',
            # 'client': {
                # 'client_id': os.environ.get('GOOG_CLIENT_ID'),
                # 'client_secret': os.environ.get('GOOG_CLIENT_SECRET'),
                # 'redirect_uri': os.environ.get(
                    # 'GOOG_OIDC_CALLBACK_URL',
                    # 'http://localhost:8000/login/callback')
            # }
        # },
        'auth0': {
            'domain': 'xgs.eu.auth0.com',
            'client': {
                'client_id': os.environ.get('AUTH0_CLIENT_ID'),
                'client_secret': os.environ.get('AUTH0_CLIENT_SECRET'),
                'redirect_uri': os.environ.get(
                    'AUTH0_CALLBACK_URL',
                    "http://{}:{}/login/callback".format(HOST, PORT))
            }
        }
    }


class DevelopmentConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True
    WTF_CSRF_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'local-dev-not-secret')
    DEBUG_TB_PANELS = [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask.ext.mongoengine.panels.MongoDebugPanel']
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PROFILER_ENABLED = True
    MAIL_DEBUG = True
    MAIL_SUPPRESS_SEND = True


class DockerConfig(DevelopmentConfig):
    # is this guaranteed to be up yet cause it's linked?
    host = os.environ.get('DB_PORT_27017_TCP_ADDR')
    port = int(os.environ.get('DB_PORT_27017_TCP_PORT', 27017))
    MONGODB_SETTINGS = {
        'host': host,
        'db': 'xgs_performance_reviews',
        'port': port
    }


class TestConfig(DevelopmentConfig):
    TESTING = True
