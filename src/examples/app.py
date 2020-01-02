#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive DigitalOcean API
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive DigitalOcean API.
#
# Hive DigitalOcean API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive DigitalOcean API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive DigitalOcean API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base

class DigitaloceanApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "digitalocean",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.droplets()

    @appier.route("/actions", "GET")
    def actions(self):
        url = self.ensure_api()
        if url: return self.redirect(url)
        api = self.get_api()
        actions = api.list_actions()
        return actions

    @appier.route("/droplets", "GET")
    def droplets(self):
        url = self.ensure_api()
        if url: return self.redirect(url)
        api = self.get_api()
        droplets = api.list_droplets()
        return droplets

    @appier.route("/create_dummy", "GET")
    def create_dummy(self):
        url = self.ensure_api()
        if url: return self.redirect(url)
        api = self.get_api()
        dummy = dict(
            name = self.field("name", "dummy"),
            region = self.field("region", "ams1"),
            size = self.field("size", "512mb"),
            image = self.field("image", "ubuntu-14-04-x64"),
            ssh_keys = self.field("ssh_keys", None),
            backups = self.field("backups", False, cast = bool),
            ipv6 = self.field("ipv6", False, cast = bool),
            private_networking = self.field("private_networking", None),
            user_data = self.field("user_data", None)
        )
        droplet = api.create_droplet(dummy)
        return droplet

    @appier.route("/logout", "GET")
    def logout(self):
        return self.oauth_error(None)

    @appier.route("/oauth", "GET")
    def oauth(self):
        code = self.field("code")
        error = self.field("error")
        appier.verify(
            not error,
            message = "Invalid OAuth response (%s)" % error,
            exception = appier.OperationalError
        )
        api = self.get_api()
        access_token = api.oauth_access(code)
        self.session["do.access_token"] = access_token
        return self.redirect(
            self.url_for("digitalocean.index")
        )

    @appier.exception_handler(appier.OAuthAccessError)
    def oauth_error(self, error):
        if "do.access_token" in self.session: del self.session["do.access_token"]
        return self.redirect(
            self.url_for("digitalocean.index")
        )

    def ensure_api(self):
        access_token = self.session.get("do.access_token", None)
        if access_token: return
        api = base.get_api()
        return api.oauth_authorize()

    def get_api(self):
        access_token = self.session and self.session.get("do.access_token", None)
        api = base.get_api()
        api.access_token = access_token
        return api

if __name__ == "__main__":
    app = DigitaloceanApp()
    app.serve()
else:
    __path__ = []
