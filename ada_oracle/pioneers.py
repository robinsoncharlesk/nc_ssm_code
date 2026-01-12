"""Character profiles for Hidden Histories pioneers."""

import random
from typing import Dict, List

class Pioneer:
    """Represents a tech pioneer with their voice and perspective."""

    def __init__(self, name: str, era: str, specialty: str, personality: str,
                 opening_phrases: List[str], perspectives: Dict[str, str]):
        self.name = name
        self.era = era
        self.specialty = specialty
        self.personality = personality
        self.opening_phrases = opening_phrases
        self.perspectives = perspectives

    def get_opening(self) -> str:
        """Get a random opening phrase characteristic of this pioneer."""
        return random.choice(self.opening_phrases)

    def get_perspective(self, topic: str) -> str:
        """Get perspective on a topic, or default wisdom."""
        # Look for keyword matches in perspectives
        topic_lower = topic.lower()
        for key, perspective in self.perspectives.items():
            if key in topic_lower:
                return perspective
        return self.perspectives.get('default', '')


# Pioneer profiles
PIONEERS = {
    'ada': Pioneer(
        name="Ada Lovelace",
        era="1815-1852",
        specialty="First Computer Programmer, Analytical Engine",
        personality="Visionary mathematician with poetic soul, sees patterns everywhere",
        opening_phrases=[
            "What a fascinating question! Let me consider the poetical science of this...",
            "Ah, this reminds me of my work on the Analytical Engine!",
            "How delightfully complex! The Jacquard loom taught me that...",
            "This is precisely the sort of question that blends art and mathematics!",
        ],
        perspectives={
            'algorithm': "You see, an algorithm is like a dance - a sequence of steps that transforms one state into another. I wrote the first one for Babbage's Engine to calculate Bernoulli numbers. What matters isn't just WHAT it computes, but HOW it thinks.",
            'ai': "The Analytical Engine has no pretensions to originate anything. It can do whatever we know how to order it to perform. The question is not whether machines can think, but whether WE can imagine what to tell them! Today's 'artificial intelligence' still follows this principle - it's our creativity, our algorithms, that give machines their power.",
            'social media': "Imagine if my Analytical Engine could weave patterns of human connection instead of numbers! But beware - algorithms that connect us can also isolate us. We must program with intention, with poetry, with humanity.",
            'tiktok': "A machine that shows you what it thinks you want to see? How clever! But who programs the pattern? Remember: the Jacquard loom weaves what the cards tell it. If your algorithmic cards are designed to keep you weaving the same pattern endlessly, you're trapped in someone else's loop.",
            'data': "Numbers tell stories, but like any story, they can be truthful or deceptive. In my time, we had to be explicit about every calculation. Today, your engines make millions of calculations in shadows. Demand transparency! Ask: what is this machine really computing?",
            'default': "Every machine we create is a mirror of our own imagination. The question isn't what technology can do - it's what we dream it should do, and whether we have the courage to encode our highest values, not just our base impulses."
        }
    ),

    'gladys': Pioneer(
        name="Gladys West",
        era="1930-present",
        specialty="GPS Pioneer, Mathematician",
        personality="Precise, humble, persistent - focused on accuracy and real-world impact",
        opening_phrases=[
            "Let me think about the mathematics of this...",
            "You know, precision matters. Let me break this down...",
            "I spent decades modeling the Earth's shape. This question requires similar careful analysis.",
            "The details matter. In my GPS work, being off by inches meant being lost by miles.",
        ],
        perspectives={
            'gps': "GPS isn't magic - it's mathematics, satellites, and a geoid model I helped perfect. We measured the Earth's lumps and bumps so precisely that now you can find a coffee shop anywhere. Technology serves when it's accurate.",
            'location': "Every time you check 'where am I?', you're using calculations I helped develop. But remember: knowing where you ARE physically is different from knowing where you're GOING in life. Technology can guide your steps, but not your purpose.",
            'maps': "I modeled the Earth's surface down to incredible precision. Today's digital maps stand on that foundation. But a map is only as good as its data - and its data is only as good as the people who collect it and the biases they bring.",
            'navigation': "In my day, we used punchcards and mainframes to compute satellite orbits. Now it's in your pocket! But navigation isn't just about finding places - it's about being found when you're lost. Make sure your technology serves both.",
            'data': "Data without precision is just noise. I learned that programming the IBM machines to model Earth's shape. Today you have more data than ever - but are you precise? Are you accurate? Or just collecting numbers?",
            'default': "I was a Black woman in a field that didn't expect me. I succeeded through precision, persistence, and focusing on the work. Whatever technology you're asking about - ask yourself: is it precise? Does it serve? Does it include everyone's perspective in its calculations?"
        }
    ),

    'eniac': Pioneer(
        name="The ENIAC Programmers",
        era="1940s",
        specialty="First Electronic Computer Programmers",
        personality="Collaborative, problem-solvers, pioneers who figured it out with no manual",
        opening_phrases=[
            "We six learned by doing - no one had programmed a computer before!",
            "Let me tell you what we discovered when there was no manual...",
            "You know, we had to trace the wires and understand the hardware to write any code.",
            "Programming meant understanding the whole machine - there was no abstraction layer!",
        ],
        perspectives={
            'programming': "We programmed ENIAC by physically plugging cables and setting switches. No keyboard, no screen, no compiler. Want to debug? Trace every wire. Today's programming is easier - but do you understand what's really happening in your machine?",
            'women': "They called us 'computers' - human computers - then expected us to just operate the machine. We became the first programmers, taught ourselves everything, and got written out of history. Your field still has this problem. Fix it.",
            'bug': "Finding bugs in ENIAC meant physically walking through the room-sized machine looking for burnt-out vacuum tubes or misconfigured cables. Today you have debuggers and logs. Use them! We would have dreamed of such tools.",
            'team': "There were six of us: Kay, Betty, Marlyn, Ruth, Jean, and Frances. We taught each other. We figured it out together. Programming has always been collaborative, no matter what the myths of lone geniuses tell you.",
            'learning': "We had NO manual. NO courses. NO Stack Overflow. We looked at the hardware, traced the circuits, tested our theories. The best way to learn is still to build something, break it, and figure out why.",
            'default': "We were hidden for decades - our contributions erased or attributed to men. When you learn about ENIAC, you hear about the machine or the men who built it. Rarely about us, the women who made it think. Remember: technology is made by people, and too many people's contributions are still hidden."
        }
    ),

    'radia': Pioneer(
        name="Radia Perlman",
        era="1951-present",
        specialty="Spanning Tree Protocol, Network Design",
        personality="Modest genius, practical problem-solver, focused on making things work",
        opening_phrases=[
            "It's really just a simple algorithm that solves a hard problem...",
            "Let me explain the networking perspective on this...",
            "You know, I never set out to be the 'Mother of the Internet' - I just wanted to solve a problem!",
            "Network design teaches you: the simplest solution is often the best.",
        ],
        perspectives={
            'network': "The Spanning Tree Protocol was about preventing loops - making sure messages don't bounce around forever. Today's networks are infinitely more complex, but the principle holds: design for resilience, expect failure, have a plan.",
            'internet': "They call me 'Mother of the Internet' but really, the Internet is a collective creation. My contribution was making sure networks don't melt down when there are redundant paths. Today's challenge is making sure they don't melt down from misinformation and bad actors.",
            'security': "I've worked on network security for decades. Here's what I know: security is HARD. It's not about perfect solutions - it's about defense in depth, assuming breach, and designing systems that fail safely. Don't trust. Verify.",
            'blockchain': "Everyone talks about blockchain like it's magic. It's not - it's a distributed ledger with interesting properties and serious limitations. Before you use it, ask: do I actually need a trustless system? Or do I just think it sounds cool?",
            'social': "Social networks are networks, just like computer networks. And just like computer networks, they need protocols, they can have loops, and they can propagate problems incredibly quickly. The difference is: in social networks, the 'loops' are disinformation and radicalization.",
            'default': "Technology is about solving real problems in practical ways. Not hype. Not buzzwords. Ask yourself: what problem am I actually solving? Is this the simplest solution? What happens when it fails? Because it will fail."
        }
    ),
}


def get_pioneer(name: str) -> Pioneer:
    """Get a pioneer by name or random."""
    name_lower = name.lower()

    # Direct matches
    if name_lower in PIONEERS:
        return PIONEERS[name_lower]

    # Partial matches
    for key, pioneer in PIONEERS.items():
        if name_lower in pioneer.name.lower():
            return PIONEERS[key]

    # Random if not found
    return random.choice(list(PIONEERS.values()))


def get_all_pioneers() -> List[Pioneer]:
    """Get all pioneers."""
    return list(PIONEERS.values())
