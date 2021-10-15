import click
import yaml
import time
import logging.config

from collections import deque

from db.mgdb import MemGraphDB
from utils.protocol_prefix import add_https
from scripts.url_parser.bfs import bfsearch
from scripts.storage.node_storage import ADJListToGraphNodesConverter


with open('config/logger_config.yml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)


@click.group()
def cli(): ...


@click.command()
@click.option('--start_url')
@click.option('--depth', type=int, default=2)
def network(start_url, depth):

    start_time = time.time()

    mgdb = MemGraphDB()

    logging.info(f'Starting to parse: "{add_https(start_url)}" at {depth} depth level.')
    ADJ_LIST = {}
    # link parsing
    bfsearch(
        adj_list=ADJ_LIST,
        root_node=add_https(start_url),
        q=deque(),
        max_level=depth)

    # traversing ADJ_LIST and converting it to list of node tuples
    data_to_nodes = ADJListToGraphNodesConverter(ADJ_LIST)
    nodes = data_to_nodes.get_nodes

    parsing_stop_time = time.time()
    logging.info('Starting to save nodes into MemGraph Database.')

    # maybe to most memory efficient way would be to, as we parse, save nodes(in small chunks with iteration)
    # directly to database (and handle error's in parallel) so we do not hold all nodes in memory.
    # For now I chose this way: finish parsing first and then save what is parsed.

    # saving parsed nodes into db for further analysis.
    mgdb.save_values_to_db(nodes)

    final_stop_time = time.time()
    logging.info(f'Parsing time: {parsing_stop_time - start_time}')
    logging.info(f'General execution time: {final_stop_time - start_time}')


@click.command()
@click.option('--start_url')
@click.option('--end_url')
def path(start_url, end_url):
    print(start_url, end_url)

    mgdb = MemGraphDB()
    mgdb.get_path(start_url, end_url)


cli.add_command(network)
cli.add_command(path)

if __name__ == '__main__':
    cli()
