import click
from arithmetics.commands import arithmetics

@click.version_option('0.0.1', prog_name="Calculator From CLI")
@click.group()
def main():
    """Calculator From CLI"""
    pass

main.add_command(arithmetics)

if __name__ == "__main__":
    main()