# Debug Log – Task 1

## Error 1

**Error Message:**  
`AttributeError: 'VideoGame' object has no attribute 'validate_time_spent'`

**What It Means:**  
`set_time_spent` called `self.validate_time_spent(...)`, but the actual method name is `_validate_time_spent` (with a leading underscore). 

**How I Fixed It:**  
Corrected the call in `set_time_spent` from `self.validate_time_spent(time_spent)` to `self._validate_time_spent(time_spent)` in `src/structs/VideoGame.py`.

**Resource Used:**  
VScode 

---

## Error 2

**Error Message:**  
No runtime error

**What It Means:**  
`_tags = []` was declared as a class-level variable in `VideoGame`, meaning all instances shared the same list. Adding tags to one game would unexpectedly affect every other game object.

**How I Fixed It:**  
Removed `_tags = []` from the class body and moved it into `__init__` as `self._tags = []`, so each instance gets its own separate list.

**Resource Used:**  
Code review — [Python docs on class vs instance variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)

---

## Error 3

**Error Message:**  

**What It Means:**  

**How I Fixed It:**  

**Resource Used:**  

## Error 4

**Error Message:**  

**What It Means:**  

**How I Fixed It:**  

**Resource Used:**  

## Error 5

**Error Message:**  

**What It Means:**  

**How I Fixed It:**  

**Resource Used:**