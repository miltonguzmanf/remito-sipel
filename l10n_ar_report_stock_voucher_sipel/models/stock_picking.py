# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from datetime import datetime


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def print_report_remittance(self):
        return self.env.ref('l10n_ar_report_stock_voucher_sipel.report_remito').report_action(self, config=False)

    def get_line_remittance(self):
        list_line = []
        for rec in self:
            if rec.state == 'done':
                for line in rec.move_line_ids_without_package:
                    if line.product_id.default_code:
                        default_code = '['+ line.product_id.default_code +']'+' '+ line.product_id.name
                    else:
                        default_code = line.product_id.name
                    vals = {
                        'qty': int(line.qty_done),
                        'product': default_code,
                        'lot': line.lot_id.name,
                        'product_uom': line.product_uom_id.name,
                        'product_name': line.product_id.name,
                    }
                    list_line.append(vals)
            else:
                for line in rec.move_ids_without_package:
                    if line.product_id.default_code:
                        default_code = '['+ line.product_id.default_code +']'+' '+ line.product_id.name
                    else:
                        default_code = line.product_id.name
                    vals = {
                        'qty': int(line.product_uom_qty),
                        'product': default_code,
                        'lot': '',
                        'product_uom': line.product_uom_id.name,
                        'product_name': line.product_id.name,
                    }
                    list_line.append(vals)
        return list_line

    def get_location(self):
        agrupe_name = ''
        for rec in self:
            if rec.partner_id.city and rec.partner_id.state_id and rec.partner_id.zip:
                agrupe_name = rec.partner_id.city+', '+rec.partner_id.state_id.name + ', '+rec.partner_id.zip
            if rec.partner_id.city and rec.partner_id.state_id and not rec.partner_id.zip:
                agrupe_name = rec.partner_id.city+', '+rec.partner_id.state_id.name
            if rec.partner_id.city and not rec.partner_id.state_id and not rec.partner_id.zip:
                agrupe_name = rec.partner_id.city
        return agrupe_name

    def get_location_invoice(self):
        agrupe_name = ''
        for rec in self:
            if rec.sale_id:
                if rec.sale_id.partner_id.street and rec.sale_id.partner_id.city and rec.sale_id.partner_id.state_id and rec.sale_id.partner_id.zip:
                    agrupe_name = rec.sale_id.partner_id.street+', '+rec.sale_id.partner_id.city+', '+rec.sale_id.partner_id.state_id.name + ', '+rec.partner_id.zip
                if rec.sale_id.partner_id.street and rec.sale_id.partner_id.city and rec.sale_id.partner_id.state_id and not rec.sale_id.partner_id.zip:
                    agrupe_name = rec.sale_id.partner_id.street+', '+rec.sale_id.partner_id.city+', '+rec.sale_id.partner_id.state_id.name
                if rec.sale_id.partner_id.street and rec.sale_id.partner_id.city and not rec.sale_id.partner_id.state_id and not rec.sale_id.partner_id.zip:
                    agrupe_name = rec.sale_id.partner_id.street+', '+rec.sale_id.partner_id.city
                if rec.sale_id.partner_id.street and not rec.sale_id.partner_id.city and not rec.sale_id.partner_id.state_id and not rec.sale_id.partner_id.zip:
                    agrupe_name = rec.sale_id.partner_id.street
        return agrupe_name

    def get_datetoday(self):
        return datetime.today().date().__format__('%d/%m/%Y')

    def get_info(self):
        for rec in self:
            if rec.partner_id.mobile:
                complet_info = rec.partner_id.name or rec.partner_id.commercial_company_name +'. Cel: ' + rec.partner_id.mobile
            elif rec.partner_id.phone:
                complet_info = rec.partner_id.name or rec.partner_id.commercial_company_name + '. Tel: ' + rec.partner_id.phone
            else:
                complet_info = rec.partner_id.name or rec.partner_id.commercial_company_name
        return complet_info
