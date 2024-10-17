"""Development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'W7\xf7\x98\x9e\xe4th\xdfw7\xc0\x86iy\xb9\xe6t\xab%!w\xc4\xe2'

# File Upload to var/uploads/
ANTARA_HEBBAR_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = ANTARA_HEBBAR_ROOT/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024