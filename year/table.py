import xlsxwriter

def build_xlsx_data():

    workbook = xlsxwriter.Workbook('Tablefile.xlsx', )

    worksheet = workbook.add_worksheet('Report')
    current_row = 0
    report_width = 7

    workbook.formats[0].set_font_size(9)
    table_style = 'Table Style Light 14'

    workbook.close()