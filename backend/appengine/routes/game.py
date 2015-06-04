# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required

@login_not_required
@no_csrf
def index():
    return TemplateResponse()

@login_not_required
@no_csrf
def drawing_canvas():
    return TemplateResponse()

@login_not_required
@no_csrf
def canvas_images():
    return TemplateResponse()
