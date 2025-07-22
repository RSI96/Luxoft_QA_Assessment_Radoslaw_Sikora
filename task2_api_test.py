import requests

ENDPOINT = 'http://127.0.0.1:5000/'

def get_users():
    return requests.get(ENDPOINT + '/users')

def get_user_by_id(id):
    return requests.get(ENDPOINT + f'/users/{id}')

def create_user(payload):
    return requests.post(ENDPOINT + '/users', json = payload)

def create_invalid_users():
    no_name_user_data = {
        "email":"invalid@example.com"
    }
    no_email_user_data = {
        "name":"Invalid"
    }
    empty_user_data = {}
    return [no_name_user_data, no_email_user_data, no_email_user_data]

#First three tests are fulfilling requirements for this task. The rest is for better coverage.
#It would be much better to use pytest for test execution but it was not listed in available tools for this task so I tried to do the task without it.
def TC01_test_get_user():
    '''Tests Get User with id = 1'''
    user_data = {"email":"alice@example.com","id":1,"name":"Alice"}
    get_user_response = get_user_by_id(user_data['id']).json()
    try:
        assert get_user_response == user_data, 'Inconsistency in first user in the list.'
    except AssertionError as error:
        print(f'FAILED - TC01 - Test Get User with id = 1. Error: {error}. Expected: {user_data}. Observed: {get_user_response}.')
    else:
        print(f'PASSED - TC01 - Test Get User. User retrieval successful.')

def TC02_test_create_user():
    '''Test Create User.'''
    new_user_data = {
        "name":"Radek",
        "email":"radek@example.com"
    }
    create_user_response = create_user(new_user_data)
    new_user_id = create_user_response.json()['id']
    new_user_expected_response = new_user_data | {'id': new_user_id}
    new_user_get_response = get_user_by_id(new_user_id)
    new_user_get_response_data = new_user_get_response.json()
    try:
        assert new_user_get_response_data['id'] == new_user_expected_response['id'] and new_user_get_response_data['name'] == new_user_expected_response['name'] and new_user_get_response_data['email'] == new_user_expected_response['email'], 'Inconsistency in created user.'
    except AssertionError as error:
        print(f'FAILED - TC02 - Test Create User with id = {new_user_id}. Error: {error}. Expected: {new_user_expected_response}. Observed: {new_user_get_response_data}.')
    else:
        print(f'PASSED - TC02 - Test Create User. User creation successful.')

def TC03_test_error_handling():
    '''Test Create User. Status Code is 400.'''
    invalid_users = create_invalid_users()
    for invalid_user in invalid_users:
        invalid_user_response = create_user(invalid_user)
        try:
            assert invalid_user_response.status_code == 400, 'Status code is not 400.'
        except AssertionError as error:
            print(f'FAILED - TC03 - Test Create User Status Code is 400. Error: {error}. Expected: 400. Observed: {invalid_user_response.status_code}')
        else:
            print(f'PASSED - TC03 - Test Create User. Status Code is 400.')

    get_non_existing_user_response = get_user_by_id(9999999)
    try:
        assert get_non_existing_user_response.status_code == 404, 'Status code is not 404.'
    except AssertionError as error:
        print(f'FAILED - TC03 - Test Get Non Existing User. Error: {error}. Expected: 404. Observed: {get_non_existing_user_response.status_code}')
    else:
        print(f'PASSED - TC03 - Test Get Non Existing User. Status Code is 404.')

    get_user_server_error_response = get_user_by_id(999)
    try:
        assert get_user_server_error_response.status_code == 500, 'Status code is not 500.'
    except AssertionError as error:
        print(f'FAILED - TC03 - Test Get User. Server Error. Error: {error}. Expected: 500. Observed: {get_user_server_error_response.status_code}')
    else:
        print(f'PASSED - TC03 - Test Get User. Server Error. Status Code is 500.')

#Additional tests for better coverage
def TC04_test_get_users():
    '''Test Get User with all available ids.'''
    get_users_response = get_users()
    user_list_length = len(get_users_response.json())
    for i in range(0, user_list_length):
        user_id = get_users_response.json()[i]['id']
        get_user_response = get_user_by_id(user_id)
        try:
            assert get_user_response.json() == get_users_response.json()[i], 'Inconsistent data between /users and /users<id>.'
        except AssertionError as error:
            print(f'FAILED - TC04 - Test Get User with id = {user_id}. Expected Result: {get_users_response.json()[i]}. Actual Result: {get_user_response.json()}')
        else:
            print(f'PASSED - TC04 - Test Get User with id = {user_id}.')

def TC05_test_get_user_status_code():
    '''Test Get User Status Code. Status code is 200.'''
    user_data = {"email":"alice@example.com","id":1,"name":"Alice"}
    get_user_response = get_user_by_id(user_data['id'])
    try:
        assert get_user_response.status_code == 200, 'Status code is not 200.'
    except AssertionError as error:
        print(f'FAILED - TC05 - Test Get User Status Code. Error: {error}.')
    else:
        print(f'PASSED - TC05 - Test Get User Status Code. Status code is 200.')

def TC06_test_get_users_status_code():
    '''Test Get Users Status Code. Status code is 200.'''
    user_data = {"email":"alice@example.com","id":1,"name":"Alice"}
    get_users_response = get_users()
    try:
        assert get_users_response.status_code == 200, 'Status code is not 200.'
    except AssertionError as error:
        print(f'FAILED - TC06 - Test Get Users Status Code. Error: {error}.')
    else:
        print(f'PASSED - TC06 - Test Get Users Status Code. Status code is 200.')

def TC07_test_create_user_status_code():
    '''Test Create New User Status Code. Status code is 201.'''
    new_user_data = {
        "name":"Radek",
        "email":"radek@example.com"
    }
    create_user_response = create_user(new_user_data)
    try:
        assert create_user_response.status_code == 201, 'Status code is not 201.'
    except AssertionError as error:
        print(f'FAILED - TC07 - Test Create New User Status Code. Error: {error}.')
    else:
        print(f'PASSED - TC07 - Test Create New User Status Code. Status code is 201.')

TC01_test_get_user()
TC02_test_create_user()
TC03_test_error_handling()
TC04_test_get_users()
TC05_test_get_user_status_code()
TC06_test_get_users_status_code()
TC07_test_create_user_status_code()