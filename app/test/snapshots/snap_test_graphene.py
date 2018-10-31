# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGraphene::test_app_graphql 1'] = {
    'data': {
        'allUsers': {
            'edges': [
                {
                    'node': {
                        'id': 'VXNlcnM6MQ==',
                        'username': 'teste01'
                    }
                }
            ]
        }
    }
}
