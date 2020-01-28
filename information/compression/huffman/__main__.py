from compression.huffman import construct_encoding_table, construct_tree, decode, encode, get_counts

#
#

test_string = 'Today, I grew a little taller, a little wiser, and a little more resilient.'

print(f'Original: {test_string}')

_counts = get_counts(test_string)
print(f'  Counts: {_counts}')

_tree = construct_tree(_counts)
print(f'    Tree: {_tree}')

_encoding_table = construct_encoding_table(_tree)
print(f'Encoding: {_encoding_table}')

_encoded_string = encode(test_string, _encoding_table)
print(f' Encoded: {_encoded_string}')

_decoded_string = decode(_encoded_string, _tree)
print(' Decoded: ' + ''.join(_decoded_string))

print(f'Original: {len(test_string)} characters')
print(f' Encoded: {len(_encoded_string)} bits')

print()

#
#

test_string = test_string.split(' ')

print(f'Original: {test_string}')

_counts = get_counts(test_string)
print(f'  Counts: {_counts}')

_tree = construct_tree(_counts)
print(f'    Tree: {_tree}')

_encoding_table = construct_encoding_table(_tree)
print(f'Encoding: {_encoding_table}')

_encoded_string = encode(test_string, _encoding_table)
print(f' Encoded: {_encoded_string}')

_decoded_string = decode(_encoded_string, _tree)
print(' Decoded: ' + ' '.join(_decoded_string))

print(f'Original: {len(test_string)} words')
print(f' Encoded: {len(_encoded_string)} bits')

print()

#
#

with open('resources/lorem_ipsum.txt') as f:
    test_string = f.read()

print('Original: <lorem_ipsum.txt>')

_counts = get_counts(test_string)
print(f'  Counts: {_counts}')

_tree = construct_tree(_counts)
print(f'    Tree: {_tree}')

_encoding_table = construct_encoding_table(_tree)
print(f'Encoding: {_encoding_table}')

_encoded_string = encode(test_string, _encoding_table)
print(f' Encoded: {_encoded_string}')

# _decoded_string = decode(_encoded_string, _tree)
# print(' Decoded: ' + ''.join(_decoded_string))

print(f'Original: {len(test_string)} characters')
print(f' Encoded: {len(_encoded_string)} bits')
