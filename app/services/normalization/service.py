from app.services.normalization.models import NormalizedDocument

class NormalizationService:
    def normalize(self, text: str) -> NormalizedDocument:
        """
        Normalize the extracted text into a structured format.
        """
        # In a real implementation, this would call an LLM.
        # For now, we stub it.
        return self._llm_normalize(text)

    def _llm_normalize(self, text: str) -> NormalizedDocument:
        """
        Stub for LLM-based normalization.
        """
        # Simple stub logic for demonstration
        return NormalizedDocument(
            business_intent="To be determined by LLM analysis of: " + text[:50] + "...",
            explicit_requirements=["Requirement 1 (stub)", "Requirement 2 (stub)"],
            assumptions=["Assumption 1 (stub)"],
            constraints=["Constraint 1 (stub)"],
            ambiguities=["Ambiguity 1 (stub)"]
        )
