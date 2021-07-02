from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import werkzeug
import model_handling as mh

app = Flask(__name__)
api = Api(app)

predict_post_arg = reqparse.RequestParser()
predict_post_arg.add_argument('file',
type=werkzeug.datastructures.FileStorage,
location='files',help='kindly attach image')

class FYP_Model(Resource):
    def post(self):
        arg = predict_post_arg.parse_args()
        image_file = arg['file']
        img_path = "app/uploads/images/image.jpg"
        image_file.save(img_path)
        result = mh.predict(img_path)
        return result

api.add_resource(FYP_Model,'/predict/')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")