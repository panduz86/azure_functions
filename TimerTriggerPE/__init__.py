import datetime
import logging

import azure.functions as func
from azure.storage.blob import BlobServiceClient
import os

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    connect_str = os.environ['AzureWebJobsStorage']
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    for container in blob_service_client.list_containers():
        logging.info('Container name %s', container.name)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
