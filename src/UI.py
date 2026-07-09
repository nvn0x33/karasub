from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt, Confirm

class UI:
    config = {
        "hl_color": "",
        "hl_bg": "",
        "text_color": "",
        "bg_color": "",
        "font_style": "",
        "font_size": ""
    }
    
    def __init__(self):
        self.print_UI()
    
    def print_UI(self):
        Console().clear()
        print("[bold cyan]karasub[/bold cyan] is a tool that adds karaoke-style, word-by-word highlighted subtitles to your video.\n")

        print(Panel(
            "[green]Put your video(s) in [bold]input/[/bold][/green]\n"
            "[green]Output will be saved in [bold]output/[/bold][/green]",
            title="[bold cyan]karasub[/bold cyan]"
        ))

        if not Confirm.ask("Continue?"):
            exit()

        print("\n[bold magenta]HIGHLIGHTED WORD:[/bold magenta]")
        print("[dim]Only hex codes are allowed:[/dim]")
        
        self.config.hl_color = Prompt.ask("  Text color       default - [white]white[/white] (#FFFFFF)", default="#FFFFFF")
        self.config.hl_bg = Prompt.ask("  Background       default - [yellow]yellow[/yellow] (#FFFF00)", default="#FFFF00")

        print("\n[bold magenta]OTHER WORDS:[/bold magenta]")
        self.config.text_color = Prompt.ask("  Text color       default - [white]white[/white] (#FFFFFF)", default="#FFFFFF")
        self.config.bg_color = Prompt.ask("  Background       default - [grey0 on white]black[/grey0 on white] (#000000)", default="#000000")

        print("\n[bold magenta]FONT:[/bold magenta]")
        self.config.font = Prompt.ask("  Style (Inter / Roboto Mono / path to .ttf, .otf, .ttc): ", default="Inter")
        self.config.size = Prompt.ask("  Size (Enter = auto)", default="auto")