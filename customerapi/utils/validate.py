"""Validator Module"""
import re


def validate(data, regex):
    return True if re.match(regex, data) else False


def validate_password(password: str):
    reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return validate(password, reg)


def validate_username(username: str):
    regex = r'\b[A-Za-z0-9._%+-]+'
    return validate(username, regex)


def validate_user(**args):
    if not args.get('username') or not args.get('password'):
        return {
            'username': 'username is required',
            'password': 'Password is required'
        }
    if not isinstance(args.get('username'), str) or not isinstance(args.get('password'), str):
        return {
            'username': 'username must be a string - recieved %s' % type(args.get('username')),
            'password': 'Password must be a string - recieved %s' % type(args.get('password')),
        }
    if not validate_username(args.get('username')):
        return {
            'username': 'username is invalid'
        }
    if not validate_password(args.get('password')):
        return {
            'password': 'Password is invalid, Should be at least 8 characters with \
                upper and lower case letters, numbers and special characters'
        }
    return True


def validate_username_and_password(username, password):
    if not (username and password):
        return {
            'username': 'username is required',
            'password': 'Password is required'
        }
    if not validate_username(username):
        return {
            'username': 'username is invalid'
        }
    if not validate_password(password):
        return {
            'password': 'Password is invalid, Should be at least 8 characters with \
                upper and lower case letters, numbers and special characters'
        }
    return True
