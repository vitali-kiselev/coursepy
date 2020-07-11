import xlsxwriter


@staticmethod
def build_xlsx_data():
        # output = io.BytesIO()

        # workbook = xlsxwriter.Workbook(output, )
        workbook = xlsxwriter.Workbook('D:/my_output_file.xlsx')

        worksheet = workbook.add_worksheet('Report')

        current_row = 0

        report_width = 7


        workbook.formats[0].set_font_size(9)

        # COLORS
        dark = "444444"
        white = "ffffff"
        bg_color = 'ffffff'
        
        table_style = 'Table Style Light 14'

        # https://d295c5dn8dhwru.cloudfront.net/wp-content/uploads/2019/06/09043133/44.png

        am_dt_format = workbook.add_format({'num_format': 'mmm d yyyy hh:mm AM/PM', 'font_size': 9})
        date_format = workbook.add_format({'num_format': 'mmm d yyyy', 'font_size': 9})
        bold = workbook.add_format({'bold': True})
        
        table_header = workbook.add_format({'bold': True, 'font_size': 9})

        money = workbook.add_format({'num_format': '$#,##0.00', 'font_size': 9})
        
        no_header = workbook.add_format({'font_size': 1})
        
        merge_header = workbook.add_format({
            'bold': 1,
            'border': 0,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'white'})


        name = 'Ivanov'
        some_sum = 0


        start_date = datetime.date.today()-datetime.timedelta(days=7)
        end_date = datetime.date.today()

       # worksheet.merge_cells(start_current_row, start_column=1, end_current_row, end_column=report_width)

        worksheet.merge_range('A{}:G{}'.format(current_row+1, current_row+1), 'Report {}'.format(name), merge_header)

        current_row += 1

        worksheet.write(current_row, 0, 'Period:', bold)
        worksheet.write(current_row, 1, '{:%m/%d/%Y} to {:%m/%d/%Y}'.format(start_date, end_date), bold)
        current_row += 1

        worksheet.write(current_row, 0, 'Total:', bold)
        worksheet.write(current_row, 1, some_sum, money)

        current_row += 1

        current_row += 1

        
        worksheet.write(current_row, 0, 'Items', bold)
        current_row += 1
        
        # ----Trips Table----
        columns_widths = {
            0: 20,
            1: 20,
            2: 20,
            3: 7,
            4: 40,
            5: 7,
            6: 10,
        }

        for k, v in columns_widths.items():
            worksheet.set_column(k, k, v)

        current_row += 1

        first_table_row = last_table_row = current_row

        t_data = []

        some_objects = [{
            'number': 11,
            'start_dttm': datetime.datetime.now(),
            'end_dttm': datetime.datetime.now(),
            'units': 13,
            'description': 'Some notes',
            'amount': 100.00,
            'avg_price': 0,
        }]

        for line in some_objects:
            
            t_data.append(dict(
                number = line['number'],
                start_dttm = line['start_dttm'],
                end_dttm = line['end_dttm'],
                units = line['units'],
                description = line['description'],
                amount = line['amount'],
                avg_price = line['amount'] / line['units'] if line['units'] else 0,
            ))

            current_row+=1
            last_table_row+=1

        table_data_columns = [
            dict(header='ID#', total_string='Totals'),
            dict(header='Start Date Time', format=am_dt_format),
            dict(header='End Date Time', format=am_dt_format),
            dict(header='Units', total_function='SUM', ),
            dict(header='Notes', ),
            dict(header='Amount', total_function='SUM', format=money),
            dict(header='AVG', total_function='average', format=money),
        ]


        t_options = {
            'data': t_data,
            'total_row': 1,
            'style': table_style,
            'columns': table_data_columns
        }
        worksheet.add_table('A{}:G{}'.format(first_table_row, last_table_row), options=t_options)

        current_row += 1


        workbook.close()

        return True

#        output.seek(0)
#        data = output.read()
#        return data