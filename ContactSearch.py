# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import json
import os

project_dir = os.path.dirname(os.path.realpath(__file__))
file_path = project_dir + "/data.json"

app = Flask(__name__)


def get_data():
    with open(file_path, 'r') as file:
        data = json.load(file)
    data = sorted(data, key=lambda x: x['name'])
    return data


def search_data(data, search_term):
    """
    :param data: list of dicts of contacts
    :param search_term: string to search for
    :return: dict of contacts matching search term
    """
    matches = []

    def find_match(value):
        if search_term.lower() in value.lower() or search_term.lower() == value.lower():
            if d not in matches:
                matches.append(d)

    for d in data:
        for k, v in d.items():
            if isinstance(v, list):
                for i in v:
                    find_match(i)
            else:
                find_match(v)

    return matches


@app.route('/')
def start():
    search = request.args.get('search')
    data = get_data()
    if search:
        print(search)
        matching_contacts = search_data(data, search)
        context = {'results': True, 'matches': matching_contacts, 'search_term': search}
        return render_template('results.html', data=context)
    elif search == '':
        context = {'results': True, 'matches': data, 'search_term': search}
        return render_template('results.html', data=context)
    else:
        return render_template('search.html', data=data)


if __name__ == '__main__':
    app.run()
