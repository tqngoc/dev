# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Filter',
    'version': '1.0',
    'website': 'http://www.hhdgroup.com/',
    'author': 'HHD Group',
    'category': 'HHD Group',
    'sequence': 10,
    'summary': 'Projects, Tasks',
    'depends': [
        'project',
    ],
    'description': """
Projects, Tasks Filter
=====================================================

* Today
* This Week
* This Month
* Yesterday
* Last week
* Last Month
    """,
    'data': [
        'views/tasks_filter.xml',
    ],
    'qweb': [],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
