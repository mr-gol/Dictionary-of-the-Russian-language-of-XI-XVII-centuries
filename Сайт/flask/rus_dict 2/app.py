# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, request, render_template, session
from flask_babel import Babel
from backend import join_search_tables, join_search_conditions, join_search_conditions2,search_query, load_page, resource_genre
from math import ceil
import sqlite3 as sqlite
import os

def get_locale():
    return session.get('lang', request.accept_languages.best_match(['ru', 'en']))

app = Flask(__name__)
app.secret_key = 'rus_dict_olesar2'
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
babel = Babel(app, locale_selector=get_locale)

@app.context_processor
def inject_get_locale():
    return dict(get_locale=get_locale)

def names():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Database","Dictionary_Final.db")
    return db_path

connection = sqlite.connect(names(), check_same_thread=False)
cursor = connection.cursor()

@app.route('/')
def hi():
    return redirect(url_for('main'))

@app.route('/toggle_language')
def toggle_language():
    if session.get('lang', 'ru') == 'ru':
        session['lang'] = 'en'
    else:
        session['lang'] = 'ru'
    return redirect(url_for('main'))

@app.route('/main_page')
def main():
    return render_template('main_page.html')

@app.errorhandler(Exception)
def not_found_error(error):
    print(error)
    return render_template('error.html')

@app.route('/search1', methods=['GET', 'POST'])
def search_wrd():
    page_size = 80
    page_num = int(request.args.get('page', 1))  # Get the page number from the GET request
    if request.method == 'GET' and not request.args.get('page'):
        session.pop('query_search_wrd', None)  # Remove the query from the session
        return render_template('search1.html')
    else:
        if 'query_search_wrd' in session and page_num != 1:
            query = session['query_search_wrd'] # Get the query from the session
        else: # request.method == 'POST':
            query = []
            for i in request.form:
                parameter = i
                p_value = request.form.getlist(i)
                if p_value[0] != '':
                    query.append([parameter, p_value])
            session['query_search_wrd'] = query
        result_word_list = list(search_query(join_search_tables(query), join_search_conditions(query)))
        word_list_length = len(result_word_list)
        if word_list_length == 1:
            return redirect(url_for('result', word=result_word_list[0]))
        else:
            # Calculate the range of items for the current page
            start = (page_num - 1) * page_size
            end = start + page_size
            # Slice the result list to only include items for the current page
            page_items = result_word_list[start:end]
            # Calculate the total number of pages
            total_pages = ceil(word_list_length / page_size) if word_list_length > 1 else 0
            return render_template('result.html', words_list=page_items, total_pages=total_pages, current_page=page_num, total_words=word_list_length)

@app.route('/result/<word>', methods=['GET'])  # Change '/result_<word>' to '/result/<word>'
def result(word):
    print(word)
    text = load_page(word.upper())
    if not text:
        return render_template('result.html', words_list=word)
    return render_template('word_entry.html', word=text)

@app.route('/result_list', methods=['GET'])
def result_list(words_list):
    return render_template('result.html', words_list=words_list)

@app.route('/source_search', methods=['GET', 'POST'])
def search_txt():
    page_size = 80
    page_num = int(request.args.get('page', 1))  # Get the page number from the GET request
    if request.method == 'GET' and not request.args.get('page'):
        session.pop('query_search_txt', None)  # Remove the query from the session
        session.pop('genres_search_result', None) # Remove the genres search from the session
        return render_template('source_search.html')
    else:
        if 'query_search_txt' in session and page_num != 1:
            query = session['query_search_txt']  # Get the query from the session
            genres_search_result = session['genres_search_result'] # Get the genres search from the session
        else: # request.method == 'POST':
            query = []
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
                    #break
                #except sqlite3.OperationalError:
                #except Exception:
                    #return render_template('error.html')
            session['query_search_txt'] = query
            session['genres_search_result'] = genres_search_result
            print(f"query: {query}")
            print(f"query: {genres_search_result}")
        # если есть еще условия кроме жанра
        if query:
            print("query if")
            query_result = search_query(join_search_tables(query), join_search_conditions(query))
            #print(query_result)
            result_word_list = list(query_result)
        else:
            # иначе итоговые рез = поиск по жанрам
            result_word_list = genres_search_result
        # если они оба есть, найду пересечение
        if genres_search_result != [] and query != []:
            result_word_list = list(genres_search_result & result_word_list)
        word_list_length = len(result_word_list)
        if word_list_length == 1:
            return redirect(url_for('result', word=result_word_list[0]))
        else:
            # Calculate the range of items for the current page
            start = (page_num - 1) * page_size
            end = start + page_size
            # Slice the result list to only include items for the current page
            page_items = result_word_list[start:end]
            # Calculate the total number of pages
            total_pages = ceil(word_list_length / page_size) if word_list_length > 1 else 0
            print(f"render template, page_num:{page_num}, page_items:{page_items}")
            return render_template('result.html', words_list=page_items, total_pages=total_pages, current_page=page_num, total_words=word_list_length)

@app.route('/full_list', methods=['GET', 'POST'])
def all_wrds():
    page_size = 80
    page_num = int(request.args.get('page', 1))  # Get the page number from the GET request
    if request.method == 'GET' and not request.args.get('page'):
        session.pop('query_all_wrds', None) # Remove the query from the session
        return render_template('full_list.html')
    else:
        if 'query_all_wrds' in session and page_num != 1:
            query = session['query_all_wrds']  # Get the query from the session
        else: # request.method == 'POST':
            #print(session['query_all_wrds'])
            query = []
            print(request.form)
            for i in request.form:
                parameter = i
                p_value = request.form.getlist(i)
                if p_value[0] != '':
                    query.append([parameter, p_value])
            session['query_all_wrds'] = query  # Store the query in the session, result to big?
        result_word_list = list(search_query(join_search_tables(query), join_search_conditions2(query)))
        word_list_length = len(result_word_list)
    if word_list_length == 1:
        return redirect(url_for('result', word=result_word_list[0]))
    else:
        # Calculate the range of items for the current page
        start = (page_num - 1) * page_size
        end = start + page_size
        # Slice the result list to only include items for the current page
        page_items = result_word_list[start:end]
        # Calculate the total number of pages
        total_pages = ceil(word_list_length / page_size) if word_list_length > 1 else 0
        return render_template('result.html', words_list=page_items, total_pages=total_pages, current_page=page_num, total_words=word_list_length)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15555, debug=True)
