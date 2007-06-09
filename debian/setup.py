from distutils.core import setup

import S3.PkgInfo

author='Michal Ludvig'
author_email='michal@logix.cz'

long_description='''
%s

Authors:
--------
    %s  <%s>
''' % (S3.PkgInfo.long_description, author, author_email)

setup(
    name=S3.PkgInfo.package,
    version=S3.PkgInfo.version,
    packages=['S3'],
    scripts=['s3cmd'],
    author=author,
    author_email=author_email,
    url=S3.PkgInfo.url,
    license=S3.PkgInfo.license,
    description=S3.PkgInfo.short_description,
    long_description=long_description
)
