from fabric.api import task
from fabric.colors import green
from fabric.operations import local


@task
def hello():
    print ("I'm alive!")


def bye():
    print ("Fudge")


@task
def what():
    print(green("WHAT"))

@task
def create_file(filename):
    local("echo $null >> {}.txt".format(filename))