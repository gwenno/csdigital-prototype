import os

from flask_assets import Bundle, Environment
from webassets.filter import get_filter

sass = get_filter('sass', as_output=True)

sass.load_paths = [os.path.join(os.path.dirname(__file__), 'static/sass'),
                    os.path.join(os.path.dirname(__file__), 'static/govuk_frontend_toolkit/stylesheets'),
                    os.path.join(os.path.dirname(__file__), 'static/govuk_elements/public/sass/elements')]


css_govuk_elements = Bundle(
    'sass/govuk_elements.scss',
    filters=sass,
    output='stylesheets/govuk_elements.css',
    depends=['/static/govuk_elements/public/sass/**/*.scss',
                '/static/govuk_frontend_toolkit/stylesheets/**/*.scss']
)

css_main = Bundle(
    'sass/main.scss',
    filters=sass,
    output='stylesheets/main.css',
    depends=['/static/sass/main/**/*.scss','/static/govuk_frontend_toolkit/stylesheets/**/*.scss']
)

env = Environment()
env.register('css_govuk_elements', css_govuk_elements)
env.register('css_main', css_main)
