def filter_html(html):
  # replace every NaN with an empty string
  html = html.replace('NaN','')

  # switch class on table
  html = html.replace('class="dataframe"','class="table"')

  # remove borders
  html = html.replace('border="1"','')

  # surround with reponsive tags
  html = "<div class='table-reponsive'>" + html + "</div>"
  return html


def table_to_html(file,table):
  import pandas as pd

  # read the csv
  dat = pd.ExcelFile(file)
  
  # collect data in all tabs
  tables = {
    sheet_name: dat.parse(sheet_name)
      for sheet_name in dat.sheet_names
    }
    
  # function parameter selects the table to print
  html = filter_html(tables[table].to_html())

  # open a file and write the html to that file
  table_doc = open(table + '.txt','w')
  table_doc.write(html)
  table_doc.close()