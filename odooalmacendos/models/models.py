# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odooalmacen(models.Model):
#     _name = 'odooalmacen.odooalmacen'
#     _description = 'odooalmacen.odooalmacen'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api
class almacen(models.Model):
	_name = 'odooalmacen.almacen'
	_description = 'model almacen'

	name = fields.Char('Id',required=True)
	tipo = fields.Char(string='Tipo',required=True)
	encargados_ids = fields.One2many('odooalmacen.encargado','encargado_id',string='EncargadoAlmacen')
class encargado(models.Model):
	_name = 'odooalmacen.encargado'
	_description = 'model encargado'

	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	encargado_id=fields.Many2one('odooalmacen.almacen',string='encargado')
class camion(models.Model):
	_name = 'odooalmacen.camion'
	_description = 'model camion'
	name = fields.Char('Id',required=True)
	tamano = fields.Char(string='Tamano',required=True)
class camionero(models.Model):
	_name = 'odooalmacen.camionero'
	_description = 'model camionero'
	name = fields.Char('Id',required=True)
	nombre = fields.Char(string='Nombre',required=True)
class moviles(models.Model):
	_name = 'odooalmacen.moviles'
	_description = 'model moviles'

	name = fields.Char('Stock',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	marca = fields.Char(string='Marca',required=True)

class ordenadores(models.Model):
	_name = 'odooalmacen.ordenadores'
	_description = 'model ordenadores'

	name = fields.Char('Stock',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	marca = fields.Char(string='Marca',required=True)

class tablet(models.Model):
	_name = 'odooalmacen.tablet'
	_description = 'model tablet'

	name = fields.Char('Stock',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	marca = fields.Char(string='Marca',required=True)