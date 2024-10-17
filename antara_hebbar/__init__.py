"""Package initializer."""
import flask

# # app is a single object used by all the code modules in this package
# # app = flask.Flask(__name__)  # pylint: disable=invalid-name
# app = flask.Flask(__name__, static_folder='../frontend/build', static_url_path='')


# # Read settings from config module (insta485/config.py)
# app.config.from_object('antara_hebbar.config')

# # Overlay settings read from a Python file whose path is set in the environment
# # variable INSTA485_SETTINGS. Setting this environment variable is optional.
# # Docs: http://flask.pocoo.org/docs/latest/config/
# #
# # EXAMPLE:
# # $ export INSTA485_SETTINGS=secret_key_config.py
# app.config.from_envvar('ANTARA_HEBBAR_SETTINGS', silent=True)

# # Tell our app about views and model.  This is dangerously close to a
# # circular import, which is naughty, but Flask was designed that way.
# # (Reference http://flask.pocoo.org/docs/patterns/packages/)  We're
# # going to tell pylint and pycodestyle to ignore this coding style violation.

from flask import Flask, send_from_directory

def create_app():
    app = flask.Flask(__name__, static_folder='../frontend/build', static_url_path='')
    app.config.from_object('antara_hebbar.config')

    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    # @app.route('/<path:path>')
    # def static_proxy(path):
    #     return Flask.send_from_directory(app.static_folder, path)

    return app