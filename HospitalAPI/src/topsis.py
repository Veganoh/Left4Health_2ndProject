import numpy as np
import pandas as pd

class Topsis:
    waiting_times = []
    arrival_times = []

    weights = []
    attributes = ['Wait Time', 'Duration']
    candidates = []

    evaluation_matrix = []
    matrixR = []
    matrixV = []

    def __init__(self, waiting_times, arrival_times, weights):
        self.waiting_times = waiting_times
        self.arrival_times = arrival_times
        self.weights = weights
        self.candidates = [item['ID'] for item in self.waiting_times]

        self.create_evaluation_matrix()
        self.create_normalized_evaluation_matrix()
        self.create_weighted_evaluation_matrix()
        self.print_matrixV()

    def create_evaluation_matrix(self):
        wait_times = [item['Wait Time'] for item in self.waiting_times]
        durations = [item['Duration'] for item in self.arrival_times]

        evaluation_matrix = np.array([wait_times, durations], dtype=float).T
        self.evaluation_matrix = evaluation_matrix

        return evaluation_matrix

    # 1º Step - Construction of the normalized decision matrix (Matrix R)
    def create_normalized_evaluation_matrix(self):
        m = len(self.evaluation_matrix)
        n = len(self.attributes)
        divisors = np.empty(n)

        for j in range(n):
            column = self.evaluation_matrix[:, j]
            divisors[j] = np.sqrt(column @ column)

        self.matrixR = self.evaluation_matrix / divisors

        return self.matrixR

    # 2º Step - Construction of the weighted normalized decision matrix (Matrix V)
    def create_weighted_evaluation_matrix(self):
        self.matrixV = self.matrixR * self.weights

        return self.matrixV

    def print_evaluation_matrix(self):
        print(pd.DataFrame(data=self.evaluation_matrix, columns=self.attributes, index=self.candidates))

    def print_matrixR(self):
        print(pd.DataFrame(data=self.matrixR, columns=self.attributes, index=self.candidates))

    def print_matrixV(self):
        print(pd.DataFrame(data=self.matrixV, columns=self.attributes, index=self.candidates))
