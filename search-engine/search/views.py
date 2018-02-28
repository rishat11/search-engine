from django.shortcuts import render
from django.db import connection


def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        if query == '':
            return render(request, 'search.html', {})
        query_words = query.split()
        sql = "SELECT d.data, d.url from documents as d where exists (select 1 from lemma where text = %s and doc_id = d.id)"
        for word in query_words[1:]:
            sql = "{} and exists (select 1 from lemma where text = %s and doc_id = d.id)".format(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql, tuple(query_words))
            row = cursor.fetchall()
        return render(request, 'search.html', {'docs': row, 'q': query})
    elif request.method == 'GET':
        return render(request, 'search.html', {})
