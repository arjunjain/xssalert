'''
Created on May 6, 2011

@author: Arjun
'''

from distutils.core import setup
from distutils.command.install_data import install_data
from distutils.command.install import INSTALL_SCHEMES
import os
import sys

class osx_install_data(install_data):
    # On MacOS, the platform-specific lib dir is /System/Library/Framework/Python/.../
    # which is wrong. Python 2.5 supplied with MacOS 10.5 has an Apple-specific fix
    # for this in distutils.command.install_data#306. It fixes install_lib but not
    # install_data, which is why we roll our own install_data class.

    def finalize_options(self):
        # By the time finalize_options is called, install.install_lib is set to the
        # fixed directory, so we set the installdir to install_lib. The
        # install_data class uses ('install_data', 'install_dir') instead.
        self.set_undefined_options('install', ('install_lib', 'install_dir'))
        install_data.finalize_options(self)

if sys.platform == "darwin": 
    cmdclasses = {'install_data': osx_install_data} 
else: 
    cmdclasses = {'install_data': install_data} 

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

all_packages, all_data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
XSSAlert_dir = 'XSSAlert'

for dirpath, dirnames, filenames in os.walk(XSSAlert_dir):
    if '__init__.py' in filenames:
        all_packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        all_data_files.append((dirpath, [os.path.join(dirpath, f) for f in filenames]))
    
if len(sys.argv) > 1 and sys.argv[1] == 'bdist_wininst':
    for file_info in all_data_files:
        file_info[0] = '\\PURELIB\\%s' % file_info[0]

all_data_files=all_data_files+[("/usr/share/applications",["xssalert.desktop"]),('/usr/share/pixmaps',["XSSAlert/ui/images/xssalert.png"])]

setup(name='XSSAlert',
      version='1.1',
      description='Penetration testing tool For detecting XSS holes in web application',
      author='Arjun Jain',
      author_email='arjunjain08@gmail.com',
      url='http://sourceforge.net/projects/xssalert7/',
      download_url='http://sourceforge.net/projects/xssalert7/files/XSSAlert-1.1.tar.bz2/download',
      packages=all_packages,
      cmdclass = cmdclasses,
      data_files =all_data_files,
      scripts = ['xssalert'],
      platforms = ['Linux'],	 
      classifiers = ['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: GNU',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: PyQt :: 4.6',
                   ],
)
