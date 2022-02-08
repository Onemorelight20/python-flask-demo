from crypt import methods
from main import app

@app.route('/')
def index():
    print('inside index')
    return "Hooray";


@app.route('/fish', methods=["GET"])
def fish_c():
    return "My fish is tasty"

@app.route('/fish', methods=["POST"])
def fish_insertion():
    return "You added a fish into system"


