# ContactSearch

ContactSearch is a tool for searching a JSON file of you network contacts.

### Tech

ContactSearch uses some open source projects to work properly:

* [Flask](http://flask.pocoo.org/) - (v0.12.2) Lightweight Python framework for web apps
* [Materialize CSS](http://materializecss.com/) - responsive front-end framework based on Material Design
* [DataTables](https://datatables.net/) for creating searchable, responsive HTML tables.
* [jQuery](https://jquery.com/) - for many reasons..

### Installation

ContachSearch requires Python 3.6 or above to run.

Install the dependencies and start the server.

```sh
$ git clone https://github.com/Georgerowberry/ContactSearch.git
$ cd ContactSearch
$ pip3 install -r requirements.txt
$ export FLASK_APP=ContactSearch.py
$ flask run
```
The server will be running on http://127.0.0.1:5000/ by defult

### Future Development

* Use a Database to store contacts, as already in JSON format could use no-SQL DB easily e.g MongoDB
* Use Pandas for faster data processing
* Use a RESTfull API for queries and just make calls for the data when needed.
    
### Author
George Rowberry



