from kubernetes import client, config
from kubernetes.stream import stream
from kubernetes.client.rest import ApiException


def connect_to_cluster():
    """ Function to creates a stream connection to
    Kubernetes Cluster

    Returns:
        connection stream -- a stream connection object
    """
    try:
        config.load_kube_config()

    except TypeError:
        config.load_incluster_config()

    con_v1 = client.CoreV1Api()

    return con_v1


if __name__ == "__main__":
    try:
        conn = connect_to_cluster()

    except ApiException as error:
        raise ApiException("ERROR: %s" % error)
