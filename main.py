from web3 import Web3
from key_derivation import get_stark_pair, build_constructor_calldata, calculate_argent_address
from config import SEED_PHRASES_TXT_PATH, PRIVATE_KEYS_TXT_PATH, ADDRESSES_TXT_PATH
from utils import read_from_txt, write_to_txt


def run():
    w3 = Web3()
    w3.eth.account.enable_unaudited_hdwallet_features()

    seed_phrases = read_from_txt(SEED_PHRASES_TXT_PATH)
    private_keys_result = []
    addresses_result = []

    for seed_phrase in seed_phrases:
        account = w3.eth.account.from_mnemonic(seed_phrase)
        stark_pair = get_stark_pair(account.key.hex())

        public_key = hex(stark_pair.public_key)
        private_key = hex(stark_pair.private_key)

        constructor_call_data = build_constructor_calldata(public_key)
        address = calculate_argent_address(public_key, constructor_call_data)

        private_keys_result.append(private_key)
        addresses_result.append(hex(address))

    write_to_txt(PRIVATE_KEYS_TXT_PATH, private_keys_result)
    write_to_txt(ADDRESSES_TXT_PATH, addresses_result)


run()
