# aptinstall.py

#: i need to have apt installed
########################## DEPRECATE BECAUSE installing apt is not as complete
########################## as using fabric despite 3.0 issues

import apt
import sys
import requests

def simple_apt_install(pkg_name):
    """

    """

    cache = apt.cache.Cache()
    cache.update()

    pkg = cache[pkg_name]
    if pkg.is_installed:
        print "{pkg_name} already installed".format(pkg_name=pkg_name)
    else:
        pkg.mark_install()

        try:
	    cache.commit()
        except Exception, arg:
	    print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def download_and_dpkg():
    url = 'https://github.com/atom/atom/releases/download/v1.12.5/atom-amd64.deb'
    pkg = download_file(url)
    dp = apt.debfile.DebPackage(filename=pkg)
    dp.install()

def install_base():
    """
    """
    pkgs = ["fabric", "emacs"]
    for pkg_name in pkgs:
        simple_apt_install(pkg_name)

def main():
    install_base()
#    download_and_dpkg()

if __name__ == '__main__':
    main()
