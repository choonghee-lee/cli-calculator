import click
from math import pi

@click.group()
def arithmetics():
    pass

# 팩토리얼 구하기
@arithmetics.command()
@click.argument('num', type=int)
def fact(num):
    """Calculate factorial value."""
    if num < 0:
        return 0
    if num == 0:
        return 1

    f = 1
    for i in range(1, num + 1):
        f = f * i
    click.echo(f)


# 거듭제곱
@arithmetics.command()
@click.argument('base', type=float)
@click.argument('exponent', type=float)
def pow(base, exponent):
    """Get the power of a number"""
    click.echo(base**exponent)


# 도를 라디안으로 변환
@arithmetics.command()
@click.argument('degree', type=float)
def dtr(degree):
    """Convert degree to radian"""
    click.echo(degree*(pi/180))


# 라디안을 도로 변환
@arithmetics.command()
@click.argument('radian', type=float)
def rtd(radian):
    """Convert radian to degree"""
    click.echo(radian*(180/pi))