# 🔮 What Would Ada Say? - An Oracle CLI

> *"The Analytical Engine weaves algebraic patterns just as the Jacquard loom weaves flowers and leaves."* — Ada Lovelace

A playful, generative CLI tool that brings **Hidden Histories** tech pioneers to life! Ask modern technology questions and receive responses channeled through the voices of pioneers whose contributions shaped computing.

## ✨ The Pioneers

### 👩‍💻 Ada Lovelace (1815-1852)
**First Computer Programmer**

Ada wrote the first algorithm intended for machine processing. She saw beyond calculation to imagine computers creating music and art - a vision that took 100+ years to realize.

### 📡 Gladys West (1930-present)
**GPS Pioneer & Mathematician**

A Black woman mathematician whose precise modeling of Earth's shape became the foundation for GPS. Her work guides billions of devices today.

### 🖥️ The ENIAC Programmers (1940s)
**First Electronic Computer Programmers**

Six women - Kay McNulty, Betty Snyder, Marlyn Wescoff, Ruth Lichterman, Jean Jennings, and Frances Bilas - programmed the first electronic computer with no manual, no training, and got erased from history.

### 🌐 Radia Perlman (1951-present)
**Mother of the Internet**

Invented the Spanning Tree Protocol that prevents network loops. Her work enables the Internet to route around failures and scale to billions of devices.

## 🚀 Installation

### Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd nc_ssm_code

# Install in development mode
pip install -e .

# Or install from PyPI (when published)
pip install ada-oracle
```

### Requirements

- Python 3.8+
- Dependencies: `click`, `rich`

## 💬 Usage

### Ask a Question

```bash
# Ask any pioneer (random selection)
ada-oracle ask "What do you think about TikTok's algorithm?"

# Ask a specific pioneer
ada-oracle ask "How does GPS work?" --pioneer gladys

# Get career advice
ada-oracle ask "Should I learn Rust or Go?" --pioneer radia

# Debug help
ada-oracle ask "How do I debug this code?" --pioneer eniac
```

### List All Pioneers

```bash
ada-oracle pioneers
```

### See Examples

```bash
ada-oracle examples
```

### Learn More

```bash
ada-oracle about
```

## 🎓 Educational Use

This tool is designed for:

- **Classroom discussions** - Spark conversations about tech history, ethics, and diversity
- **Interactive learning** - Make Hidden Histories pioneers accessible to students
- **Critical thinking** - Explore how historical perspective shapes modern tech views
- **Inspiration** - Learn from pioneers who overcame barriers to create the digital world

### Discussion Prompts

After using the Oracle, consider:

1. **Historical Context**: How did this pioneer's era shape their perspective?
2. **Hidden Contributions**: Why were some of these pioneers written out of history?
3. **Modern Relevance**: How does historical wisdom apply to today's tech challenges?
4. **Representation**: Who else is missing from tech history? Whose stories should we learn?

## 🎭 Example Conversations

### On Algorithms

```bash
$ ada-oracle ask "Explain algorithms to me" --pioneer ada

╭─────────────────────────────────────────╮
│ Ada Lovelace (1815-1852)                │
│ First Computer Programmer               │
╰─────────────────────────────────────────╯

╭─ 💬 Ada Lovelace's Response ────────────╮
│                                         │
│  What a fascinating question! Let me    │
│  consider the poetical science of       │
│  this...                                │
│                                         │
│  You see, an algorithm is like a        │
│  dance - a sequence of steps that       │
│  transforms one state into another...   │
╰─────────────────────────────────────────╯
```

### On GPS Technology

```bash
$ ada-oracle ask "How does GPS work?" --pioneer gladys

[Gladys West provides mathematical insights about satellite positioning and geodetic modeling]
```

### On Learning to Code

```bash
$ ada-oracle ask "How do I get better at programming?" --pioneer eniac

[The ENIAC Programmers share their experience learning with no manual]
```

## 🎨 Features

- **Authentic Voices**: Each pioneer has a distinct personality shaped by their era and work
- **Contextual Responses**: Questions about algorithms, AI, networks, etc. get relevant answers
- **Beautiful Output**: Rich terminal formatting with colors and panels
- **Educational**: Learn tech history while exploring modern questions
- **Playful**: Make learning interactive and fun!

## 🛠️ Development

### Project Structure

```
nc_ssm_code/
├── ada_oracle/
│   ├── __init__.py
│   ├── cli.py          # CLI interface with Click
│   ├── oracle.py       # Response generation logic
│   └── pioneers.py     # Pioneer character profiles
├── pyproject.toml
├── README.md
└── .gitignore
```

### Adding New Pioneers

To add a new pioneer, edit `ada_oracle/pioneers.py`:

```python
PIONEERS['name'] = Pioneer(
    name="Pioneer Name",
    era="Year-Year",
    specialty="What they're known for",
    personality="Their character traits",
    opening_phrases=[...],
    perspectives={...}
)
```

### Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests (when added)
pytest
```

## 🌟 Why This Matters

**Hidden Histories** refers to the contributions of people - especially women and people of color - who have been systematically erased from technology history.

- Ada Lovelace's contributions were dismissed for over a century
- The ENIAC programmers were called "operators" and forgotten
- Gladys West's GPS work went unrecognized for decades
- Even today, Radia Perlman fights "Mother of the Internet" attribution

This tool makes their wisdom accessible, honors their contributions, and reminds us that technology is built by diverse people with diverse perspectives.

## 🤝 Contributing

Contributions welcome! Ideas:

- Add more pioneers (Katherine Johnson, Grace Hopper, Margaret Hamilton, Annie Easley, etc.)
- Improve response logic
- Add more topic keywords and perspectives
- Create educational lesson plans
- Add multilingual support

## 📚 Learn More

### Resources

- [Hidden Figures](https://www.nasa.gov/content/hidden-figures) - NASA's human computers
- [The ENIAC Programmers Project](http://eniacprogrammers.org/)
- [Gladys West](https://www.af.mil/About-Us/Fact-Sheets/Display/Article/2342457/gladys-west/) - Air Force profile
- [Radia Perlman's Work](https://en.wikipedia.org/wiki/Radia_Perlman)

### Books

- *Code Girls* by Liza Mundy
- *Broad Band* by Claire L. Evans
- *The Innovators* by Walter Isaacson
- *Hidden Figures* by Margot Lee Shetterly

## 📜 License

MIT License - feel free to use this in education, personal projects, or anywhere you want to honor Hidden Histories.

## 🙏 Acknowledgments

Built with love for education, history, and the pioneers whose shoulders we stand on.

---

*"The Analytical Engine has no pretensions to originate anything. It can do whatever we know how to order it to perform."* — Ada Lovelace

*Make sure you know what you're ordering it to do.*
