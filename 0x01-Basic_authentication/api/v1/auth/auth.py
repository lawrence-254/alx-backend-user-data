#!/usr/bin/python3
'''
a class to manage the API authentication.
'''
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
        return False
    

    def authorization_header(self, request=None) -> str:
        '''
        returns auth header request
        '''
        return None
    
    
    def current_user(self, request=None) -> TypeVar('User'):
        '''
        fetches current user
        '''
        return None