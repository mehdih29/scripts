import subprocess
import argparse

# VERSION 0.1
# from https://github.com/paksu/kafka-consumer-lag-telegraf-reporter

OUTPUT_KEYS = ['topic', 'partition', 'current_offset', 'log_end_offset', 'lag']


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line



def parse_output(input_from_checker):
    """
    Parses the output from kafka-consumer-groups.sh, converts metrics in to integers and returns
    a list of dicts from each row as a response

TOPIC                          PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG        CONSUMER-ID                                       HOST                           CLIENT-ID
test_burrowx_topic             0          73              74              1          kafka-python-1.3.5-ecae6668-8dfc-412c-9a83-d93c268464b3/127.0.0.1                     kafka-python-1.3.5
    """

    output = []
    for line in nonblank_lines(input_from_checker):
        # Skip header
        if line and ('LOG-END-OFFSET'  or 'Note: This will not show information about old Zookeeper-based consumers.' or '\n') not in line:
            columns = line.split()
            # Only pick the columns we are interested in
            topic = columns[0]
            metric_columns = [int(c) for c in columns[1:5]]

            key_and_value_pairs = zip(OUTPUT_KEYS, [topic] + metric_columns)
            output.append(dict(key_and_value_pairs))

    return output


def to_line_protocol(parsed_output, group):
    """
    Converts the parsed output to InfluxDB line protocol metrics
    """
    return ["kafka.consumer_offset,group="+group+",topic={topic},partition={partition} current_offset={current_offset},log_end_offset={log_end_offset},lag={lag}"
            .format(**line) for line in parsed_output]


def get_kafka(args):
    """
    Gets consumer offsets from kafka via kafka-consumer-groups.sh

    Should work on Kafka 0.8.0.2 and 0.9.0.1
    """
    # append trailing slash
    if args.kafka_dir[-1] != "/":
        args.kafka_dir = args.kafka_dir + "/"

    params = [
        '{}bin/kafka-consumer-groups.sh'.format(args.kafka_dir),
        '--group {}'.format(args.group),
        '--describe'
    ]
    if args.zookeeper:
        params = params + ['--zookeeper', args.zookeeper]
    else:
        params = params + ['--bootstrap-server', args.bootstrap_server]

    cmd = subprocess.Popen(" ".join(params), shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE)

    return [line for line in cmd.stdout]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--kafka-dir', default='/opt/kafka/', help='Kafka base directory', required=True)
    parser.add_argument('--group', help='Kafka group to check', required=True)
    parser.add_argument('--bootstrap-server', help='Which kafka to query. Used for new consumer')
    parser.add_argument('--zookeeper', help='Which zookeeper to query. Used for old consumer')
    args = parser.parse_args()
    assert args.zookeeper or args.bootstrap_server, "requires either --zookeeper or --bootstarp-server"

    output = get_kafka(args)
    parsed_output = parse_output(output)
    for line in to_line_protocol(parsed_output, args.group):
        print line
