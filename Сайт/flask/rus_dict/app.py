# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, request, render_template
from backend import join_search_tables, join_search_conditions, search_query, load_page, resource_genre
import sqlite3 as sqlite
import os


app = Flask(__name__)

def names():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Database","Dictionary_Final.db")
    return(db_path)

connection = sqlite.connect(names(), check_same_thread=False)
cursor = connection.cursor()

@app.route('/')
def hi():
    return redirect(url_for('main'))

@app.route('/main_page')
def main():
    return render_template('main_page.html')

@app.route('/e_main_page')
def e_main():
    return render_template('e_main_page.html')

@app.errorhandler(Exception)
def not_found_error(error):
    print(error)
    return render_template('error.html')

@app.route('/search1', methods=['GET', 'POST'])
def search_wrd():
    if request.method == 'POST':
        query = []
        for i in request.form:
            parameter = i
            p_value = request.form.getlist(i)
            if p_value[0] != '':
                query.append([parameter, p_value])
        #print(query)
        result = list(search_query(join_search_tables(query), join_search_conditions(query)))
        print(result)
        if len(result) == 1:
            return redirect(url_for('result', word=result[0]))  # Change 'result_<word>' to 'result'
        else:
            return render_template('result.html', words_list=result)
    else:
        return render_template('search1.html')


@app.route('/e_search1', methods=['GET', 'POST'])
def e_search_wrd():
    if request.method == 'POST':
        query = []
        for i in request.form:
            parameter = i
            p_value = request.form.getlist(i)
            if p_value[0] != '':
                query.append([parameter, p_value])
        #print(query)
        result = list(search_query(join_search_tables(query), join_search_conditions(query)))
        print(result)
        if len(result) == 1:
            return redirect(url_for('e_result', word=result[0]))  # Change 'result_<word>' to 'result'
        else:
            return render_template('e_result.html', words_list=result)
    else:
        return render_template('e_search1.html')


@app.route('/result/<word>', methods=['GET'])  # Change '/result_<word>' to '/result/<word>'
def result(word):
    print(word)
    text = load_page(word.upper())
    if not text:
        return render_template('result.html', words_list=word)
    return render_template('word_entry.html', word=text)


@app.route('/e_result/<word>', methods=['GET'])  # Change '/result_<word>' to '/result/<word>'
def e_result(word):
    print(word)
    text = load_page(word.upper())
    if not text:
        return render_template('e_result.html', words_list=word)
    return render_template('e_word_entry.html', word=text)



@app.route('/result_list', methods=['GET'])
def result_list(words_list):
    return render_template('result.html', words_list=words_list)

@app.route('/e_result_list', methods=['GET'])
def e_result_list(words_list):
    return render_template('e_result.html', words_list=words_list)


@app.route('/source_search', methods=['GET', 'POST'])
def search_txt():
    if request.method == 'POST':
        query = []
        result = []
        genres_search_result = []
        for i in request.form:
            #try:
            parameter = i
            p_value = request.form.getlist(i)
                # ищем отдельно по жанрам
            if parameter == "source_genre" and p_value[0] != '':
                genres_search_result = resource_genre([parameter, p_value])
                print(genres_search_result)
                pass
            else:
                if p_value[0] != '':
                    query.append([parameter, p_value])


        print(f"query: {query}")
        # если есть еще условия кроме жанра
        if query:
            query_result = search_query(join_search_tables(query), join_search_conditions(query))
            print(query_result)
            result = list(query_result)
        else:
            # иначе итоговые рез = поиск по жанрам
            result = genres_search_result
        print(len(result))
        # если они оба есть, найду пересечение
        if genres_search_result != [] and query != []:
            result = list(genres_search_result & result)
        if len(result) == 1:
            return redirect(url_for('result', word=result[0]))
        else:
            return render_template('result.html', words_list=result)
    else:
        return render_template('source_search.html')


@app.route('/e_source_search', methods=['GET', 'POST'])
def e_search_txt():
    if request.method == 'POST':
        query = []
        result = []
        genres_search_result = []
        for i in request.form:
            #try:
            parameter = i
            p_value = request.form.getlist(i)
                # ищем отдельно по жанрам
            if parameter == "source_genre" and p_value[0] != '':
                genres_search_result = resource_genre([parameter, p_value])
                print(genres_search_result)
                pass
            else:
                if p_value[0] != '':
                    query.append([parameter, p_value])


        print(f"query: {query}")
        # если есть еще условия кроме жанра
        if query:
            query_result = search_query(join_search_tables(query), join_search_conditions(query))
            print(query_result)
            result = list(set(query_result))
        else:
            # иначе итоговые рез = поиск по жанрам
            result = genres_search_result
        print(len(result))
        # если они оба есть, найду пересечение
        if genres_search_result != [] and query != []:
            result = list(set(genres_search_result) & set(result))
        if len(result) == 1:
            return redirect(url_for('e_result', word=result[0]))
        else:
            return render_template('e_result.html', words_list=result)
    else:
        return render_template('e_source_search.html')


@app.route('/full_list', methods=['GET', 'POST'])
def all_wrds():
    if request.method == 'POST':
        query = []
        for i in request.form:
            parameter = i
            p_value = request.form.getlist(i)
            if p_value[0] != '':
                query.append([parameter, p_value])
        #print(query)
        result = list(search_query(join_search_tables(query), join_search_conditions(query)))
        print(result)
        if len(result) == 1:
            return redirect(url_for('result', word=result[0]))  # Change 'result_<word>' to 'result'
        else:
            return render_template('result.html', words_list=result)
    else:
        return render_template('full_list.html')

@app.route('/e_full_list',  methods=['GET', 'POST'])
def e_all_wrds():
    if request.method == 'POST':
        query = []
        for i in request.form:
            parameter = i
            p_value = request.form.getlist(i)
            if p_value[0] != '':
                query.append([parameter, p_value])
        #print(query)
        result = list(search_query(join_search_tables(query), join_search_conditions(query)))
        print(result)
        if len(result) == 1:
            return redirect(url_for('e_result', word=result[0]))  # Change 'result_<word>' to 'result'
        else:
            return render_template('e_result.html', words_list=result)
    else:
        return render_template('e_full_list.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15555, debug=True)
