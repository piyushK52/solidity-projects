import json
from solcx import compile_standard, install_solc  # python library for compiling solidity

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


# compiling (this basically generates an ABI)
install_solc("0.6.0")
compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        }
    },
    solc_version="0.6.0"
)

# writing the compiled code/ABI as a json file
with open("compiled_code.json", "w") as file:
    json.dump(compile_sol, file)
