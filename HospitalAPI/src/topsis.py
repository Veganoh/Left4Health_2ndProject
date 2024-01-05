import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)


class Topsis:
    waiting_times = []
    arrival_times = []

    weights = []
    attributes = ['Wait Time', 'Duration']
    candidates = []

    worst_similarity = []
    best_similarity = []

    evaluation_matrix = np.array([])
    matrixR = np.array([])
    matrixV = np.array([])
    a_pos = []
    a_neg = []
    ideal_negative_solutions = pd.DataFrame()

    sp, sn = [], []
    cn = []
    separation_measures_relative_distance = pd.DataFrame()
    ordered_alternatives = pd.DataFrame()

    M = 0  # Number of alternatives
    N = 0  # Number of attributes

    def __init__(self, waiting_times, arrival_times, weights):
        self.waiting_times = waiting_times
        self.arrival_times = arrival_times
        self.weights = weights
        self.candidates = [item['ID'] for item in self.waiting_times]

        self.create_evaluation_matrix()
        self.create_normalized_evaluation_matrix()
        self.create_weighted_evaluation_matrix()
        self.determine_ideal_and_negative_ideal_solutions()
        self.calculate_separation_measures()
        self.calculate_relative_distance()
        self.rank_alternatives()

    def create_evaluation_matrix(self):
        wait_times = [item['Wait Time'] for item in self.waiting_times]
        durations = [item['Duration'] for item in self.arrival_times]

        evaluation_matrix = np.array([wait_times, durations], dtype=float).T
        self.evaluation_matrix = evaluation_matrix

        return evaluation_matrix

    # 1º Step - Construction of the normalized decision matrix (Matrix R)
    def create_normalized_evaluation_matrix(self):
        self.M = len(self.evaluation_matrix)
        self.N = len(self.attributes)
        divisors = np.empty(self.N)

        for j in range(self.N):
            column = self.evaluation_matrix[:, j]
            divisors[j] = np.sqrt(column @ column)

        self.matrixR = self.evaluation_matrix / divisors

        return self.matrixR

    # 2º Step - Construction of the weighted normalized decision matrix (Matrix V)
    def create_weighted_evaluation_matrix(self):
        self.matrixV = self.matrixR * self.weights

        return self.matrixV

    # 3º Step - Determine the positive and negative ideal solution
    def determine_ideal_and_negative_ideal_solutions(self):
        self.a_pos = np.zeros(self.N)
        self.a_neg = np.zeros(self.N)

        for j in range(self.N):
            column = self.matrixV[:, j]
            max_val = np.max(column)
            min_val = np.min(column)

            self.a_pos[j] = min_val
            self.a_neg[j] = max_val

        self.ideal_negative_solutions = pd.DataFrame(data=[self.a_pos, self.a_neg], index=["$A^*$", "$A^-$"],
                                                     columns=self.attributes)

        return self.ideal_negative_solutions

    # 4º Step - Calculate the separation measures for each alternative Si* & Si-
    def calculate_separation_measures(self):
        worst_distance_mat = (self.matrixV - self.a_neg) ** 2
        best_distance_mat = (self.matrixV - self.a_pos) ** 2

        self.sn = np.sqrt(np.sum(worst_distance_mat, axis=1))
        self.sp = np.sqrt(np.sum(best_distance_mat, axis=1))

    # 5º Step - Calculate the relative distance to the ideal distance
    def calculate_relative_distance(self):
        np.seterr(all='ignore')
        self.cn = self.sn / (self.sn + self.sp)



    # 6º Step - Order the set of alternatives
    def rank_alternatives(self):
        df = pd.DataFrame(data=zip(self.cn), index=self.candidates, columns=["$C^-$"])
        df_sorted = df.sort_values(by='$C^-$', ascending=False)
        df_sorted['$C^-$'] = df_sorted.index
        df_sorted.reset_index(drop=True, inplace=True)
        self.ordered_alternatives = df_sorted
        return df_sorted

    # Get best 3 alternatives
    def get_best_alternatives(self):
        best_alternative_1 = self.ordered_alternatives.iloc[0]['$C^-$']
        best_alternative_2 = self.ordered_alternatives.iloc[1]['$C^-$']
        best_alternative_3 = self.ordered_alternatives.iloc[2]['$C^-$']
        return best_alternative_1, best_alternative_2, best_alternative_3

    def print_evaluation_matrix(self):
        print(pd.DataFrame(data=self.evaluation_matrix, columns=self.attributes, index=self.candidates))

    def print_matrixR(self):
        print(pd.DataFrame(data=self.matrixR, columns=self.attributes, index=self.candidates))

    def print_matrixV(self):
        print(pd.DataFrame(data=self.matrixV, columns=self.attributes, index=self.candidates))

    def print_ideal_negative_solutions(self):
        print(self.ideal_negative_solutions)

    def print_separation_measures(self):
        print(pd.DataFrame(data=zip(self.sp, self.sn), index=self.candidates, columns=["$S^*$", "$S^-$"]))

    def print_relative_distances(self):
        print(pd.DataFrame(data=zip(self.cp, self.cn), index=self.candidates, columns=["$C^*$", "$C^-$"]))

    def print_ranked_alternatives(self):
        print(self.ordered_alternatives)