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


    @sp.entry_point
    def move_horizontally(self, update_to):
        sp.verify(
            self.data.bot_manager == sp.sender, 
            message = "Error: non manager call"
        )
            
        self.data.coordinate_x += update_to
    
    @sp.entry_point
    def move_vertically(self, update_to):
        
        sp.verify(
            self.data.bot_manager == sp.sender, 
            message = "Error: non manager call"
        )
            
        self.data.coordinate_y += update_to


    @sp.entry_point
    def shoot_alien(self, alien_type):
        
        sp.verify(
            self.data.bot_manager == sp.sender, 
            message = "Error: non manager call"
        )

        ### SmartPy’s 'sp.if..sp.else' statements let us execute decision making with contract’s latest values in it’s storage. 
        sp.if self.data.plasma_bullet_count >= 1:
            self.data.plasma_bullet_count -= 1
            self.data.record_alien_kills[alien_type] += 1
        sp.else:
            # If the condition fails, we use 'sp.failwith' - a SmartPy helper method - to send back a relevant error message
            sp.failwith("Error: you ran out of bullets! Please buy more!")