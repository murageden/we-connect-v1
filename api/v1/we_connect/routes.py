from flask import Flask, jsonify, request
# local imports
from we_connect.user import User

app = Flask(__name__)


# holds user in session
logged_in = []


# creates a user account
@app.route('/weconnect/api/v1/auth/register', methods=['POST'])
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    user = User()
    message = user.create_user(name, email, password)
    return jsonify(message)


# logs in a user
@app.route('/weconnect/api/v1/auth/login', methods=['POST'])
def login_user():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User()
    all_users = user.get_all_users()
    for user in all_users:
        if user['email'] == email and user['password'] == password:
            message = {
                        'id': user['id'],
                        'name': user['name'],
                        'email': user['email'],
                        'msg': 'Log in successfull'}
            logged_in.append(user)
            return jsonify(message)
        else:
            message = {
                'msg': 'Wrong email-password combination'}
            return jsonify(message)


# logs out a user
@app.route('/weconnect/api/v1/auth/logout', methods=['POST'])
def logout():
    if len(logged_in) == 0:
        message = {
                'msg': 'No user is logged in currently'}
        return jsonify(message)
    else:
        message = {
                    'id': logged_in[-1]['id'],
                    'name': logged_in[-1]['name'],
                    'email': logged_in[-1]['email'],
                    'msg': 'Log out successfull'}
        logged_in.remove(logged_in[-1])
        return jsonify(message)


# password reset
@app.route('/weconnect/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    pass


# register a business
@app.route('/weconnect/api/v1/businesses', methods=['POST'])
def register_business():
    name = request.form.get('name')
    description = request.form.get('description')
    category = request.form.get('category')
    location = request.form.get('location')
    ownerId = request.form.get('ownerId')
    business = Business()
    message = business.create_business(name, category, description, location, ownerId)
    return jsonify(message)


# updates a business
@app.route('/weconnect/api/v1/businesses/<businessId>', methods=['PUT'])
def update_business():
    name = request.form.get('name')
    description = request.form.get('description')
    category = request.form.get('category')
    location = request.form.get('location')
    ownerId = request.form.get('ownerId')
    business = Business()
    message = business.update_business(businessId, name, category, description, location, ownerId)
    return jsonify(message)


# removes a business
@app.route('/weconnect/api/v1/businesses/<businessId>', methods=['DELETE'])
def remove_business():
    pass


# retrieves all businesses
@app.route('/weconnect/api/v1/businesses', methods=['GET'])
def retrieve_all_businesses():
    pass


# retrieves a single business
@app.route('/weconnect/api/v1/businesses/<businessId>', methods=['GET'])
def retrieve_business(businessId):
    response = Business().view_business(businessId)
    return jsonify(response)


# adds a review to a business
@app.route('/weconnect/api/v1/businesses/<businessId>/reviews',
methods=['POST'])
def add_review_for(businessId):
    pass


# retrieves all reviews for a single business
@app.route('/weconnect/api/v1/businesses/<businessId>/reviews',
methods=['GET'])
def get_reviews_for(businessId):
    pass


if(__name__) == '__main__':
    app.run(debug=True)
