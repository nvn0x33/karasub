from rich import print
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

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
hl_color = Prompt.ask("  Text color       default - [white]white[/white] (#FFFFFF)", default="#FFFFFF")
hl_bg = Prompt.ask("  Background       default - [yellow]yellow[/yellow] (#FFFF00)", default="#FFFF00")

print("\n[bold magenta]OTHER WORDS:[/bold magenta]")
text_color = Prompt.ask("  Text color       default - [white]white[/white] (#FFFFFF)", default="#FFFFFF")
bg_color = Prompt.ask("  Background       default - [grey0 on white]black[/grey0 on white] (#000000)", default="#000000")

print("\n[bold magenta]FONT:[/bold magenta]")
font = Prompt.ask("  Style (Inter / Roboto Mono / path to .ttf, .otf, .ttc): ", default="Inter")
size = Prompt.ask("  Size (Enter = auto)", default="auto")