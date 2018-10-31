import unittest
import json

from graphene.test import Client
from app.main.services.user_service import UserService
from app.main.schema import schema

from app.test.base import BaseTestCase
from snapshottest import TestCase

class TestGraphene(BaseTestCase, TestCase):
    def test_app_graphql(self):
        client = Client(schema)
        UserService.save_new_user({'username': "teste01", 'password': "123123"})
        query = '''query {
            allUsers {
                edges {
                    node {
                        id,
                        username
                    }
                }
            }
        }
        '''

        executed = client.execute(query)
        self.assertMatchSnapshot(executed)

if __name__ == '__main__':
    unittest.main()
