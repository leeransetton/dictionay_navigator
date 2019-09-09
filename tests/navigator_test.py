import pytest
from dictionary_navigator import navigator

@pytest.mark.parametrize('subTestName, path, safeNavigation, default, expectedResult, shouldRaiseException',
                         [
                             ('firstLevel_number_safe', 'a', True, None, 1, False),
                             ('firstLevel_bool_safe', 'b', True, None, True, False),
                             ('firstLevel_list_safe', 'c', True, None, [1,2,3], False),
                             ('firstLevel_list_item_safe', 'c[0]', True, None, 1, False),
                             ('firstLevel_list_itemOutOfRange_safe', 'c[4]', True, None, None, False),
                             ('firstLevel_list_itemOutOfRange_unsafe', 'c[4]', False, None, None, True),
                             ('firstLevel_emptyList_safe', 'd', True, None, [], False),
                             ('firstLevel_emptyList_itemOutOfRange_safe', 'd[0]', True, None, None, False),
                             ('firstLevel_emptyList_itemOutOfRange_unsafe', 'd[0]', False, None, None, True),
                             ('firstLevel_emptyDict_safe', 'e', True, None, {}, False),
                             ('firstLevel_emptyDict_item_safe', 'e.ea', True, None, None, False),
                             ('firstLevel_emptyDict_item_unsafe', 'e.ea', True, None, None, True),
                             ('firstLevel_Dict_safe', 'f', True, None, {'fa': 1, 'fb': False, 'fc': [1,2,3], 'fd': [], 'fe': {}, 'ff': {'ffa': 1}}, True),
                             ('secondLevel_number_safe', 'f.fa', True, None, 1, False),
                             ('secondLevel_bool_safe', 'f.fb', True, None, False, False),
                             ('secondLevel_list_safe', 'f.fc', True, None, [4,5,6], False),
                             ('secondLevel_list_item_safe', 'f.fc[0]', True, None, 4, False),
                             ('secondLevel_list_itemOutOfRange_safe', 'f.fc[4]', True, None, None, False),
                             ('secondLevel_list_itemOutOfRange_unsafe', 'f.fc[4]', False, None, None, True),
                             ('secondLevel_emptyList_safe', 'f.fd', True, None, [], False),
                             ('secondLevel_emptyList_itemOutOfRange_safe', 'f.fd[0]', True, None, None, False),
                             ('secondLevel_emptyList_itemOutOfRange_unsafe', 'f.fd[0]', False, None, None, True),
                             ('secondLevel_emptyDict_safe', 'f.fe', True, None, {}, False),
                             ('secondLevel_emptyDict_item_safe', 'f.fe.ea', True, None, None, False),
                             ('secondLevel_emptyDict_item_unsafe', 'f.fe.ea', True, None, None, True),
                             ('secondLevel_Dict_safe', 'f.ff', True, None, {'ffa': 1}, False),
                             ('thirdLevel_Dict_safe', 'f.ff.ffa', True, None, 1, False),
                             ('nonExistingPath_safe', 'q', True, None, None, False),
                             ('nonExistingPath_safe_defaultIsADict', 'q', True, {'someKey': 'someValue'}, {'someKey': 'someValue'}, False),
                             ('nonExistingPath_unsafe', 'q', False, None, None, True),
                         ])
def test_navigator(subTestName, path, safeNavigation, default, expectedResult, shouldRaiseException):
    obj = {
        'a': 1,
        'b': True,
        'c': [1,2,3],
        'd': [],
        'e': {},
        'f': {
            'fa': 1,
            'fb': False,
            'fc': [4,5,6],
            'fd': [],
            'fe': {},
            'ff': {
                'ffa': 1
            }
        }
    }

    try:
        value = navigator.navigate(obj, path, safeNavigation, default)
        assert shouldRaiseException == False, '{} - {}'.format(subTestName, 'an exception was expected')
        assert expectedResult == value, '{} - {}'.format(subTestName, 'received value not as expected')
    except Exception as ex:
        assert shouldRaiseException == True, '{} - {} - {}'.format(subTestName, 'an exception was unexpected', ex.message)