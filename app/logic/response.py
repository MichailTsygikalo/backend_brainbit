from flask_restful import Resource
from route import task_post_args


class ResponceTest(Resource):
    def post(self):
        print("hello")
        args = task_post_args.parse_args()
        print(args['text_question'])
        return 200