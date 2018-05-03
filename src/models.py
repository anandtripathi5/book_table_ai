from google.cloud import datastore

from logger import function_logger, log


def create_client():
    return datastore.Client.from_service_account_json('scripts/client.json')


@function_logger(log)
def add_user(client, **kwargs):
    key = client.key('users')

    task = datastore.Entity(
        key, exclude_from_indexes=["created_on"])

    task.update(**kwargs)
    client.put(task)
    print task.key, task
    return task.key


@function_logger(log)
def get_user(client, user_id=None):
    query = client.query(kind='users')
    query.add_filter('user_id', '=', user_id)
    user = list(query.fetch())
    return user[0] if user else None
