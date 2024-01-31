from app import app
import os,click
@app.cli.group()
def translate():
    """Translation commands"""
    pass

@translate.command()
def update():
    """Update database"""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('pybabel extract command failed')
    if os.system('pybabel update -i messages.pot -d app/translations/'):
        raise RuntimeError('update command faild')
    os.remove('messages.pot')

@translate.command()
def compile():
    """Compile translations"""
    if os.system('pybabel compile -d app/translations/'):
        raise RuntimeError('compile command failed')

@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel init -i messages.pot -d app/translations -l' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')