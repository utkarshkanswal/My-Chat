from django.utils.deprecation import MiddlewareMixin
import json

class MyCustomMiddleware(MiddlewareMixin):

    def process_request(self,request):
        print("Request is processed...")

    def process_response(self,request,response):
        print("processed response... ")
        if response["content-type"]=="application/json":
            data=json.loads(response.content)
            for each in data:
                each["my_custom_field"]="this is my field"
            response.content=json.dumps(data)

        return response
