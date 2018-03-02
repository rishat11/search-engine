from django.shortcuts import render
from django.db import connection


def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        if query == '':
            return render(request, 'search.html', {})
        query_words = query.split()

        t = 2
        order_str = 't1.amount'
        sql = 'select t1.data, t1.url from (select d.id, l.amount, d.url, d.data from documents as d inner join lemma as l on d.id = l.doc_id where l.text = %s) as t1'.format(query_words[0])
        for word in query_words[1:]:
            sql = "{} inner join (select d.id, l.amount from documents as d inner join lemma as l on d.id = l.doc_id where l.text =%s) as t{} on t1.id=t{}.id".format(sql, t, t)
            order_str = '{}+t{}.amount'.format(order_str, t)
            t += 1
        sql = '{} order by {} desc'.format(sql, order_str)
        with connection.cursor() as cursor:
            cursor.execute(sql, tuple(query_words))
            row = cursor.fetchall()

        return render(request, 'search.html', {'docs': row, 'q': query})
    elif request.method == 'GET':
        return render(request, 'search.html', {})
