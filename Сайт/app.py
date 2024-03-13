from flask import Flask, redirect, url_for, escape, request, render_template
from backend import join_search_tables, join_search_conditions, search_query, load_page, resource_genre
import sqlite3 as sqlite
import os

app = Flask(__name__)

def names():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Dictionary_Final.db")
    return(db_path)

connection = sqlite.connect(names(), check_same_thread=False)
cursor = connection.cursor()

@app.route('/')
def hi():
    return redirect(url_for('main'))

@app.route('/main_page')
def main():
    return render_template('main_page.html')

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
        result = list(set(search_query(join_search_tables(query), join_search_conditions(query))))
        print(result)
        if len(result) == 1:
            return redirect(url_for('result_<word>', word=result))
        else:
            return render_template('result.html', words_list=result)
    else:
        return render_template('search1.html')

@app.route('/result_<word>', methods=['GET'])
def result(word):
    print(word)
    text = load_page(word.upper())
    if text == []:
        return render_template('result.html', words_list=text)
    return render_template('word_entry.html', word=text)

@app.route('/result_list', methods=['GET'])
def result_list(words_list):
    return render_template('result.html', words_list=words_list)

@app.route('/source_search', methods=['GET', 'POST'])
def search_txt():
    if request.method == 'POST':
        result = []
        query = []
        genres_search_result = []
        for i in request.form:
            parameter = i
            p_value = request.form.getlist(i)
            #ищем отдельно по жанрам
            if parameter == "source_genre" and p_value[0] != '':
                genres_search_result = resource_genre([parameter, p_value])
                print(genres_search_result)
                pass
            else:
                if p_value[0] != '':
                    query.append([parameter, p_value])
        print(query)
        #если есть еще условия кроме нажра
        if query != []:
            result = list(set(search_query(join_search_tables(query), join_search_conditions(query))))
            print(result)
        else:
            #иначе итоговые рез = поиск по жанрам
            result = genres_search_result
        #если они оба есть, найду пересечение
        if genres_search_result != [] and query != []:
            result = list(set(genres_search_result) & set(result))
        if len(result) == 1:
            return redirect(url_for('result_<word>', word=result))
        else:
            return render_template('result.html', words_list=result)
    else:
        return render_template('source_search.html')

@app.route('/full_list')
def all_wrds():
    return render_template('full_list.html')

if __name__ == '__main__':
    app.run(debug=True)
