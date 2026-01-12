"""CLI interface for the Ada Oracle."""

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from .oracle import Oracle

console = Console()
oracle = Oracle()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """
    🔮 What Would Ada Say? - An Oracle CLI

    Ask modern tech questions and get responses from Hidden Histories pioneers:
    Ada Lovelace, Gladys West, the ENIAC Programmers, and Radia Perlman.
    """
    pass


@cli.command()
@click.argument('question', nargs=-1, required=True)
@click.option('--pioneer', '-p', help='Specific pioneer to ask (ada, gladys, eniac, radia)')
@click.option('--plain', is_flag=True, help='Plain text output without formatting')
def ask(question, pioneer, plain):
    """
    Ask a question to a Hidden Histories pioneer.

    Examples:

      ada-oracle ask "What do you think about TikTok's algorithm?"

      ada-oracle ask "Should I learn Rust?" --pioneer ada

      ada-oracle ask "How do I debug my code?" --pioneer eniac
    """
    question_text = " ".join(question)

    if not question_text.strip():
        console.print("[red]Please provide a question![/red]")
        return

    # Get response from oracle
    pioneer_obj, response = oracle.ask(question_text, pioneer)

    if plain:
        # Plain text output
        print(f"\n{pioneer_obj.name} ({pioneer_obj.era})")
        print(f"{pioneer_obj.specialty}")
        print(f"\n{response}\n")
    else:
        # Rich formatted output
        console.print()

        # Pioneer header
        header = f"[bold cyan]{pioneer_obj.name}[/bold cyan] [dim]({pioneer_obj.era})[/dim]\n[italic]{pioneer_obj.specialty}[/italic]"

        # Response panel
        panel = Panel(
            response,
            title=f"💬 {pioneer_obj.name}'s Response",
            title_align="left",
            border_style="cyan",
            padding=(1, 2),
        )

        console.print(Panel(header, border_style="magenta"))
        console.print(panel)
        console.print()


@cli.command()
def pioneers():
    """List all available pioneers."""
    console.print()
    console.print("[bold magenta]🌟 Hidden Histories Tech Pioneers[/bold magenta]\n")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Name", style="cyan", width=20)
    table.add_column("Era", style="yellow", width=15)
    table.add_column("Specialty", style="green")

    for p in oracle.list_pioneers():
        table.add_row(p.name, p.era, p.specialty)

    console.print(table)
    console.print()
    console.print("[dim]Use --pioneer or -p to ask a specific pioneer[/dim]")
    console.print("[dim]Example: ada-oracle ask \"your question\" --pioneer ada[/dim]")
    console.print()


@cli.command()
def about():
    """Learn about the Ada Oracle project."""
    about_text = """
# 🔮 What Would Ada Say?

A playful, generative CLI tool that brings **Hidden Histories** tech pioneers to life!

Ask modern technology questions and receive responses channeled through the voices of:

- **Ada Lovelace** (1815-1852) - The first computer programmer
- **Gladys West** (1930-present) - GPS pioneer and mathematician
- **The ENIAC Programmers** (1940s) - First electronic computer programmers
- **Radia Perlman** (1951-present) - Inventor of Spanning Tree Protocol

## Why This Matters

Technology history is full of hidden contributions - especially from women and people of color.
This tool makes their wisdom accessible, interactive, and fun.

## Educational Use

- Use in classrooms to teach tech history
- Spark discussions about algorithms, AI, ethics, and technology
- Make learning interactive and engaging
- Remember the pioneers whose contributions were erased

## Examples

Ask about anything: TikTok algorithms, debugging code, career advice, AI ethics,
networking, GPS, social media, blockchain, or what programming language to learn.

Each pioneer brings their unique perspective shaped by their era, their challenges,
and their groundbreaking work.
    """

    console.print(Markdown(about_text))


@cli.command()
def examples():
    """Show example questions to ask."""
    console.print()
    console.print("[bold magenta]💡 Example Questions[/bold magenta]\n")

    examples_list = [
        ("What do you think about TikTok's algorithm?", "See Ada's take on algorithmic loops"),
        ("How does GPS work?", "Learn from Gladys West who helped make it possible"),
        ("I'm stuck debugging my code. Help!", "Get advice from the ENIAC programmers"),
        ("Should I use blockchain for this project?", "Radia Perlman cuts through the hype"),
        ("What do you think about AI ethics?", "Multiple perspectives on modern challenges"),
        ("How do I get better at programming?", "Timeless wisdom from the pioneers"),
        ("What's your advice for women in tech?", "Hear from those who paved the way"),
        ("Explain neural networks to me", "See how pioneers understand modern concepts"),
    ]

    for question, description in examples_list:
        console.print(f"[cyan]❯[/cyan] [bold]{question}[/bold]")
        console.print(f"  [dim]{description}[/dim]\n")

    console.print("[dim]Try any question! The pioneers will respond in their unique voices.[/dim]")
    console.print()


if __name__ == '__main__':
    cli()
