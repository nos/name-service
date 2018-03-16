"""
NeoSense Smart Contract based Licensing
Created by Dean van Dugteren (City of Zion, VDT Network)
hello@dean.press
"""

from boa.interop.Neo.Runtime import CheckWitness, Log
from boa.interop.Neo.Storage import GetContext, Put, Delete, Get
from boa.builtins import concat


# Main Operation

def Main(operation, args):
    """
    Main definition for the smart contracts

    :param operation: the operation to be performed
    :type operation: str

    :param args: list of arguments.
        args[0] is always sender script hash
        args[1] is always domain
        args[2] (optional) is either target or other address
        args[3] (optional) is target (if args[2] is address)
    :param type: str

    :return:
        byterarray: The result of the operation
    """
    # Common definitions
    user_hash = args[0]
    domain = args[1]
    domain_owner_key = concat(domain, ".owner")
    domain_target_key = concat(domain, ".target")
    owner = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'

    # This doesn't require authentication
    if operation == 'GetDomain':
        return Get(GetContext(), domain_target_key)

    # Everything after this requires authorization
    authorized = CheckWitness(user_hash)
    if not authorized:
        Log("Not Authorized")
        return False
    Log("Authorized")

    if operation == 'RegisterDomain':
        if(CheckWitness(owner)):
            address = args[2]
            Put(GetContext(), domain_owner_key, address)
            if len(args) == 4:
                target = args[3]
                Put(GetContext(), domain_target_key, target)
            return True

    if operation == 'SetDomainTarget':
        if CheckWitness(domain_owner_key) or CheckWitness(owner):
            # License the product
            target = args[2]
            Put(GetContext(), domain_target_key, target)
            return True

    if operation == 'DeleteDomain':
        if(CheckWitness(owner)):
            Delete(GetContext(), domain_owner_key)
            Delete(GetContext(), domain_target_key)
            return True
            
    return False
