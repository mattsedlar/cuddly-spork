def filter_html(html):
  # replace every NaN with an empty string
  html = html.replace('NaN','')
  html = html.replace('nan%','')

  # switch class on table
  html = html.replace('class="dataframe"','class="table"')
  
  # add bg-primary class to thead
  html = html.replace('<thead>\n    <tr ','<thead>\n    <tr class="bg-primary" ')

  # remove borders
  html = html.replace('border="1"','')

  # surround with reponsive tags
  html = "<div class='table-reponsive'>" + html + "</div>"
  return html

def stringify(x):
  # coerce into float if it isn't already
  x = float(x)
  x = str(round(x * 100,1)) + "%"
  return x

def roundify(x):
  # coerce into float if it isn't already
  x = float(x)
  x = round(x,1)
  return x

def transform(df,ints,skip):
  if type(ints) == list:
    for int in ints:
      df.iloc[skip:,int] = df.iloc[skip:,int].apply(stringify)
      
  else:
    df.iloc[skip:,ints] = df.iloc[skip:,ints].apply(stringify)
    
def round_up(df,ints,skip):
    if type(ints) == list:
      for int in ints:
        df.iloc[skip:,int] = df.iloc[skip:,int].apply(roundify)
    else:
      df.iloc[skip:,ints] = df.iloc[skip:,ints].apply(roundify)

def table_to_html(file,table,ints=None,rounding=False,skip=0):
  import pandas as pd
  import xlrd

  # read the csv
  dat = pd.read_excel(file,sheetname=table)
  
  # call transform function here if ints
  if ints != None:
    if rounding == True:
      round_up(dat,ints,skip)
    else:
      transform(dat,ints)

  # function parameter selects the table to print
  html = filter_html(dat.to_html())

  # open a file and write the html to that file
  table_doc = open(table + '.html','w')
  table_doc.write(html)
  table_doc.close()