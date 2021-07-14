# Collaborative Filtering package

Some description

## Running

```bash
python -m cf --user-id 4
python -m cf --user-id 4 --train --items-filename u.item --ranks-filename u.base
python -m cf --user-id 4 --test
```

## Tests

```python
pytest \
  --cov-report html \
  --cov-report term \
  --cov=cf tests
```
