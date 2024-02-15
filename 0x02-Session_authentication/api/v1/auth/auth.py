#!/usr/bin/env python3
'''
a class to manage the API authentication.
'''
import re
from typing import List, TypeVar
from flask import request


class Auth:
    '''
    class for authentication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        checks if auth is required
        '''
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        '''
        returns auth header request
        '''
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        fetches current user
        '''
        return None

    def session_cookie(self, request=None) -> str:
        """Gets the value of the cookie named SESSION_NAME.
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME', '_my_session_id')
            return request.cookies.get(cookie_name)
