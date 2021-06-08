# Copyright 2020 AITIC S.A.S
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Argentinian Stock Voucher Report Sipel",
    "summary": "Stock Voucker Report",
    "version": "13.0.2.0.0",
    "development_status": "Beta",
    "category": "Localization/Argentina",
    "website": "https://www.aitic.com.ar/",
    "author": "AITIC S.A.S.",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["stock_voucher", "sale", "stock", "l10n_ar_report_invoice_aitic", "l10n_ar_transporter", "external_sale_agent"],
    "data": [
        'views/report_invoice.xml',
        'report/report_stock_picking_remittance.xml',
    ]
}
