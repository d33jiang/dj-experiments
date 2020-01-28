import dataclasses
import heapq
import typing
from collections import defaultdict

Symbol = typing.Any
Frequency = typing.Union[int, float]
EncodingTable = typing.Mapping[Symbol, str]


@dataclasses.dataclass
class TreeNode:
    frequency: Frequency
    symbol: Symbol = None
    left: 'TreeNode' = None
    right: 'TreeNode' = None

    def __lt__(self, other: 'TreeNode'):
        return self.frequency < other.frequency

    def __repr__(self):
        if self.symbol:
            return repr(self.symbol)
        else:
            return f'({self.left} {self.right})'


def get_counts(data_string: typing.Iterable[Symbol]) -> typing.Mapping[Symbol, int]:
    counts = defaultdict(int)

    for symbol in data_string:
        counts[symbol] += 1

    return counts


def construct_tree(frequencies: typing.Mapping[Symbol, Frequency]) -> typing.Optional[TreeNode]:
    nodes = [
        TreeNode(frequency=frequency, symbol=symbol)
        for symbol, frequency in frequencies.items()
    ]
    heapq.heapify(nodes)

    if len(nodes) == 0:
        return None

    if len(nodes) == 1:
        node = nodes[0]
        return TreeNode(
            frequency=node.frequency,
            left=node
        )

    while len(nodes) > 1:
        a = heapq.heappop(nodes)  # type: TreeNode
        b = heapq.heappop(nodes)  # type: TreeNode
        heapq.heappush(
            nodes,
            TreeNode(
                frequency=a.frequency + b.frequency,
                left=a,
                right=b
            )
        )

    return nodes[0]


def construct_encoding_table(root_node: TreeNode) -> EncodingTable:
    encoding_table = {}

    def process_node(node: TreeNode, codeword: str = ''):
        if node.symbol:
            encoding_table[node.symbol] = codeword
        else:
            process_node(node.left, codeword + '0')
            process_node(node.right, codeword + '1')

    process_node(root_node, '')

    return encoding_table


def encode(data: typing.Iterable[Symbol], encoding_table: EncodingTable) -> str:
    result = []

    for symbol in data:
        result.append(encoding_table[symbol])

    return ''.join(result)


def decode(data: str, root_node: TreeNode) -> typing.List[Symbol]:
    if root_node.symbol:
        raise ValueError

    next_index = 0
    node = root_node

    result = []

    while next_index < len(data):
        if data[next_index] == '0':
            node = node.left
        else:
            node = node.right

        next_index += 1

        if node.symbol:
            result.append(node.symbol)
            node = root_node

    return result


#
#

test_string = 'Today, I grew a little taller, a little wiser, and a little more resilient.'

print(test_string)

_counts = get_counts(test_string)
print(_counts)

_tree = construct_tree(_counts)
print(_tree)

_encoding_table = construct_encoding_table(_tree)
print(_encoding_table)

_encoded_string = encode(test_string, _encoding_table)
print(_encoded_string)

_decoded_string = decode(_encoded_string, _tree)
print(''.join(_decoded_string))

print(8 * len(test_string))
print(len(_encoded_string))

print()

#
#

test_string = test_string.split(' ')

print(test_string)

_counts = get_counts(test_string)
print(_counts)

_tree = construct_tree(_counts)
print(_tree)

_encoding_table = construct_encoding_table(_tree)
print(_encoding_table)

_encoded_string = encode(test_string, _encoding_table)
print(_encoded_string)

_decoded_string = decode(_encoded_string, _tree)
print(' '.join(_decoded_string))

print(f'{len(test_string)} words')
print(len(_encoded_string))

print()

#
#

with open('resources/lorem_ipsum.txt') as f:
    test_string = f.read()

_counts = get_counts(test_string)
print(_counts)

_tree = construct_tree(_counts)
print(_tree)

_encoding_table = construct_encoding_table(_tree)
print(_encoding_table)

_encoded_string = encode(test_string, _encoding_table)
print(_encoded_string)

_decoded_string = decode(_encoded_string, _tree)
print(''.join(_decoded_string))

print(8 * len(test_string))
print(len(_encoded_string))
