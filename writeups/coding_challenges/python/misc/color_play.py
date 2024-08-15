class colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    YELLOW = '\033[0;33m'
    RED = '\033[91m'
    BLACK = '\033[0;30m'
    PURPLE = '\033[0;35m'
    WHITE = '\033[0;37m'
    RESET = '\033[0m'

swedish_names = {
   'Erik': 'Johansson',
   'Anna': 'Larsson',
   'Lars': 'Svensson',
   'Eva': 'Nilsson',
   'Johan': 'Andersson',
   'Karin': 'Karlsson',
   'Peter': 'Eriksson',
   'Marie': 'Olsson',
   'Anders': 'Lindberg',
   'Sofia': 'Bergström'
}

def color_code(names, colors):
    color_values = [getattr(colors, attr) for attr in dir(colors) if not attr.startswith('__') and attr != 'RESET']
    color_count = len(color_values)
    
    for i, (firstname, lastname) in enumerate(swedish_names.items()):
        first_color = color_values[i % color_count]
        last_color = color_values[(i + 1) % color_count]
        print(f"{first_color}{firstname}{colors.RESET} {last_color}{lastname}{colors.RESET}")

color_code(swedish_names, colors)