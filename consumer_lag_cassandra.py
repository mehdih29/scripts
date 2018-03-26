import subprocess
import argparse
import csv 

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
    """

    output = []
    readCSV = csv.reader(input_from_checker, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)

    return output


def to_line_protocol(parsed_output, group):
    """
    Converts the parsed output to InfluxDB line protocol metrics
    """
    return ["kafka.consumer_offset,group="+group+",topic={topic},partition={partition} current_offset={current_offset},log_end_offset={log_end_offset},lag={lag}"
            .format(**line) for line in parsed_output]


def get_cassandra(args):
    """
    Gets consumer offsets from cassandra
    """

# cqlsh -e "use system; COPY local TO STDOUT with HEADER = true;"


    params = [
        'use {};'.format(args.cassandra_keyspace),
        'COPY {} TO STDOUT with HEADER = true;'.format(args.cassandra_table)
    ]

    cmd = subprocess.Popen('cqlsh -e "'+ " ".join(params) + '"', shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE)

    return [line for line in cmd.stdout]

if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--cassandra_keyspace', default='current_position', help='cassandra keyspace', required=True)
    parser.add_argument('--cassandra_table', default='core2', help='cassandra table', required=True)
    args = parser.parse_args()

    output = get_cassandra(args)
    print output
    parsed_output = parse_output(output)
    print parsed_output

    #for line in to_line_protocol(parsed_output, args.group):
    #    print line
