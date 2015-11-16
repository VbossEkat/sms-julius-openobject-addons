# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name": "Task Work add project",
    "summary": "Add project in task work",
    "version": "1.0",
    "author": "Julius Network Solutions",
    "website": "http://www.julius.fr",
    'category': 'Project Management',
    "depends": [
        "project",
        "project_task_work_calendar_view",
    ],
    "description": """
Improve view of task works.
---------------------------

Add related project in task work views.
""",
    "demo" : [],
    "data": [
        "project_task_work_view.xml", 
    ],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: