import yaml
import importlib
import sys
from sanic import Sanic, response
app = Sanic(name="App")
class Main:
    def index(self, request):
        return response.text('Home')
    def test(self, request):
        return response.text('Test') 
    
if __name__ == "__main__":
    with open('routes.yml', 'r') as stream:
        data = yaml.load(stream, yaml.BaseLoader)
    for item in data:
        call_module = getattr(sys.modules[__name__], item['controller'])
        controller = call_module()
        handler = getattr(controller, item['handler']) 
        app.add_route(handler, item['path'], )
    app.run(host='0.0.0.0', port=80, debug=True)
