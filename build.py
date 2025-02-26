import fabricate

def build():
    fabricate.run('go', 'build')

def clean():
    fabricate.autoclean()

if __name__ == '__main__':
    fabricate.main()

