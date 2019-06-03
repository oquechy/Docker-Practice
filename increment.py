import sys
import time

import boto3

time.sleep(20)

if len(sys.argv) != 3:
    print(f'Expected 2 parameters with queue names, got {len(sys.argv) - 1}')
    exit(1)

sqs = boto3.resource('sqs', endpoint_url='http://localstack:4576/')
read_queue = sqs.get_queue_by_name(QueueName=sys.argv[1])
write_queue = sqs.get_queue_by_name(QueueName=sys.argv[2])

while True:
    for message in read_queue.receive_messages():
        number = message.body
        print(number, flush=True)
        write_queue.send_message(MessageBody=f'{int(number) + 1}')
        message.delete()
        time.sleep(2)
