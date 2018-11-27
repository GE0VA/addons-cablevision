# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime, timedelta
import io
import logging

_logger = logging.getLogger(__name__)

try:
    import xlwt
except ImportError:
    _logger.debug('Cannot `import xlwt`.')

try:
    import base64
except ImportError:
    _logger.debug('Cannot `import base64`.')


class PartnerReport(models.TransientModel):
	_inherit = 'tecnico.wizard'
	_description='Reporte de Clientes'
	
	tecnico = fields.Many2one(comodel_name="tecnico", string="Tecnico", required=False, )
	
	def get_user(self):
		return self.env['res.users'].browse(self._uid).name

	@api.multi
	def print_xls(self):
		return self.make_excel()
	
	@api.multi
	def make_excel(self):
		workbook = xlwt.Workbook(encoding="utf-8")
		worksheet = workbook.add_sheet("Tecnicos")
		
		# Styles for cells
		style_title = xlwt.easyxf("font:height 300; font: name Liberation Sans, bold on,color black; align: horiz left")
		style_table_header = xlwt.easyxf(
			"font:height 200; font: name Liberation Sans, bold on,color black; align: horiz left")
		style_table_header_right = xlwt.easyxf(
			"font:height 200; font: name Liberation Sans, bold on,color black; align: horiz right")
		style_table_data_text = xlwt.easyxf(
			"font:height 200; font: name Liberation Sans,color black; align: horiz left")
		style_table_data_text_bold = xlwt.easyxf(
			"font:height 200; font: name Liberation Sans, bold on,color black; align: horiz left")
		style_table_data_numbers = xlwt.easyxf(
			"font:height 200; font: name Liberation Sans,color black; align: horiz right")
		style_table_data_numbers_bold = xlwt.easyxf(
			"font:height 200; font: name Liberation Sans, bold on,color black; align: horiz right")
		style_table_header_1 = xlwt.easyxf("font:height 200; font: name Liberation Sans; align: horiz left")
		
		style_total = xlwt.XFStyle()
		style_total.borders.top = 1
		style_total.borders.top_colour = 0
		style_total.font.height = 200
		style_total.font.name = "Liberation Sans"
		style_total.font.bold = "on"
		
		# Make report header
		worksheet.write_merge(0, 1, 0, 9, "Técnicos", style=style_title)
		row = 2
		worksheet.write(row, 0, self.env.user.company_id.name, style=style_table_header_1)

		#body
		row += 2
		worksheet.write_merge(row, row, 0, 4, 'Licencias del Técnico', style=style_table_header)
		row += 1
		worksheet.write(row, 0,  "Licencia", style=style_table_header)
		worksheet.write(row, 1,  "Fecha", style=style_table_header)

		data = self.tecnico
		# Make report body
		for this in data.licencias_ids:
			row += 1
			#
			# identification_type = ''
			# if partner.identification_type:
			# 	identification_type = dict(self.env['res.partner'].fields_get(allfields=['identification_type'])['identification_type']['selection'])[
			# 	partner.identification_type]

			worksheet.write(row, 0, this.licencia_id.name , style=style_table_data_text)
			worksheet.write(row, 1, this.date_due, style=style_table_data_text)

		file_data = io.BytesIO()
		workbook.save(file_data)
		
		wiz_id = self.env['save.tecnico.wizard'].create({
			'state': 'get',
			'data': base64.encodestring(file_data.getvalue()),
			'name': "Tecnicos.xls"
		})
		
		return {
			'type': 'ir.actions.act_window',
			'name': 'Reporte XLS',
			'res_model': 'save.tecnico.wizard',
			'view_mode': 'form',
			'view_type': 'form',
			'res_id': wiz_id.id,
			'target': 'new'
		}

class TecnicoReportSaveWizard(models.TransientModel):
	_name = "save.tecnico.wizard"
	
	name = fields.Char('filename', readonly=True)
	data = fields.Binary('file', readonly=True)
