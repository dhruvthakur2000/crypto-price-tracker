import click
from src.api import get_crypto_price
from src. errors import APIError
import json

@click.command()

@click.option(
    '--crypto', '-c',
    required=True,
    prompt='Enter the Crypto id', 
    help='The cryptocurrency to track (e.g., Bitcoin, Ethereum).',
    type=str
    )

@click.option(
    '--output', '-o',
    type=click.Choice(['console', 'file'], case_sensitive=False),
    default='console',
    help='Output format: console or file.'
    )

@click.option(
    '--file', '-f',
    type=click.Path(),
    help='File path to save output (required if output is "file").'
    )
   
def cli(crypto,output, file):
    """
    CLI for tracking cryptocurrency prices.
    """
    try:
        price = get_crypto_price(crypto)
        if output == 'console':
            click.echo()
            click.secho(f"💰 {crypto.upper()} Prices", fg='green', bold=True)
            click.secho(f"🇮🇳 INR: ₹{price['inr']:,}", fg='yellow')
            click.secho(f"🇺🇸 USD: ${price['usd']:,}", fg='blue')
            click.echo
        elif output == 'file':
            if not file:
                raise click.UsageError("File path is required when output is 'file'.")
                return
            if not file.endswith('.json'):
                raise click.UsageError("File must have a .json extension.")
        
        with open(file, 'w') as f:
            json.dump({crypto: price}, f)
            click.echo(f"Price saved to {file}")
    except APIError as e:
        click.echo(f"Error fetching price: {e}")
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")