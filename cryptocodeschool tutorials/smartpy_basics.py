import smartpy as sp

### Creating a class called Cryptobot which is essentially the smart contract
### It inherits the Contract class from Smartpy
class Cryptobot(sp.Contract):

    def __init__(self, manager_address, life_state):
        
        self.init(
            bot_manager = manager_address,
            name = "terminator",
            is_alive = life_state,
            

            ### Unlike Python, SmartPy data types are signed.     
            # Non-negative integers: eg: 4 is represented by 'sp.TNat', called as 'sp.nat'
            # Signed integers (i.e integers that can hold negative values): eg: -42 is represented by 'sp.TInt', called as 'sp.int'
            coordinate_x = sp.int(0), 
            coordinate_y = sp.nat(0), 
            
            plasma_bullet_count = 5,

            ### Maps are equivalent to python dictionary, Maps are represented by type 'sp.TMap(key, value)' in SmartPy
            record_alien_kills = {
                "simple_alien": sp.nat(0), 
                "boss_alien": sp.nat(0), 
            }  
        )

    ### Entry functions are basically class methods with the added capacity to modify a contract’s local storage.
    # to define entry point functions, @sp.entry_point decorator is used
    @sp.entry_point
    def change_name(self, new_name):
        

        ### 'sp.verify' comes in handy to prevent an entry function from proceeding if certain conditions are not met.
        # To specifically check for equality conditions, we can use 'sp.verify_equal'
        sp.verify(
            self.data.bot_manager == sp.sender, 
            message = "Error: non manager call"
        )

        self.data.name = new_name