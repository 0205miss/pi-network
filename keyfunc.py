import struct
import hashlib
import hmac


# BIP-0044 path format for Stellar keypair derivation, as specified in
# https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0005.md
ACCOUNT_PATH_FORMAT = "m/44'/314159'/0'"


# the index of the first hardened key, per BIP-0032 and SLIP-0010
HARDENED = 0x80000000

# as defined in https://github.com/satoshilabs/slips/blob/master/slip-0010.md
CURVE = b'ed25519 seed'


hmac_sha_512 = lambda key, data: hmac.new(key, data, hashlib.sha512).digest()


def key(v):
    """Return the private key part (the left half) of a 64-byte sequence v."""
    return v[:32]


def chain_code(v):
    """Return the chain code part (the right half) of a 64-byte sequence v."""
    return v[32:]


def ser32(i):
    """Serialize a 32-bit unsigned integer i as a 4-byte sequence.
       The most significant byte of i appears first in the serialization.
    """
    return struct.pack('>L', i)
    

def new_master_key(seed):
    """Return the extended master key derived from a 64-byte binary seed.
    
    BIP-0032 defines an extended key as a pair (private_key, chain_code).
    The extended master key is the pair (master_private_key, master_chain_code)
    specified by SLIP-0010.
    """
    h = hmac_sha_512(CURVE, seed);
    return (key(h), chain_code(h))


def derive(parent_key, parent_chain_code, i):
    """Return the i-th extended child key from an extended parent key."""
    assert len(parent_key) == 32
    assert len(parent_chain_code) == 32    
    assert i >= HARDENED, 'no public derivation for ed25519'
    data = b'\x00' + parent_key + ser32(i)
    h = hmac_sha_512(parent_chain_code, data)
    return (key(h), chain_code(h))


def derive_along_path(path, seed):
    """Derive an extended key from a 64-byte binary seed and a BIP-0044 path.
    Returns the extended key obtained by following the given derivation path, 
    starting at the extended master key derived from the given binary seed.
    """
    elements = list(element.rstrip("'") for element in path.split('/'))[1:]
    (key, chain_code) = new_master_key(seed)
    for e in elements:
        (key, chain_code) = derive(key, chain_code, int(e) | HARDENED)
    return key


def account_keypair(seed, account_number):
    """Return the account keypair for a 64-byte binary seed and account_number."""
    from stellar_base.keypair import Keypair
    acc_seed = derive_along_path(ACCOUNT_PATH_FORMAT, seed);
    return Keypair.from_raw_seed(acc_seed)
