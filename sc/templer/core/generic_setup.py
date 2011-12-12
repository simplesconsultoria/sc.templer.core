# -*- coding:utf-8 -*-
from templer.core.vars import EXPERT
from templer.core.vars import BooleanVar


gs_vars = [
        BooleanVar(
            'add_profile',
            title='Register a Default Profile',
            description='Should this package register a Default GS Profile',
            modes=(EXPERT, ),
            default=True,
            structures={'False': None, 'True': 'gs_nested_default'},
        ),
        BooleanVar(
            'add_profile_uninstall',
            title='Register an Uninstall Profile',
            description='Should this package register an Uninstall GS Profile',
            modes=(EXPERT, ),
            default=True,
            structures={'False': None, 'True': 'gs_nested_uninstall'},
        ),
]