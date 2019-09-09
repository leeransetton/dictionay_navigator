
def navigate(dictToNavigate, path, safeNavigation=True, default=None):
    if not isinstance(dictToNavigate, dict):
        raise TypeError('dictToNavigate should be a dictionary')

    if not isinstance(path, basestring):
        raise TypeError('path should be a string')

    breadCrumbs = path.split('.')
    currentObject = dictToNavigate

    for crumb in breadCrumbs:
        if not isinstance(currentObject, dict):
            return default

        key = crumb.split('[')[0]

        if safeNavigation and key not in currentObject:
            return default
        else:
            currentObject = currentObject[key]

        if '[' in crumb:
            if not isinstance(currentObject, list):
                if safeNavigation:
                    return default
                else:
                    raise TypeError('Tried to access list when the type is {}'.format(type(currentObject).__name__))

            index = int(crumb.split('[')[1].split(']')[0])

            if safeNavigation and index >= len(currentObject):
                return default
            else:
                currentObject = currentObject[index]

    return currentObject

