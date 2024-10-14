# Author: Shawn Yat Sin
# ID: 261052225

BORDER_SPACING = 1.0 #(represents the amount of spacing on the edges of the plot)
FENCE_COST_PER_METRE = 10.0 #(the cost of fencing per metre)
GRAVEL_COST_PER_METRE_SQUARED = 2.0 #(the cost of gravel per squared metre)
COLOR1_COST = 5.0 #(the cost in dollars of painting the fence a certain color per metre)
COLOR2_COST = 5.0
COLOR3_COST = 5.0
COLOR4_COST = 10.0
COLOR5_COST = 1000.0

def get_perimeter_of_subplot(subplot_w, subplot_h):     

    ''' (float, float) -> (float)
    Takes subplot_w and subplot_h as inputs and returns the perimeter of the rectangular subplot.

    >>> get_perimeter_of_subplot(2,3)
    10
    >>> get_perimeter_of_subplot(-2,3)
    10
    >>> get_perimeter_of_subplot (-2.5, -1.5)
    8.0
    >>> get_perimeter_of_subplot(2.3, 4.56)
    9.16
    '''
    perimeter = 2 * (abs(subplot_w) + abs(subplot_h))  # absolute value in case of negative numbers, perimeter formula = 2(L+l)
    return perimeter

def get_area_of_subplot(subplot_w, subplot_h):
    ''' (float, float) -> (float)
    Takes subplot_w and subplot_h as inputs and returns the area of a subplot.

    >>> get_area_of_subplot(5,6)
    30
    >>> get_area_of_subplot(-3, 4)
    12
    >>> get_area_of_subplot(3.5, 2)
    7.0
    >>> get_area_of_subplot(6.8,2.3)
    15.64
    '''
    area = abs(subplot_w) * abs(subplot_h)        # area = L * l
    return area

def get_cost_per_subplot(subplot_w, subplot_h, color_cost_per_metre):
    ''' (float, float, float) -> (float)
    Takes subplot_w, subplot_h and color_cost_per_metre as inputs and returns the cost of a subplot.
    
    >>> get_cost_per_subplot(5, 5, 5)
    350.0
    >>> get_cost_per_subplot(-5, 4, 3)
    274.0
    >>> get_cost_per_subplot(3.5, 2.8, 1.6)
    165.76
    '''
    perimeter = get_perimeter_of_subplot(subplot_w, subplot_h)
    area = get_area_of_subplot(subplot_w, subplot_h)
    cost_of_fencing = round(perimeter * (FENCE_COST_PER_METRE + color_cost_per_metre), 2)  # rounding for cents
    cost_of_gravel = round(area * GRAVEL_COST_PER_METRE_SQUARED, 2)
    cost_per_subplot = cost_of_fencing + cost_of_gravel
    return cost_per_subplot

def get_cost_for_color(color_choice):
    ''' (int) -> (float)
    Takes color_choice as an integer between 1 and 5 and returns the corresponding cost per metre of painting for that color. If the
    integer is not between 1 and 5, returns 0.0.
    
    >>> get_cost_for_color(1)
    5.0
    >>> get_cost_for_color(5)
    1000.0
    >>> get_cost_for_color(6)
    0.0
    '''
    if color_choice == 1:
        return COLOR1_COST
    
    elif color_choice == 2:
        return COLOR2_COST
    
    elif color_choice == 3:
        return COLOR3_COST
    
    elif color_choice == 4:
        return COLOR4_COST
    
    elif color_choice == 5:
        return COLOR5_COST
    
    else:
        return 0.0

def choose_color():
    ''' () -> (float)
    Prints the list of five available colors to the user. A prompt is then given to the user to select the color
    and the function will return the cost of the given color.
    >>> choose_color()
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 5
    1000.0
    
    >>> choose_color()
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 3
    5.0
    
    >>> choose_color()
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 0
    0.0
    '''
    print("Color options\n", "1 Santa Red\n", "2 Yeti Blue\n", "3 Yuzu Yellow\n", "4 Brilliant Diamond\n", "5 Shining Pearl")
    color = int(input("What color would you like? "))
    cost_for_color = get_cost_for_color(color)
    return cost_for_color

def get_num_subplots(plot_w, plot_h, subplot_w, subplot_h, spacing_w, spacing_h):
    ''' (float, float, float, float, float, float) -> (int)
    Takes as inputs the plot_w, plot_h, subplot_w, subplot_h, spacing_w, spacing_h and calculates the maximum number of subplots
    and returns it as an integer.
    
    >>> get_num_subplots(10, 3, 1, 1, 1, 1)
    4
    >>> get_num_subplots(11, 3, 1, 1, 1, 1)
    5
    >>> get_num_subplots(10, 1, 1, 1, 1, 1)
    0
    '''
    nb_columns = (plot_w - (2 * BORDER_SPACING)) // (subplot_w + spacing_w)
    nb_rows = (plot_h - (2 * BORDER_SPACING)) // (subplot_h + spacing_h)
    remaining_column_space = (plot_w - (2 * BORDER_SPACING)) % (subplot_w + spacing_w)
    remaining_row_space = (plot_h - (2 * BORDER_SPACING)) % (subplot_h + spacing_h)
    
    if nb_columns < 0 or nb_rows < 0:      # if there is either no row or no column
        nb_subplots = 0
        return nb_subplots
         
    if remaining_column_space != 0 and subplot_w <= remaining_column_space: # if remaining column space has space for a subplot
        nb_columns = nb_columns + 1
    
    if remaining_row_space != 0 and subplot_h <= remaining_row_space:  # if remaining row space has space for a subplot
        nb_rows = nb_rows + 1
           
    nb_subplots = int(nb_columns * nb_rows)
    return nb_subplots

def calculate_cost():
    ''' () -> (float)
    Asks the user to enter the following values: plot_w, plot_h, subplot_w, subplot_h, spacing_w, spacing_h. Asks the user for their
    choice of color. Calculates the number of subplots that can fit in the plot, as well as the total cost for the fencing. It will print
    out these two values and return the cost as a float.
    
    >>> calculate_cost()
    Enter the width of the plot: 10
    Enter the height of the plot: 10
    Enter the width of a subplot: 1
    Enter the height of a subplot: 1
    Enter the horizontal spacing between subplots: 1
    Enter the vertical spacing between subplots: 1
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 5
    16.0 subplots can fit in the plot, with a total cost of $64672.0
    64672.0
    
    >>> calculate_cost()
    Enter the width of the plot: 10
    Enter the height of the plot: 10
    Enter the width of a subplot: 1
    Enter the height of a subplot: 1
    Enter the horizontal spacing between subplots: 0
    Enter the vertical spacing between subplots: 0
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 5
    64 subplots can fit in the plot, with a total cost of $258688.0
    258688.0
    
    >>> calculate_cost()
    Enter the width of the plot: 10
    Enter the height of the plot: 10
    Enter the width of a subplot: 1
    Enter the height of a subplot: 1
    Enter the horizontal spacing between subplots: 1
    Enter the vertical spacing between subplots: 1
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 0
    16 subplots can fit in the plot, with a total cost of $672.0
    672.0
    '''
    plot_w = float(input("Enter the width of the plot: "))
    plot_h = float(input("Enter the height of the plot: "))
    subplot_w = float(input("Enter the width of a subplot: "))
    subplot_h = float(input("Enter the height of a subplot: "))
    spacing_w = float(input("Enter the horizontal spacing between subplots: "))
    spacing_h = float(input("Enter the vertical spacing between subplots: "))
    color_cost_per_metre = choose_color()
    nb_subplots = get_num_subplots(plot_w, plot_h, subplot_w, subplot_h, spacing_w, spacing_h)
    cost_per_subplot = get_cost_per_subplot(subplot_w, subplot_h, color_cost_per_metre)
    cost_for_fencing = nb_subplots * cost_per_subplot
    
    print(str(nb_subplots), "subplots can fit in the plot, with a total cost of $" + str(cost_for_fencing))
    return cost_for_fencing
    
def get_num_subplots_for_budget(plot_length, subplot_length, budget, color_cost_per_metre):
    ''' (float, float, float, float) -> (int)
    Takes the plot_length, subplot_length, budget, color_cost_per_metre as inputs. Calculates the number of subplots that
    can fit in the plot size, costing at most the budget and returns it as an integer.
    
    >>> get_num_subplots_for_budget(3, 1, 46, 1)
    1
    >>> get_num_subplots_for_budget(10, 1, 250, 5)
    4
    >>> get_num_subplots_for_budget(10, 1, 5000, 5)
    64
    >>> get_num_subplots_for_budget(10.6, 1.25, 5000, 5)
    47
    '''
    cost_per_subplot = get_cost_per_subplot(subplot_length, subplot_length, color_cost_per_metre)
    nb_subplots = int(budget // cost_per_subplot)
    area_of_subplot = get_area_of_subplot(subplot_length, subplot_length)
    area_of_plot = get_area_of_subplot(plot_length - (2 * BORDER_SPACING), plot_length - (2 * BORDER_SPACING))
    
    if (nb_subplots * area_of_subplot) > area_of_plot:                       # for exceeding area of subplots
        surplus_area = (nb_subplots * area_of_subplot) - area_of_plot        # calculates the extra area taken by the subplots
        
        if surplus_area % area_of_subplot != 0:                              # determines the nb of extra subplots
            nb_extra_subplots = (surplus_area // area_of_subplot) + 1        # adds an extra subplot if surplus area not equally divided
        else:
            nb_extra_subplots = surplus_area // area_of_subplot
            
        nb_subplots = int(nb_subplots - nb_extra_subplots)
        
    return nb_subplots

def find_maximal_subplots():
    ''' () -> (int)
    Asks the user for plot_length, subplot_length, budget and their choice of color. Calculates and prints the number of subplots given
    the budget. Calculates the amount of spacing possible between each subplot. Returns the number of subplots as an integer.
    
    >>> find_maximal_subplots()
    Enter the side length of the plot: 10
    Enter the side length of a subplot: 1
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 1
    Enter your maximum budget: 200
    With the given budget, 3 subplots can fit in the plot, with spacing of 1.67m.
    3
    
    >>> find_maximal_subplots()
    Enter the side length of the plot: 10
    Enter the side length of a subplot: 1
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 1
    Enter your maximum budget: 5000
    With the given budget, 64 subplots can fit in the plot, with spacing of 0.0m.
    64
    
    >>> find_maximal_subplots()
    Enter the side length of the plot: 10
    Enter the side length of a subplot: 10
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 2
    Enter your maximum budget: 5000
    With the given budget, 0 subplots can fit in the plot, with spacing of 0m.
    0
    '''
    plot_length = float(input("Enter the side length of the plot: "))
    subplot_length = float(input("Enter the side length of a subplot: "))
    color_cost_per_metre = choose_color()
    budget = float(input("Enter your maximum budget: "))
    nb_subplots = get_num_subplots_for_budget(plot_length, subplot_length, budget, color_cost_per_metre)
    
    if nb_subplots == 0:
        spacing = 0
        
    elif (nb_subplots * subplot_length) > (plot_length - (2 * BORDER_SPACING)):   
        nb_subplots_per_side = (nb_subplots * subplot_length) // (plot_length - (2  * BORDER_SPACING)) # max nb of subplots that could fit
        extra_space = plot_length - (2 * BORDER_SPACING) - (nb_subplots_per_side * subplot_length)
        spacing = round(extra_space / nb_subplots_per_side, 2)
    else:   
        extra_space = plot_length - (2 * BORDER_SPACING) - (nb_subplots * subplot_length)
        spacing = round(extra_space / nb_subplots, 2)
        
    print("With the given budget,", str(nb_subplots), "subplots can fit in the plot, with spacing of", str(spacing) + "m.")       
    return nb_subplots

def menu():
    ''' () -> (NoneType)
    Prints the options of calculating the cost of plot project or finding maximal subplots and asks the user to pick the desired
    option. It then executes the appropriate option. If the user enters an invalid number, it prints Invalid choice and ends the program.
    When the program ends, Have a nice day! is printed.
    >>> menu()
    Welcome to the Plot Calculator!
    Please choose from the following:
    1 Calculate cost of plot project
    2 Find maximal subplots
    Your choice: 1
    Enter the width of the plot: 10
    Enter the height of the plot: 10
    Enter the width of a subplot: 1
    Enter the height of a subplot: 1
    Enter the horizontal spacing between subplots: 1
    Enter the vertical spacing between subplots: 1
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 5
    16 subplots can fit in the plot, with a total cost of $64672.0
    Have a nice day!
    
    >>> menu()
    Welcome to the Plot Calculator!
    Please choose from the following:
    1 Calculate cost of plot project
    2 Find maximal subplots
    Your choice: 4
    Invalid choice.
    Have a nice day!
    
    >>> menu()
    Welcome to the Plot Calculator!
    Please choose from the following:
    1 Calculate cost of plot project
    2 Find maximal subplots
    Your choice: 2
    Enter the side length of the plot: 10
    Enter the side length of a subplot: 1.5
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 2
    Enter your maximum budget: 400
    With the given budget, 4 subplots can fit in the plot, with spacing of 0.5m.
    Have a nice day!
    
    >>> menu()
    Welcome to the Plot Calculator!
    Please choose from the following:
    1 Calculate cost of plot project
    2 Find maximal subplots
    Your choice: 2
    Enter the side length of the plot: 10
    Enter the side length of a subplot: 9
    Color options
     1 Santa Red
     2 Yeti Blue
     3 Yuzu Yellow
     4 Brilliant Diamond
     5 Shining Pearl
    What color would you like? 1
    Enter your maximum budget: 5000
    With the given budget, 0 subplots can fit in the plot, with spacing of 0m.
    Have a nice day!
    '''
    print("Welcome to the Plot Calculator!\n" + "Please choose from the following:")
    print("1 Calculate cost of plot project\n" + "2 Find maximal subplots")
    choice = int(input("Your choice: "))
    
    if choice == 1:
        calculate_cost()
        
    elif choice == 2:
        find_maximal_subplots()
    
    else:
        print("Invalid choice.")
        
    print("Have a nice day!")
    
