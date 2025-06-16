"""
https://stepik.org/lesson/13239/step/6?unit=3425
"""
from typing import Dict


def read_encoding(chars_cnt: int) -> Dict[str, str]:
    codes = {}
    for _ in range(chars_cnt):
        ch, code = input().split(': ')
        codes[code] = ch
    return codes


def decode_encoded_sequence(codes: Dict[str, str], encoded_sequence: str) -> str:
    bits = ""
    decoded_string = ""
    for b in encoded_sequence:
        bits += b
        if bits in codes:
            decoded_string += codes[bits]
            bits = ""
    return decoded_string


if __name__ == "__main__":
    k, l = map(int, input().split())
    codes = read_encoding(k)
    encoded_sequence = input()
    decoded_string = decode_encoded_sequence(codes, encoded_sequence)
    print(decoded_string)
