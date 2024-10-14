TYPES = ['Regular', 'Thick', 'Wet', 'Hot']
TOPPINGS = ['Banana', 'Oreo', 'Berry', 'Kiwi', 'Kale']
SIZES = ['Small', 'Medium', 'Large', 'X-Large']

SMOOTHIE_TYPES = [('Regular', 1.00),('Thick', 1.50), ('Wet', 2.00), ('Hot', 1.00)]
SMOOTHIE_TOPPINGS = [('Banana', 1.00), ('Oreo', 1.50), ('Berry', 1.00), ('Kiwi', 1.00), ('Kale', 1.20)]
SMOOTHIE_SIZES = [('Small', 4.00), ('Medium', 4.60), ('Large', 5.10), ('X-Large', 6.00)]

class Smoothie:
    
    ''' A class that represents a Smoothie.
        Attributes: smoothie_type, smoothie_topping, smoothie_size
    '''
    
    def __init__(self, smoothie_type, smoothie_size, smoothie_topping =[], subtotal = 0):
        ''' (str, str, list, float)
        Creates a Smoothie object.
        '''
        if smoothie_type not in TYPES or smoothie_topping[0] not in TOPPINGS or smoothie_size not in SIZES:
            raise ValueError("One of the smoothie options was misspelled or does not exist. Please reorder.")
        
        self.smoothie_type = smoothie_type
        self.smoothie_topping = smoothie_topping[:] # assigning a mutable data type, so I made a copy of the list
        self.smoothie_size = smoothie_size
                
    def add_topping(self, topping):
        ''' (str) -> NoneType
        Adds a topping to the smoothie.
        '''
        if topping in TOPPINGS:
            self.smoothie_topping.append(topping)
                
    def calculate_subtotal(self):
        ''' () -> NoneType
        Calculates the subtotal for the current SmoothieOrder object and updates it.
        '''
        subtotal = 0
        for opt in SMOOTHIE_TYPES:
            if self.smoothie_type == opt[0]:
                subtotal += opt[1]
                break
            
        for opt in SMOOTHIE_TOPPINGS:
            for topping in self.smoothie_topping: 
                if topping == opt[0]:
                    subtotal += opt[1]
                
        for size in SMOOTHIE_SIZES:
            if self.smoothie_size == size[0]:
                subtotal += size[1]
                break
            
        self.subtotal = subtotal
    
