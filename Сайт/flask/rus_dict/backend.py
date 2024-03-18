# -*- coding: utf-8 -*-
import sqlite3 as sqlite
import os

def names():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "Database", "Dictionary_Final.db")
    return(db_path)

connection = sqlite.connect(names(), check_same_thread=False)
cursor = connection.cursor()

def search_query(search_tables, conditions): #ищет заголовочные имена и выводит список
    sql_string = 'SELECT entry_name FROM entries ' + search_tables + conditions
    #print(sql_string)
    cursor.execute(sql_string)
    res = cursor.fetchall()

    words = []  # список всех найденных head слов
    for word in res:
        words.append(str(word[0]))
    #print(words)
    return words

def join_search_tables(params): #по параметру определяет какие таблицы нужны для поиска и составляет часть запроса
    param_dict = {
        #parameter : needed table to search
        "gloss": ["gloss"],
        "etymology": ["etymology"],
        #"etym_and_gloss_lang": ["gloss", "etymology", "language"],
        "definition": ["definition"],
        "example": ["definition", "quote_d", "quote"],
        "source": ["definition", "quote_d", "quote", "source"]
    }
    join_dict = {
        # table to search : sql text
        "gloss": 'JOIN glosses ON glosses.word_id==entries.entry_id ',
        "etymology": 'JOIN etymology ON etymology.word_id==entries.entry_id ',
        #"language": 'JOIN languages ON glosses.language==languages.lang_id ',
        "definition": 'JOIN definitions ON definitions.entry_id == entries.entry_id ',
        "quote_d": 'JOIN quote_to_definition ON quote_to_definition.definition_id == definitions.definition_id ',
        "quote": 'JOIN quotes ON quotes.quote_id == quote_to_definition.quote_id ',
        "source": 'JOIN sources ON sources.source_id == quotes.source_id '
    }
    param_list = []
    for param in params: #название param = ОбщееИмяПараметра_уточнение, смотрю на общ.имя
        if param[0].split("_")[0] in param_dict:
            param_list.extend(param_dict[param[0].split("_")[0]])
    param_list = list(set(param_list))
    search_tables = ''
    for parameter in param_list: #если параметр в списке, значит ему нужно подключить другую таблицу
        search_tables += join_dict[parameter]
    return search_tables

def join_search_conditions(conds): #conds = [[cond,[value]],[cond,[value]],[cond,[value]],[...]...]
    conditions = 'WHERE '
    texts = []
    sql_cond_text = ''
    for cond in conds: #для параметра свой запрос
        cond_value = cond[1][0]
        #(cond, cond_value)
        if cond[0] == "head":
            sql_cond_text = f'(entry_name == "{cond_value.upper()}" OR entry_name LIKE "{cond_value.upper()}\__" ESCAPE "\\") '
        if cond[0] == "form":
            sql_cond_text = f'form LIKE "%{cond_value.lower()}%" '
        if cond[0] == "mask":
            #print(cond_value, "!!!!!!!!!!")
            cond_value = cond_value.replace("*","%")
            sql_cond_text = f'entry_name LIKE "{cond_value.upper()}" '
        if cond[0] == "pos":
            sql_cond_text = f'(gram_pos LIKE "%{cond_value}%" '
            if len(cond[1]) > 1: #если значений условия больше одного
                for c in cond[1][1:]:
                    cond_value = c
                    sql_cond_text += f'OR gram_pos LIKE "%{cond_value}%" '
            sql_cond_text += ') '
        if cond[0] == "gender":
            sql_cond_text = f'(gram_gen=="{cond_value}" '
            if len(cond[1]) > 1:  # если значений условия больше одного
                for c in cond[1][1:]:
                    cond_value = c
                    sql_cond_text += f'OR gram_gen=="{cond_value}" '
            sql_cond_text += ') '
        if cond[0] == "number":
            sql_cond_text = f'(gram_number=="{cond_value}" '
            if len(cond[1]) > 1:  # если значений условия больше одного
                for c in cond[1][1:]:
                    cond_value = c
                    sql_cond_text += f'OR gram_number=="{cond_value}" '
            sql_cond_text += ') '
        if cond[0] == "degree":
            sql_cond_text = f'(gram_degree=="{cond_value}" '
            if len(cond[1]) > 1:  # если значений условия больше одного
                for c in cond[1][1:]:
                    cond_value = c
                    sql_cond_text += f'OR gram_degree=="{cond_value}" '
            sql_cond_text += ') '
        if cond[0] == "aspect":
            sql_cond_text = f'(gram_aspect=="{cond_value}" '
            if len(cond[1]) > 1:  # если значений условия больше одного
                for c in cond[1][1:]:
                    cond_value = c
                    sql_cond_text += f'OR gram_aspect=="{cond_value}" '
            sql_cond_text += ') '
        if cond[0] == "iType":
            sql_cond_text = f'(gram_itype=="{cond_value}" '
            if len(cond[1]) > 1:  # если значений условия больше одного
                for c in cond[1][1:]:
                    cond_value = c
                    sql_cond_text += f'OR gram_itype=="{cond_value}" '
            sql_cond_text += ') '
        if cond[0] == "gloss":
            sql_cond_text = f'gloss_lemma=="{cond_value}" '
        if cond[0] == "etymology":
            sql_cond_text = f'etym_lemma=="{cond_value}" '
        #if cond[0] == "etym_and_gloss_lang_language":
            #sql_cond_text = f'languages.language LIKE {cond_value} '
        if cond[0] == "definition":
            sql_cond_text = f'text_meaning LIKE "%{cond_value}%" '
        if cond[0] == "example_quote":
            sql_cond_text = f'quote LIKE "%{cond_value}%" '
        if cond[0] == "example_date_start_y":
            sql_cond_text = f'date_start_y == {cond_value} '
        if cond[0] ==  "example_date_end_y":
            sql_cond_text = f'date_end_y == {cond_value} '
        if cond[0] ==  "example_orig_date_start_y":
            sql_cond_text = f'orig_date_start_y == {cond_value} '
        if cond[0] == "example_orig_date_end_y":
            sql_cond_text = f'orig_date_start_y == {cond_value} '
        if cond[0] == "example_date_start_c":
            sql_cond_text = f'date_start_c == {cond_value} '
        if cond[0] == "example_date_end_c":
            sql_cond_text = f'date_start_c == {cond_value} '
        if cond[0] == "example_orig_date_start_c":
            sql_cond_text = f'orig_date_start_y == {cond_value} '
        if cond[0] == "example_orig_date_end_c":
            sql_cond_text = f'orig_date_start_y == {cond_value} '
        if cond[0] == "source_name":
            sql_cond_text = f'(full LIKE "%{cond_value}%" '
            if len(cond[1]) > 1:  # если значений условия больше одного
                for c in cond[1][1:]:
                    cond_value = c
                    sql_cond_text += f'OR abbr_name LIKE "%{cond_value}%" '
            sql_cond_text += ') '
        if cond[0] == "source_translate":
            sql_cond_text = f'is_translated==1 '
        if cond[0] == "source_non_translate":
            sql_cond_text = f'is_translated==0 '
        if cond[0] == "source_language":
            sql_cond_text = f'lang_id == "{cond_value}" '
        if cond[0] == "source_date_start_y":
            sql_cond_text = f'sources.date_start_y == {cond_value} '
        if cond[0] == "source_date_end_y":
            sql_cond_text = f'sources.date_start_y == {cond_value} '
        if cond[0] == "source_date_start_c":
            sql_cond_text = f'sources.date_start_y == {cond_value} '
        if cond[0] == "source_date_end_c":
            sql_cond_text = f'sources.date_start_y == {cond_value} '
        if cond[0] == "source_publication_date_start":
            sql_cond_text = f'publication_date_y == {cond_value} '
        if cond[0] == "source_publication_date_end":
            sql_cond_text = f'publication_date_c == {cond_value} '

        texts.append(sql_cond_text)
    sql_where_text = ("AND ".join(texts))
    conditions += sql_where_text
    return(conditions)

def load_page(word):
    #нахожу full_text для интересующего слова по известному head слову
    sql_string = f'SELECT entry_name, is_variant, variant_to_entry, id_entry_to_see, full_text FROM entries WHERE entry_name == "{word}" OR entry_name LIKE "{word}\__" ESCAPE "\\"'
    cursor.execute(sql_string)
    res = cursor.fetchall()
    #print(res)
    text_to_see = []
    #[entry_name, is_variant =0|1, variant_to_entry, id_entry_to_see, full_text]
    for index_1 in range(len(res)):
        if res[index_1][1] == 1:
            sql_string_extra = f'SELECT id_entry_to_see, full_text FROM entries WHERE entry_id == {res[index_1][2]}'
            cursor.execute(sql_string_extra)
            res_extra = cursor.fetchall()
            for index_2 in range(len(res_extra)):
                text_to_see.append(res_extra[index_2][1])
        else:
            text_to_see.append(res[index_1][4])
    if len(text_to_see) != 0:
        text_to_see = text_to_see[0].split("\n")
    return text_to_see

#отдельные поисковые запросы для тех условий, которые нельзя объединить
def resource_genre(param): #param = [cond, value] = ["source_genre", genre1, genre2, ...]
    get_id_select = 'SELECT type_id FROM sources_types '
    #get_id_join = join_search_tables(param[0])
    cond_value = param[1][0]
    get_id_where = f'WHERE (type == "{cond_value}" '
    if len(param[1]) > 1:
        for extra_value in param[1][1:]:
            #print(extra_value)
            cond_value = extra_value
            get_id_where += f'OR type == "{cond_value}"  '
    get_id_where += ')'
    #sql_get_id = get_id_select + get_id_join + get_id_where
    sql_get_id = get_id_select + get_id_where
    #print(sql_get_id)
    cursor.execute(sql_get_id)
    res_id = cursor.fetchall()
    list_of_id = []
    for id in res_id:
        list_of_id.append(id[0])
    #print(list_of_id)


    sql_get_head_word = f'''SELECT entry_name FROM entries 
JOIN definitions ON definitions.entry_id == entries.entry_id
JOIN quote_to_definition ON definitions.definition_id==quote_to_definition.definition_id
JOIN quotes ON quote_to_definition.quote_id==quotes.quote_id
JOIN sources ON sources.source_id == quotes.source_id
WHERE type_id == "{list_of_id}"
'''
    cursor.execute(sql_get_head_word)
    result = cursor.fetchall()
    res_words = []
    for word in result:
        res_words.append(word[0])
    res_words = list(res_words)
    return res_words

#n = int(input())
#if n == 1:
#    print(join_search_conditions([['head', ['отец']], ['pos', ['NOUN', 'ADJ', 'VERB']], ['number', ['pl']], ['iType', ['нескл.', 'неизм.']]]))
