import io
import os
from flask import Flask, request, send_file
from PIL import Image
from base64 import b64decode

import u2net

# Initialize the Flask application
app = Flask(__name__)

# Simple probe.
@app.route('/', methods=['GET'])
def hello():
    return 'Hello U^2-Net!'


# Route http posts to this method
@app.route('/postImage/', methods=['POST'])
def run():
    # Convert string data to PIL Image
    img = Image.open(io.BytesIO(b64decode(request.form['image'])))

    # Process Image
    res = u2net.run(img)

    # Save to buffer
    buff = io.BytesIO()
    res.save(buff, 'PNG')
    buff.seek(0)

    # Return data
    return send_file(buff, mimetype='image/png')


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
