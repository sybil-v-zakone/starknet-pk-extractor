import hashlib

from eth_account.hdaccount import (
    key_from_seed
)
from starknet_py.hash.address import compute_address
from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.signer.stark_curve_signer import KeyPair

import config
import constants


def grind_key(key_seed):
    key_value_limit = constants.GRIND_KEY_VALUE_LIMIT
    if not key_value_limit:
        return key_seed

    max_allowed_val = constants.GRIND_KEY_MAX_ALLOWED_VALUE

    i = 0
    key = None
    while True:
        key = hash_key_with_index(key_seed, i)
        i += 1

        if key < max_allowed_val:
            break

    return format(int(key, 16) % int(key_value_limit, 16), 'x')


def hash_key_with_index(key, index):
    key = bytes.fromhex(key[2:])

    x = key + bytes([index])
    key_hash = hashlib.sha256(x).hexdigest()
    return key_hash


def get_stark_pair(private_key):
    hdnode_private_key = key_from_seed(bytes.fromhex(private_key[2:]), constants.BASE_DERIVATION_PATH)
    hdnode_private_key_hash = "0x" + hdnode_private_key.hex()
    ground_key = grind_key(hdnode_private_key_hash)

    stark_pair = KeyPair.from_private_key(int(ground_key, 16))
    return stark_pair


def build_constructor_calldata(public_key, cairo_version: str=config.CAIRO_VERSION):
    if cairo_version == 'cairo0':
        return [
            int(constants.cairo0_argent_hashes['ACCOUNT_CLASS_HASH']),
            get_selector_from_name('initialize'),
            2,
            int(public_key, 16),
            0
        ]
    if cairo_version == 'cairo1':
        return [
            int(public_key, 16),
            0
        ]


def calculate_argent_address(public_key, constructor_call_data, cairo_version: str=config.CAIRO_VERSION):
    class_hash = constants.cairo0_argent_hashes['PROXY_CLASS_HASH'] if cairo_version == 'cairo0'\
        else constants.cairo1_argent_hashes['ACCOUNT_CLASS_HASH']

    return compute_address(
        class_hash=int(class_hash),
        constructor_calldata=constructor_call_data,
        salt=int(public_key, 16),
        deployer_address=0
    )
