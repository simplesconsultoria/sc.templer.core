# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

version = '20111209.01'

setup(
    name='sc.templer.core',
    version=version,
    description="Base templer structures for Simples Consultoria.",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Plone",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='simples_consultoria web command-line skeleton project',
    author='Simples Consultoria',
    author_email='products@simplesconsultoria.com.br',
    url='http://www.simplesconsultoria.com.br/',
    namespace_packages=['sc', 'sc.templer'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "templer.core",
        "templer.buildout",
    ],
    entry_points="""
    [paste.paster_create_template]
    python_package = sc.templer.core.base:NestedPackage
    plone_package = sc.templer.core.base:PlonePackage

    [templer.templer_structure]
    egg_docs_ex = sc.templer.core.structures:EggDocsStructure
    plone_testing_base = sc.templer.core.structures:PloneTestingStructure
    plone_testing_40 = sc.templer.core.structures:PloneTesting40Structure
    plone_testing_41 = sc.templer.core.structures:PloneTesting41Structure
    plone_testing_42 = sc.templer.core.structures:PloneTesting42Structure
    
    gs_nested_default = sc.templer.core.structures:GSDefaultProfileStructure
    gs_nested_uninstall = sc.templer.core.structures:GSUninstallProfileStructure
    gs_nested_init_content = sc.templer.core.structures:GSInitContentProfileStructure
    """,
    )
