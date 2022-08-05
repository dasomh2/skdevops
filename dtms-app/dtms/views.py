from django.shortcuts import render
from django.db import connection

def tableView(request):
  try:
    cursor = connection.cursor()
    query = "select * from information_schema.SCHEMATA"
    execute = cursor.execute(query)
    result = cursor.fetchall()

    connection.commit()
    connection.close()

  except:
    connection.rollback()
    print("Failed to select in DB")

  context = []
  for data in result:
    row = {'catalog_name': data[0],
           'schema_name': data[1],
           'default_ch_name': data[2],
           'default_co_name': data[3],
           'default_encryption': data[5]
           }
    context.append(row)

  # print(context)

  return render(request, 'dtms/index.html', {'context': context})
