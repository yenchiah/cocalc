
# This file is part of CoCalc: Copyright © 2020 Sagemath, Inc.
# License: AGPLv3 s.t. "Commons Clause" – read LICENSE.md for details

###
# To do development on this, install it locally:
#   pip install --user --upgrade smc_pyutil/
###

# CRITICAL: I don't know any other way to ensure the permissions are
# right on the templates than this
import os
from os.path import join
path = os.path.dirname(os.path.realpath(__file__))
os.system("chmod a+r -R %s" % join(path, "smc_pyutil", "templates"))


def readme():
    with open('README.md') as f:
        return f.read()


# from https://github.com/ninjaaron/fast-entry_points/ issue https://github.com/sagemathinc/cocalc/issues/2259
import fastentrypoints
from setuptools import setup, find_packages

# This checks, if setup.py is run with 'install --user'
# in that case we assume it is installed for development and do NOT change the python executable.
# Therefore we want to load the local library via the site.py mechanism.
# (this mimics http://svn.python.org/projects/python/trunk/Lib/distutils/dist.py, called in setup behind the scenes)
from distutils.core import Distribution
d = Distribution()
d.parse_command_line()

# CRITICAL!
# Uses a wrapped python executable to not load the user's "site" packages in ~/.local.
# Otherwise, setuptool's startup scripts do not work, if there is a conflicting
# setuptools version in .local/lib/python-packages (or, any other locally installed python lib)
# setting sys.executable changes the she-bang #!... at the top of these scripts
# credits to http://stackoverflow.com/a/17329493
python2_nosite = '/usr/local/bin/python2-nosite'
# don't overwrite for local smc-in-smc development
if 'user' not in d.command_options.get("install", {}).keys():
    # check, if python2_nosite exists and is executable
    if os.path.isfile(python2_nosite) and os.access(python2_nosite, os.X_OK):
        import sys
        sys.executable = python2_nosite

setup(
    name='smc_pyutil',
    version='1.1',
    description='CoCalc Python Utilities',
    long_description=readme(),
    url='https://github.com/sagemathinc/cocalc',
    author='SageMath, Inc.',
    author_email='office@sagemath.com',
    license='GPLv3+',
    packages=find_packages(),
    install_requires=['markdown2', 'psutil', 'PyYAML', 'ansi2html'],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Mathematics :: Server',
    ],
    keywords='server mathematics cloud',
    scripts=['smc_pyutil/bin/smc-sage-server'],
    entry_points={
        'console_scripts': [
            'open                 = smc_pyutil.smc_open:main',
            'close                = smc_pyutil.smc_close:main',
            # START deprecated smc-*
            'smc-sagews2pdf       = smc_pyutil.sagews2pdf:main',
            'smc-sws2sagews       = smc_pyutil.sws2sagews:main',
            'smc-docx2txt         = smc_pyutil.docx2txt:main',
            'smc-open             = smc_pyutil.smc_open:main',
            'smc-new-file         = smc_pyutil.new_file:main',
            'smc-status           = smc_pyutil.status:main',
            'smc-jupyter          = smc_pyutil.jupyter_notebook:main',
            'smc-jupyter-no-output= smc_pyutil.jupyter_delete_output:main',
            'smc-ipynb2sagews     = smc_pyutil.ipynb2sagews:main',
            'smc-ls               = smc_pyutil.git_ls:main',
            'smc-compute          = smc_pyutil.smc_compute:main',
            'smc-start            = smc_pyutil.start_smc:main',
            'smc-stop             = smc_pyutil.stop_smc:main',
            'smc-update-snapshots = smc_pyutil.update_snapshots:update_snapshots',
            'smc-top              = smc_pyutil.smc_top:main',
            'smc-git              = smc_pyutil.smc_git:main',
            'smc-html2sagews      = smc_pyutil.html2sagews:main',
            'smc-rmd2html         = smc_pyutil.rmd2html:main',
            'smc-java2html        = smc_pyutil.java2html:main',
            'smc-m2sagews         = smc_pyutil.m2sagews:main',
            'smc-sagews2ipynb     = smc_pyutil.sagews2ipynb:main',
            # END deprecated smc-*
            'cc-sagews2pdf       = smc_pyutil.sagews2pdf:main',
            'cc-sws2sagews       = smc_pyutil.sws2sagews:main',
            'cc-docx2txt         = smc_pyutil.docx2txt:main',
            'cc-open             = smc_pyutil.smc_open:main',
            'cc-close            = smc_pyutil.smc_close:main',
            'cc-new-file         = smc_pyutil.new_file:main',
            'cc-status           = smc_pyutil.status:main',
            'cc-jupyter          = smc_pyutil.jupyter_notebook:main',
            'cc-jupyterlab       = smc_pyutil.jupyter_lab:main',
            'cc-jupyter-no-output= smc_pyutil.jupyter_delete_output:main',
            'cc-jupyter-classic-open = smc_pyutil.jupyter_notebook:prepare_file_for_open',
            'cc-ipynb2sagews     = smc_pyutil.ipynb2sagews:main',
            'cc-ls               = smc_pyutil.git_ls:main',
            'cc-compute          = smc_pyutil.smc_compute:main',
            'cc-start            = smc_pyutil.start_smc:main',
            'cc-stop             = smc_pyutil.stop_smc:main',
            'cc-update-snapshots = smc_pyutil.update_snapshots:update_snapshots',
            'cc-top              = smc_pyutil.smc_top:main',
            'cc-git              = smc_pyutil.smc_git:main',
            'cc-html2sagews      = smc_pyutil.html2sagews:main',
            'cc-rmd2html         = smc_pyutil.rmd2html:main',
            'cc-java2html        = smc_pyutil.java2html:main',
            'cc-m2sagews         = smc_pyutil.m2sagews:main',
            'cc-sagews2ipynb     = smc_pyutil.sagews2ipynb:main',
            'cc-ipynb-to-pdf     = smc_pyutil.ipynb_to_pdf:main'
        ]
    },
    include_package_data=True)
