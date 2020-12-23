# -*- coding: utf-8 -*-
from odoo import http


class Bookstore(http.Controller):
    @http.route('/bookstore/', auth='public')
    def index(self, **kw):
        return http.request.render('bookstore.index', {
            'root': '/bookstore',
        })

    @http.route('/bookstore/books/', auth='public')
    def list(self, **kw):
        return http.request.render('bookstore.listing', {
            'root': '/bookstore',
            'objects': http.request.env['bookstore.book'].search([]),
        })

    @http.route('/bookstore/books/<model("bookstore.book"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('bookstore.object', {
            'object': obj
        })
