""""
hdfs client
"""

from hdfs import InsecureClient

def get_client(user="worker"):
    """
    returns HDFS web client object for HDFS job
    
    Parameters
    ---------
    user : str default "worker"
    """
    return InsecureClient("http://hdfs:9870", user=user)