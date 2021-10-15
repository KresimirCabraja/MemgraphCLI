import unittest
import logging
from click.testing import CliRunner
from main import cli, network


logging.disable()


class TestCli(unittest.TestCase):

    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_network_command(self):
        cli_runner = self.runner
        with cli_runner.isolated_filesystem():
            result = cli_runner.invoke(cli=cli, args=['network', '--start_url', 'google.com', '--depth', 0])
            self.assertEqual(result.exit_code, 0)
            self.assertNotEqual(result.exit_code, 1)

    def test_path_command(self):
        cli_runner = self.runner
        result = cli_runner.invoke(cli=cli, args=[
                                            'path',
                                            '--start_url',
                                            'google.com',
                                            '--end_url',
                                            'google.com/account'
                                            ])
        self.assertEqual(result.exit_code, 0)


if __name__ == '__main__':
    unittest.main()
