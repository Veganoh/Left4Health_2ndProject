class Ahp:
     
 def __init__(self, criteria, alternatives):
        self.criteria = criteria
        self.alternatives = alternatives
        self.criteria_weights = {}
        self.alternative_scores = {}

def compare_criteria(self):
        self.criteria_weights = {}
        for criterion in self.criteria:
            pairwise_comparison = {}
            for other_criterion in self.criteria:
                if other_criterion == criterion:
                    pairwise_comparison[other_criterion] = 1
                else:
                    comparison = float(input(f"Quao importante  {criterion} em relacao a {other_criterion}? "))
                    pairwise_comparison[other_criterion] = comparison
                    pairwise_comparison[criterion] = 1 / comparison
            self.criteria_weights[criterion] = pairwise_comparison

def compare_alternatives(self):
        self.alternative_scores = {}
        for criterion in self.criteria:
            alternative_scores = {}
            for alternative in self.alternatives:
                comparison = float(input(f"Quao preferivel  {alternative} em relacao aos outros para {criterion}? "))
                alternative_scores[alternative] = comparison
            self.alternative_scores[criterion] = alternative_scores

def calculate_priority(self):
        criteria_priority = {}
        for criterion in self.criteria:
            priority = sum(
                self.criteria_weights[criterion][other_criterion] * (
                    self.alternative_scores[criterion][alternative] / getattr(self.alternatives[alternative], criterion)
                ) for other_criterion in self.criteria for alternative in self.alternatives
            ) / len(self.alternatives)
            criteria_priority[criterion] = priority
        return criteria_priority