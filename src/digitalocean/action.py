#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive DigitalOcean API
# Copyright (c) 2008-2015 Hive Solutions Lda.
#
# This file is part of Hive DigitalOcean API.
#
# Hive DigitalOcean API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive DigitalOcean API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive DigitalOcean API. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

class ActionApi(object):

    def list_actions(self):
        url = self.base_url + "actions"
        contents = self.get(url)
        return contents

    def get_action(self, action_id):
        url = self.base_url + "actions/%d" % action_id
        contents = self.get(url)
        return contents["action"]
