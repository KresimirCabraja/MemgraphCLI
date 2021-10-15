import sys
import yaml
import logging
import mgclient


class MemGraphDB:

    def __init__(self, db_config_path: str = ''):
        # If config file path is not found, fallback to localhost.
        # In real case scenario, remote db will probably have some
        # password or public/private key for ssl/tls. Since this is not
        # real case scenario I did not provide attributes for such case.
        self.config = {}
        self.connection = None
        self.cursor = None

        try:
            with open(db_config_path) as stream:
                self.config = yaml.safe_load(stream)
                logging.info('Connection to DB from config file OK.')

                self.connection = mgclient.connect(
                    host=self.config['host'],
                    port=self.config['port']
                )
                self.cursor = self.connection.cursor()

        except (FileNotFoundError, IsADirectoryError):
            logging.warning('Config file for MemGraph database not found or path not provided.')
            logging.info('Setting db connection to localhost values.')

            self.config['host'] = '127.0.0.1'
            self.config['port'] = 7687

            try:
                # code smell of repeating chunks of code...I know...
                self.connection = mgclient.connect(
                    host=self.config['host'],
                    port=self.config['port']
                )
                self.cursor = self.connection.cursor()

                logging.info('Connected to localhost MemGraph DB.')
            except Exception as e:
                logging.error(f'Connection refused: {e}')
                sys.exit("Exiting. Couldn't connect to DB")

    def save_values_to_db(self, nodes):
        for _ in nodes:
            for i in _:
                self.cursor.execute("""
                            CREATE (n:Node {url: '%s'})-[u:LINKED_TO]->  
                            (m:Node {url: '%s'})
                             RETURN n, u, m
                            """ % (i[0], i[-1]))
                self.connection.commit()

    def get_path(self, node_a: str, node_b: str):
        path = self.cursor.execute(
            """
                MATCH (n)-->(m)
                RETURN n.url, m.url
            """
        )
        return path


if __name__ == '__main__':

    list_of_nodes = [
        [('https://index.hr', 'https://www.index.hr/oglasi/'),
         ('https://index.hr', 'https://recepti.index.hr'),
         ('https://index.hr', 'https://www.index.hr/lajk/'),
         ('https://index.hr', 'https://www.index.hr/indexforum/'),
         ]
    ]

    db = MemGraphDB()
    db.save_values_to_db(list_of_nodes)
