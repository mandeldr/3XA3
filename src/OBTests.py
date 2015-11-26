import unittest2 as unittest
import identity.RicardianContract
import identity.Identity
import identity.Identity.Settings
import identity.Store
import identity.Notary
import identity.Contracts
import DHTMod
import InitializationMod
import node.Node
import hashlib
import time


class RicardianContractTests(unittest.TestCase):

    #contract_dict
    contract_dict = dict()
    contract_dict['expiry'] = "30/12/15"
    contract_dict['price'] = "50"
    contract_dict['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
    contract_dict['item_name'] = "Hat"

    #seller_settings
    seller_settings = identity.Identity.Settings()

    def test_constructor(self, contract_dict, seller_settings):
        testRicardianContract = identity.RicardianContract(contract_dict, seller_settings)
        self.assertIsInstance(testRicardianContract, identity.RicardianContract, "Constructor returns the correct instance type (Ricardian Contract)")

    def test_get_module(self):
        return None

    def test_contract_hash(self):
        return None

    def test_get_dict(self):
        return None

class IdentityTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_get_settings(self):
        return None

    def test_set_settings(self):
        return None

    def test_new_contract(self):
        return None

    def test_get_my_contracts(self):
        return None

    def test_save(self):
        return None

class SettingsTests(unittest.TestCase):

    def test_constructor(self):
        return None

class StoreTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_get(self):
        return None

    def test_set(self):
        return None

    def test_addMerchant(self):
        return None

class NotaryTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_get(self):
        return None

    def test_set(self):
        return None

class ContractsTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_getExpiredContracts(self):
        return None

    def test_getOnGoingContracts(self):
        return None

    def test_addContract(self):
        return None

class DHTModTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_ping(self):
        return None

    def test_store(self):
        return None

    def test_find_node(self):
        return None

    def test_find_keyword(self):
        return None

class InitializationModTests(unittest.TestCase):

    def test_create_GUID(self):
        return None

    def test_initialize_Bazaar(self):
        return None

    def test_which(self):
        return None

class NotaryModTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_get_all(self):
        return None

    def test_get(self):
        return None

class OBNodeTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_start_node(self):
        return None

    def test_listen_on_here(self):
        return None

    def test_attempt_bootstrap(self):
        return None

    def test_bootstrap_done(self):
        return None

    def test_saveState(self):
        return None

if __name__ == '__main__':
    unittest.main()











