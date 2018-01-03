from fabric.api import run, env, execute
env.user = os.environ.get('FABUSER')
env.password = os.environ.get('FABPASSWD')

def setup():
    run("yum install nginx")
    run("yum install python-pip")
    run("pip install virtualenv")

def build():
    with cd("controle-despesas-republica"):
        run("virtualenv env")
        with prefix('workon env'):
            run("pip install -r requirements.txt")
            run("python sis/manager.py test")

def dist():
    with cd("controle-despesas-republica")
    run('tar -cvf controle-despesas-republica.tar env sis')            
