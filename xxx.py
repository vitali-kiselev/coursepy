import xlsxwriter
import calendar
name = 'Двоешник Виталий'
year = 2020
cal = calendar.TextCalendar(firstweekday=0)
#mounts = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
workbook = xlsxwriter.Workbook('D:/noSave.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})
table_header = workbook.add_format({'bold': True, 'font_size': 25})
year_font = workbook.add_format({'bold': True, 'font_size': 20})
mounth_font = workbook.add_format({'bold': True, 'font_size': 15})
workbook.formats[0].set_font_size(9)


worksheet.write('E1', f'Календарь от {name}', table_header)
worksheet.write('E2', f'Год: {year}', year_font)
table_style = 'Table Style Light 14'
current_row = 4
report_width = 7
worksheet.write(3, 5, cal.formatmonth(2016, 5), bold)



workbook.close()