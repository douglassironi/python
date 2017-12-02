from fabric.api import run, env, execute

env.user = "root"
env.password = "toor"
env.hosts = ["10.50.11.38"]

def host_type():
    run('uname -s')

def resolucao_1024():
    run("xrandr -d :0 --output default --mode 1024x768 --primary")

def resolucao_800():
    run("xrandr -d :0 --output default --mode 800x600 --primary")

execute(resolucao_1024)
execute(resolucao_800)
