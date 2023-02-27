"""
Copyright (C) 2023 Henrik Baran

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import sys
import time
from confluent_kafka import Consumer, KafkaError, KafkaException


conf = {'bootstrap.servers': "host1:9092,host2:9092",
        'group.id': "foo",
        'auto.offset.reset': 'smallest'}

# my_consumer = Consumer(conf)
my_consumer = 'Ätest'
my_topics = ['BI_TAKE_OUT_LOG']


def basic_consume_loop(consumer, topics):
    try:
        # consumer.subscribe(topics)

        while True:
            """msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            elif msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)"""
            print('test')
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    finally:
        pass
        # Close down consumer to commit final offsets.
        # consumer.close()


def main():
    basic_consume_loop(consumer=my_consumer, topics=my_topics)


if __name__ == "__main__":
    main()
