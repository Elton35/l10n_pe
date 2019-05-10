# -*- coding: utf-8 -*-
from odoo import models, fields, api

class einvoice_catalog_01(models.Model):
    _name = "einvoice.catalog.01"
    _description = 'Codigo de Tipo de documento'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
    label = fields.Char(string='Label to print', size=256)
    
    @api.multi
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result

class einvoice_catalog_06(models.Model):
    _name = "einvoice.catalog.06"
    _description = 'Tipo de documento de Identidad'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
    default = fields.Char(string='Valor por defecto', size=128)
    
    @api.multi
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result
        
class einvoice_catalog_07(models.Model):
    _name = "einvoice.catalog.07"
    _description = 'Codigos de Tipo de Afectacion del IGV'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
    no_onerosa = fields.Boolean(string='No onerosa')
    type = fields.Selection([('gravado','Gravado'),('exonerado','Exonerado'),('inafecto','Inafecto')],string='Tipo')
    
    @api.multi
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result

class einvoice_catalog_08(models.Model):
    _name = "einvoice.catalog.08"
    _description = 'Codigos de Tipo de Afectacion del IGV'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
	
    @api.multi
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result

class einvoice_catalog_09(models.Model):
    _name = "einvoice.catalog.09"
    _description = 'Codigos de Tipo de Nota de Credito Electronica'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
    
    @api.multi
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result

class einvoice_catalog_10(models.Model):
    _name = "einvoice.catalog.10"
    _description = 'Codigos de Tipo de Nota de Debito Electronica'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
    
    @api.multi
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result

class einvoice_catalog_16(models.Model):
    _name = "einvoice.catalog.16"
    _description = 'Codigos - Tipo de Precio de Venta Unitario'

    code = fields.Char(string='Code', size=4, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
	
    @api.multi
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result
        
class einvoice_catalog_25(models.Model):
    _name = "einvoice.catalog.25"
    _description = 'Codigos - Producto SUNAT'

    code = fields.Char(string='Code', size=12, index=True, required=True)
    name = fields.Char(string='Description', size=128, index=True, required=True)
	
    @api.multi
    @api.depends('code', 'name')
    def name_get(self):
        result = []
        for table in self:
            l_name = table.code and table.code + ' - ' or ''
            l_name +=  table.name
            result.append((table.id, l_name ))
        return result
    
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('code', '=ilike', name.split('-')[0] + '%'), ('name', operator, name)]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ['&', '!'] + domain[1:]
        ids = self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
        return self.browse(ids).name_get()

