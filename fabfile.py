import time
from fabric.api import local, env
from fabric.contrib.project import rsync_project

env.hosts = ['admin@icron.org']
#env.path = '/home/admin/web/icron.org/public_html/'

def push():
    local('git push')

def serve():
    local('run-rstblog serve')

def build():
    # hook windows rights
	#local('cacls _build /T /e /g Alexander:f')
	#local('rmdir /S _build')
	
    # Build HTML
    local('rm -rf _build/ && run-rstblog build')

    # Generate sitemaps
    #local('python gensitemap.py > _build/sitemap.xml')

    # Minify CSS
    local('cssmin < _build/static/style.css > _build/static/style.min.css')
    local('mv _build/static/style.min.css _build/static/style.css')
    local('cssmin < _build/static/_pygments.css > _build/static/_pygments.min.css')
    local('mv _build/static/_pygments.min.css _build/static/_pygments.css')

    # Add timestamp to css files
    #local('find _build -type f -exec sed -i "s/\(link.*\)style.css/\\1style.css?%s/g" {} \;' % int(time.time()))
    #local('find _build -type f -exec sed -i "s/\(link.*\)_pygments.css/\\1_pygments.css?%s/g" {} \;' % int(time.time()))

def sync():
    rsync_project(remote_dir='/home/admin/web/icron.org/public_html/',
                  local_dir='_build/',
                  delete=True,
				  extra_opts = '--chmod=Du=rwx,go=rx,Fu=rw,og=r',
                  exclude=['*.py', '*.pyc', 'requirements.txt'])

def deploy():
    build()
    sync()

def publish():
    deploy()
    push()