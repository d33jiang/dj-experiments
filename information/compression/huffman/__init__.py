import dataclasses
import heapq
from collections import defaultdict

import typing

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
