import click
from click_help_colors import HelpColorsGroup
from arithmetics.commands import arithmetics

@click.version_option('0.1.0', prog_name="Calculator From CLI")
@click.group(
    cls=HelpColorsGroup,
    help_headers_color="yellow",
    help_options_color="magenta"
)
def main():
    """Calculator From CLI"""
    pass

main.add_command(arithmetics)

if __name__ == "__main__":
    main()