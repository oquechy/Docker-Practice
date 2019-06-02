import sys

import boto3

if len(sys.argv) < 2:
    print(f'Expected list of queue names to create')
    exit(1)

sqs = boto3.resource('sqs', endpoint_url=f'http://localhost:4576/')
for i, name in enumerate(sys.argv[1:]):
    queue = sqs.create_queue(QueueName=name)
    print(queue.url)
    if i == 0:
        queue.send_message(MessageBody='1')
