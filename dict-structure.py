# This file contains the skeleton of the dictionary
# You can use this skeleton to store the extracted values
# for each of the key's, there should be space for each of
# the key's that can be extracted from the provided pdf files


# This is a work in progress
# Currently tested for list of headers and list of key-value dicts
# that correspond by order in the respective lists
# Todo: find way to build an extra level on the tree
# Todo: (alternate route) find a way to directly assign existing and new keys (and values) to a nested dict


def create_skeleton_dict(headers: list, keyvals: list):
    """Makes nested dict based on list and dict or list
    *currently only supports one level down of nesting*

    Parameters: a list of headers and a list of dicts where
    the lists are of equal length (the length of the dicts
    can vary without causing issue).

    Returns: a nested dictionary where respective 'keyvals' are
    nested in respective 'headers' based on order in the list
    and dictionary provided as parameters
    """
    skeleton_dict = dict(zip(headers, keyvals))
    return skeleton_dict


if __name__ == "__main__":
    import json
    header_list = ["header1", "header2", "header3"]
    keyval_list = [{"key1.1": "val1.1", "key1.2": "val1.2", "key1.3": "val1.3"},
                   {"key2.1": "val2.1", "key2.2": "val2.2", "key2.3": "val2.3"},
                   {"key3.1": "val3.1", "key3.2": "val3.2", "key3.3": "val3.3"}]
    print(create_skeleton_dict(header_list, keyval_list))
    print(type(create_skeleton_dict(header_list, keyval_list)))
    print(json.dumps(create_skeleton_dict(header_list, keyval_list), indent=2))
    print(type(json.dumps(create_skeleton_dict(header_list, keyval_list))))
