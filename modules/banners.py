from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from modules.utils import get_terminal_width


# https://patorjk.com/software/taag/
def print_banner(console) -> None:
    width = get_terminal_width()
    height = 8
    banner = """\
████████╗██╗  ██╗██████╗ ███████╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
╚══██╔══╝██║  ██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
   ██║   ███████║██████╔╝█████╗  ███████║   ██║   ██║     ███████║█████╗  ██║     █████╔╝ 
   ██║   ██╔══██║██╔══██╗██╔══╝  ██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
   ██║   ██║  ██║██║  ██║███████╗██║  ██║   ██║   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                                                                                          
"""

    banner_small = """\
 ______ __                    __   _____ __             __  
/_  __// /   ____ ___  ___ _ / /_ / ___// /  ___  ____ / /__
 / /  / _ \ / __// -_)/ _ `// __// /__ / _ \/ -_)/ __//  '_/
/_/  /_//_//_/   \__/ \_,_/ \__/ \___//_//_/\__/ \__//_/\_\ 
"""

    if width < 90:
        banner = banner_small
        height = 7

    panel = Panel(
        Align(
            Text(banner, justify="center", style="blue"),
            vertical="middle",
            align="center",
        ),
        width=width,
        height=height,
        subtitle="by Rexbeast made with <3",
    )
    console.print(panel)
