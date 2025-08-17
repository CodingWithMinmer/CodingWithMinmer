class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def areSame(head1: Node, head2: Node) -> bool:
    # p1, p2 = head1, head2
    # i = j = 0
    # while p1 and p2:
    #     val1, val2 = p1.val, p2.val
    #     len1, len2 = len(val1), len(val2)

    #     while i < len1 and j < len2:
    #         if val1[i] != val2[j]:
    #             return False
    #         i += 1
    #         j += 1

    #     if i == len1:
    #         i = 0
    #         p1 = p1.next
    #     if j == len2:
    #         j = 0
    #         p2 = p2.next

    # return p1 is None and p2 is None

    p1,p2 = head1,head2
    i =j =0
    while p1 and p2:
        va1,va2 = p1.val,p2.val
        while i < len(va1) and j < len(va2):
            print(va1[i],va2[j])
            if va1[i] != va2[j]: return False
            j +=1
            i +=1
        if i == len(va1):
            p1 = p1.next
            i = 0
        
        if j == len(va2):
            p2 = p2.next
            j=0
    return not p1  and not p2


import pytest


def create_linked_list(data: list[str]) -> Node | None:
    """Helper function to create a linked list from a list of strings."""
    if not data:
        return None
    
    dummy_head = Node()
    current = dummy_head
    for val in data:
        current.next = Node(val)
        current = current.next
    return dummy_head.next

# A list of test cases where the linked lists should be considered the same.
# Each tuple contains: (list1_data, list2_data, expected_result)
true_test_cases = [
    pytest.param(["a", "bc"], ["ab", "c"], True, id="split_strings_match"),
    pytest.param(["ab", "c"], ["ab", "c"], True, id="identical_lists"),
    pytest.param(["a", "b", "c"], ["abc"], True, id="multiple_nodes_vs_single_node"),
    pytest.param(["abc"], ["a", "b", "c"], True, id="single_node_vs_multiple_nodes"),
    pytest.param([], [], True, id="both_lists_empty"),
    pytest.param(["a", "", "b"], ["ab"], True, id="list_with_empty_string_node"),
]

# A list of test cases where the linked lists should be considered different.
false_test_cases = [
    pytest.param(["a", "b"], ["a", "c"], False, id="different_content"),
    pytest.param(["ab", "d"], ["ab", "c"], False, id="different_at_end"),
    pytest.param(["a", "b"], ["ab", "c"], False, id="list2_is_longer"),
    pytest.param(["ab", "c"], ["a", "b"], False, id="list1_is_longer"),
    pytest.param(["a"], [], False, id="list2_is_empty"),
    pytest.param([], ["a"], False, id="list1_is_empty"),
    pytest.param(["apple"], ["apply"], False, id="difference_in_last_char"),
]

@pytest.mark.parametrize("list1_data, list2_data, expected", true_test_cases + false_test_cases)
def test_areSame(list1_data, list2_data, expected):
    """
    Tests the areSame function with various scenarios using parameterization.
    """
    # Arrange: Create linked lists from the input data
    head1 = create_linked_list(list1_data)
    head2 = create_linked_list(list2_data)

    # Act: Call the function to be tested
    result = areSame(head1, head2)

    # Assert: Check if the result matches the expected outcome
    assert result == expected


