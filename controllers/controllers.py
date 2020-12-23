# -*- coding: utf-8 -*-
from odoo import http


class Bookstore(http.Controller):
    @http.route('/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('bookstore.index', {
            'root': '',
        })

    @http.route('/books/', auth='public', website=True)
    def list(self, **kw):
        print("books")
        return http.request.render('bookstore.listing', {
            'root': '',
            'objects': http.request.env['bookstore.book'].search([]),
        })

    @http.route('/books/<model("bookstore.book"):obj>/', auth='public', website=True)
    def object(self, obj, **kw):
        return http.request.render('bookstore.object', {
            'object': obj
        })