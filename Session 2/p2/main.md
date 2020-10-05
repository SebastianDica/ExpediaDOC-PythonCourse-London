# Python Dictionaries

## Extensibility

* The properties accessed via the keys in the dictionary, do not have to be strings or numbers. These can be **arrays**.

```python
{
  "name": "John",
  "age": 36,
  "location": "London",
  "children": [ "Megan", "Tom" ]
}
```

* The properties accessed via the keys in the dictionary, do not have to be strings or numbers. These can other **dictionaries**.

```python
{
  "name": "John",
  "age": 36,
  "location": "London",
  "work": {
    "title": "Software Developer Engineer",
    "company": "Expedia Group"
  }
}
```

* The properties accessed via the keys in the dictionary, do not have to be strings or numbers. These can an **array of dictionaries**.

```python
{
  "name": "John",
  "age": 36,
  "location": "London",
  "children": [
    {
      "name": "Tom",
      "age": 14
    },
    {
      "name": "Megan",
      "age": 16
    }
  ]
}
```
