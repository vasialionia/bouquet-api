Bouquet
=======

A simple application for storing compliments.

API
---

#### GET /compliment
Returns an array of all the compliments stored. (See GET /compliment/:id response format.)

#### GET /compliment/:id
Return the compliment with id provided. Response format:
```
{
    'lang': 'en',
    'sex': 'male',
    'text': 'You are the best!'
}
```

#### POST /compliment
Creates a compliment. Params:
```
lang - 'en', 'ru', etc.
sex - 'male', 'female', etc.
text - 'You are the best!', etc.
```

#### DELETE /compliment/:id
Delete the compliment with id provided.

#### PUT /compliment/:id
Updates the compliment with id provided. (See POST /compliment params.)

Installation
--------------

```sh
git clone https://github.com/vasialionia/bouquet-api.git bouquet-api
cd bouquet-api
python
```
```python
from app import db
db.create_all()
exit()
```
```sh
python app.py
```
