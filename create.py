import sys
import time

import boto3

time.sleep(10)

if len(sys.argv) < 2:
    print(f'Expected list of queue names to create')
    exit(1)

sqs = boto3.resource('sqs', endpoint_url='http://localstack:4576/')
for i, name in enumerate(sys.argv[1:]):
    queue = sqs.create_queue(QueueName=name)
    print(queue.url)
    if i == 0:
        queue.send_message(MessageBody='1')
