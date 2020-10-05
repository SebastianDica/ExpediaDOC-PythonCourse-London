# Python Dictionaries

## About

* https://www.w3schools.com/python/python_dictionaries.asp
* A dictionary is a collection which is unordered, changeable and indexed
* In Python dictionaries are written with curly brackets, and they have keys and values

## Properties

* A dictionary is a **collection** which is unordered, changeable and indexed. The following represents a collection of properties.

```python
{
  "name": "John",
  "age": 36,
  "location": "London"
}
```

* A dictionary is a collection which is **unordered**, changeable and indexed. The following two dictionaries, are comparatively, the same.

```python
{
  "name": "John",
  "age": 36,
  "location": "London"
}
```
```python
{
  "location": "London",
  "age": 36,
  "name": "John"
}
```
* A dictionary is a collection which is unordered, **changeable** and indexed. The second dictionary is a modification of the first dictionary.

```python
{
  "name": "John",
  "age": 36,
  "location": "London"
}
```
```python
{
  "name": "John",
  "age": 36,
  "location": "Edinburgh"
}
```

* A dictionary is a collection which is unordered, changeable and **indexed**. The properties of the dictionary can be accessed using a key.

```python
x = {
  "name": "John",
  "age": 36,
  "location": "London"
}
x['name'] # This will reference the String John
```