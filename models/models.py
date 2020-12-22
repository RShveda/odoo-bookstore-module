# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Category(models.Model):
    _name = 'bookstore.category'
    _description = 'Book category. One book may be listed by up to three categories.'

    name = fields.Char(required=True)
    book_ids = fields.Char(required=True, default="m2m")


class Author(models.Model):
    _name = 'bookstore.author'
    _description = 'Book authors. Author may write multiple books and some books can be written in accompany ' \
                   'with other authors.'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    full_name = fields.Char(compute="_compute_full_name")
    book_ids = fields.Char(required=True, default="m2m")

    def _compute_full_name(self):
        for record in self:
            record.full_name = "{} {}".format(self.first_name, self.last_name)


class Publisher(models.Model):
    _name = 'bookstore.publisher'
    _description = "Book publisher. One Publisher may publish many books."

    name = fields.Char(required=True)
    book_ids = fields.Char(required=True, default="o2m")


class Book(models.Model):
    _name = 'bookstore.book'
    _description = "Book item which is written by Authors and may be listed by multiple (up to 3) existing Categories"

    title = fields.Char(required=True, string="Book title")
    year = fields.Integer(required=True, string="Year")
    author_ids = fields.Char(required=True, string="Authors", default="m2m")
    category_ids = fields.Char(required=True, string="Categories", default="m2m")
    publisher_id = fields.Char(required=True, string="Publisher", default="m2o")
    in_stock = fields.Integer(required=True, string="Stock")


class RentalRecord(models.Model):
    _name = 'bookstore.rental_record'
    _description = "Holds information about rental operations. Rent can be performed by one user on one book."

    taker_id = fields.Char()
    book_id = fields.Char()
    taken_date = fields.Date()
    returned_date = fields.Date()
