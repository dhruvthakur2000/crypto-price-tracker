import unittest
from click.testing import CliRunner
from src.cli import cli

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_valid_crypto_console(self):
        result = self.runner.invoke(cli, ['--crypto', 'bitcoin', '--output', 'console'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Prices", result.output)

    def test_invalid_crypto(self):
        result = self.runner.invoke(cli, ['--crypto', 'invalidcoin', '--output', 'console'])
        self.assertIn("error", result.output.lower())

    def test_missing_file_path(self):
        result = self.runner.invoke(cli, ['--crypto', 'bitcoin', '--output', 'file'])
        self.assertIn("file path is required ", result.output.lower())

if __name__ == "__main__":
    unittest.main()
