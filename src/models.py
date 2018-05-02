from google.cloud import datastore


def create_client(project_id):
    return datastore.Client.from_service_account_json('scripts/client.json')


def add_user(client, **kwargs):
    key = client.key('users')

    task = datastore.Entity(
        key, exclude_from_indexes=["created_on"])

    task.update(**kwargs)
    client.put(task)
    print task.key, task
    return task.key


def get_user(client, user_id=None):
    query = client.query(kind='users')
    query.add_filter('user_id', '=', user_id)
    user = list(query.fetch())
    return user[0]