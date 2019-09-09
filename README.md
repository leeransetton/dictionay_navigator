# Python Dictionary Navigator

## Quick Start
To install, use pip:

`pip install -U dictionay_navigator`

## Usage
```
>>> from dictionary_navigator import navigator
>>> myDict = {
        'person': {
            'name': {
                'first': 'Michael',
                'las': 'Scott'
            },
            'height': 175.3,
            'friendsNames': ['Jim', 'Ryan', 'Todd', 'Stanley', 'Darryl'],
            'enemies': ['Toby']
        }
    }

>>> navigator.navigate(myDict, 'person.name.first')
'Michael'

>>> navigator.navigate(myDict, 'person.friendsNames')
['Jim', 'Ryan', 'Todd', 'Stanley', 'Darryl']

>>> navigator.navigate(myDict, 'person.friendsNames[2]')
'Todd'

>>> navigator.navigate(myDict, 'person.friendsNames[10]')

>>> navigator.navigate(myDict, 'person.friendsNames[10]', default='Dwight')
'Dwight'

>>> navigator.navigate(myDict, 'person.friendsNames[10]', safeNavigation=False)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "testProject/.pyenv/local/lib/python2.7/site-packages/dictionary_navigator/navigator.py", line 35, in navigate
    currentObject = currentObject[index]
IndexError: list index out of range
```


