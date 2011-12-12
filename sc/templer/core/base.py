# -*- coding:utf-8 -*-
import copy

from templer.core.base import get_var

from templer.core.vars import EASY
from templer.core.vars import EXPERT
from templer.core.vars import StringVar

from templer.core.base import BaseTemplate
from templer.core.nested_namespace import NestedNamespace

from sc.templer.core import DEFAULTS as D

from sc.templer.core.generic_setup import gs_vars


def base_vars():
    ''' Base variables for our templates '''
    vars = copy.deepcopy(NestedNamespace.vars)

    get_var(vars, 'author').default = D.get('author')
    get_var(vars, 'author_email').default = D.get('email')
    get_var(vars, 'url').default = D.get('url')
    get_var(vars, 'keywords').default = 'python simples_consultoria'
    get_var(vars, 'namespace_package').default = 'sc'
    get_var(vars, 'namespace_package2').default = 'project'
    get_var(vars, 'package').default = 'package'
    get_var(vars, 'license_name').default = 'GPL'
    return vars


class NestedPackage(BaseTemplate):

    summary = "Nested namespace template for Simples Consultoria's packages"
    help = """This is a base template for Simples Consultoria's projects that
              use a nested namespace (two dots in the name).
              """
    category = "Simples Consultoria"
    ndots = 2
    use_cheetah = True
    required_templates = []
    default_required_structures = ['egg_docs_ex', ]

    _template_dir = "templates/nested_namespace"

    vars = copy.deepcopy(base_vars())

    def check_vars(self, vars, cmd):
        if not cmd.options.no_interactive and \
           not hasattr(cmd, '_deleted_once'):
            del vars['package']
            cmd._deleted_once = True
        return super(NestedPackage, self).check_vars(vars, cmd)

    def has_structure(self, name=""):
        ''' Validates if we have a structure with a given name '''
        structures = [ep.name for ep in self.all_structure_entry_points()]
        return name in structures


class PlonePackage(NestedPackage):

    summary = "A Plone package template for Simples Consultoria's projects"
    help = """This is a base template for Simples Consultoria's Plone projects
              that use a nested namespace (two dots in the name).
              """

    required_templates = ['python_package', ]

    default_required_structures = ['bootstrap',
                                   'plone_testing_base']

    vars = copy.deepcopy(base_vars())

    vars.extend(copy.deepcopy(gs_vars))

    vars.append(
        StringVar(
            'plone_version',
            'Plone version',
            default='4.1',
            modes=(EASY, EXPERT),
           )
    )

    get_var(vars, 'keywords').default = 'python plone zope simples_consultoria'

    def add_plone_testing(self, version):
        ''' Adds the default testing configuration for the package '''

        def sanitize(version):
            version = version[:3].replace('.', '')
            return version

        structure = 'plone_testing_%s' % sanitize(version)
        if self.has_structure(structure):
            self.required_structures.append(structure)

    def has_profile(self, responses):
        ''' Return true if we have any GS profile '''
        return (responses.get('add_profile',False) or
                responses.get('add_profile_uninstall',False) or
                responses.get('add_profile_init_content',False))

    def check_vars(self, vars, cmd):
        responses = super(PlonePackage, self).check_vars(vars, cmd)
        self.add_plone_testing(responses['plone_version'])
        responses['has_profile'] = self.has_profile(responses)
        return responses
