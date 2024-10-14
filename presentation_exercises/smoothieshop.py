from smoothie import Smoothie

TYPES = ['Regular', 'Thick', 'Wet', 'Hot']
TOPPINGS = ['Banana', 'Oreo', 'Berry', 'Kiwi', 'Kale']
SIZES = ['Small', 'Medium', 'Large', 'X-Large']

SMOOTHIE_TYPES = [('Regular', 1.00),('Thick', 1.50), ('Wet', 1.00), ('Hot', 1.00)]
SMOOTHIE_TOPPINGS = [('Banana', 1.00), ('Oreo', 1.50), ('Berry', 1.00), ('Kiwi', 1.00), ('Kale', 1.20)]
SMOOTHIE_SIZES = [('Small', 4.00), ('Medium', 4.60), ('Large', 5.10), ('X-Large', 6.00)]

class SmoothieShop:
    
    ''' A class that represents a SmoothieShop that sells smoothies
    Attributes: smoothies'''
    
    def __init__(self, smoothies=[]):
        ''' (list) -> SmoothieShop
        Creates a SmoothieShop object with an optional list of smoothies.
        '''
        self.smoothies = smoothies
        
    def add_to_bill(self, smoothie):
        ''' (Smoothie) -> NoneType
        Adds a smoothie to the bill.
        '''
        self.smoothies.append(smoothie)
        
            
    def bill_subtotal(self):
        bill_subtotal = 0
        for smoothie in self.smoothies:
            bill_subtotal += smoothie.subtotal
            
        return bill_subtotal
    
    def print_receipt(self, subtotal):
        ''' (float) -> Nonetype
        Calculates the taxes on top of the subtotal, and prints the final total to the screen,
        as well as the order details.
        '''
        gst = round(subtotal * 0.05)
        qst = round(subtotal * 0.09975)
        total = round(subtotal + gst + qst, 2)
        count = 1
        for order in self.smoothies:
            print("\nORDER"+ str(count)+":", order.smoothie_type, '[' + '|'.join(order.smoothie_topping) + ']', order.smoothie_size)
            print("PRICE:\t", order.subtotal)
            count += 1
        print("\nCOST:\t " + str(subtotal))
        print("GST:\t " + str(gst))
        print("QST:\t " + str(qst))
        print("TOTAL:\t " + str(total))
    
    #def add_tips(self):
                
def order():
    final_cost = SmoothieShop()
    order_completed = 'N'
    toppings = []
    while order_completed == 'N':
        print('\nThese are the smoothie types we offer:')
        for opt in SMOOTHIE_TYPES:
            print(opt[0])
        smoothie_type = input("What type of smoothie would you like? ")
        
        print('\nThese are the available toppings:')
        for opt in SMOOTHIE_TOPPINGS:
            print(opt[0])    
        topping = input("What topping would you like? ")
        toppings.append(topping)
        
        print('\nThese are the available sizes:')
        for opt in SMOOTHIE_SIZES:
            print(opt[0])    
        size = input("What size would you like? ")
        
        order = Smoothie(smoothie_type, size, toppings)
        
        extra_topping = 'Y'
        while extra_topping == 'Y':                                            # can add as many toppings as we want
            extra_topping = input('\nWould you like to add a topping? (Y/N) ')
            if extra_topping == 'Y':
                print('\nThese are the available toppings:')
                for opt in SMOOTHIE_TOPPINGS:
                    print(opt[0])    
                topping = input("What topping would you like to add? ")
                order.add_topping(topping)
                
        order.calculate_subtotal()
                
        final_cost.add_to_bill(order)                             # adding Smoothie object to SmoothieShop object
        order_completed = input('\nWill that be all? (Y/N) ')     # if 'N', will make another Smoothie
    
    bill_subtotal = final_cost.bill_subtotal()                    # adds all the smoothie subtotals
    final_cost.print_receipt(bill_subtotal)
    
if __name__ == '__main__':
    order()
        
        
        
            
