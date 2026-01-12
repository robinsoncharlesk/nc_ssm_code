"""Oracle response generation logic."""

import random
from typing import Optional
from .pioneers import Pioneer, get_pioneer, get_all_pioneers


class Oracle:
    """The Oracle that channels pioneer wisdom."""

    def __init__(self):
        self.pioneers = get_all_pioneers()

    def ask(self, question: str, pioneer_name: Optional[str] = None) -> tuple[Pioneer, str]:
        """
        Ask a question and get a response from a pioneer.

        Args:
            question: The question to ask
            pioneer_name: Optional specific pioneer, otherwise random

        Returns:
            Tuple of (Pioneer, response)
        """
        # Select pioneer
        if pioneer_name:
            pioneer = get_pioneer(pioneer_name)
        else:
            pioneer = random.choice(self.pioneers)

        # Generate response
        response = self._generate_response(pioneer, question)

        return pioneer, response

    def _generate_response(self, pioneer: Pioneer, question: str) -> str:
        """Generate a response in the pioneer's voice."""
        # Start with characteristic opening
        opening = pioneer.get_opening()

        # Get perspective on the topic
        perspective = pioneer.get_perspective(question)

        # Add some contextual wisdom
        wisdom = self._add_contextual_wisdom(pioneer, question)

        # Combine into response
        response = f"{opening}\n\n{perspective}"

        if wisdom:
            response += f"\n\n{wisdom}"

        return response

    def _add_contextual_wisdom(self, pioneer: Pioneer, question: str) -> str:
        """Add contextual wisdom based on pioneer and question type."""
        question_lower = question.lower()

        # Check for question type
        if any(word in question_lower for word in ['should i', 'should we', 'what should']):
            return self._get_advice_wisdom(pioneer)
        elif any(word in question_lower for word in ['why', 'how come', 'explain']):
            return self._get_explanation_wisdom(pioneer)
        elif any(word in question_lower for word in ['future', 'will', 'going to']):
            return self._get_future_wisdom(pioneer)
        else:
            return ""

    def _get_advice_wisdom(self, pioneer: Pioneer) -> str:
        """Get advice-oriented wisdom."""
        advice = {
            'ada': "In the end, trust your imagination. The Analytical Engine was impossible until we imagined it possible.",
            'gladys': "My advice: do the work. Be precise. Don't wait for permission or recognition. The GPS system I helped build speaks for itself.",
            'eniac': "Our advice: dive in. You learn by doing, by breaking things, by figuring it out. Don't wait for the perfect tutorial - it doesn't exist.",
            'radia': "Keep it simple. Solve the actual problem, not the problem you wish you had. And document your work - your future self will thank you."
        }
        for key, pioneer_advice in advice.items():
            if key in pioneer.name.lower():
                return advice[key]
        return ""

    def _get_explanation_wisdom(self, pioneer: Pioneer) -> str:
        """Get explanation-oriented wisdom."""
        explanations = {
            'ada': "Understanding requires both analysis and imagination. Break it down into steps, but don't lose sight of the whole.",
            'gladys': "The answer is in the mathematics. Calculate it, verify it, test it. Precision reveals truth.",
            'eniac': "To understand something, take it apart. Trace the wires. Follow the logic. See how the pieces connect.",
            'radia': "The best explanations are simple. If you can't explain it simply, you don't understand it well enough yet."
        }
        for key, explanation in explanations.items():
            if key in pioneer.name.lower():
                return explanations[key]
        return ""

    def _get_future_wisdom(self, pioneer: Pioneer) -> str:
        """Get future-oriented wisdom."""
        future = {
            'ada': "The future is limited only by our imagination and our willingness to encode our values into our machines.",
            'gladys': "The future will be built on precision and persistence. Technology that serves humanity, not exploits it.",
            'eniac': "The future belongs to those who learn by doing, who collaborate, and who remember the hidden contributions of the past.",
            'radia': "The future will have new problems, but the principles remain: solve real problems, keep it simple, design for failure."
        }
        for key, future_wisdom in future.items():
            if key in pioneer.name.lower():
                return future[key]
        return ""

    def list_pioneers(self) -> list[Pioneer]:
        """Get list of all available pioneers."""
        return self.pioneers
