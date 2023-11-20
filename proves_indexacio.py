from typing import List
import random
from scipy.cluster.hierarchy import linkage
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Define the Problem class
class Problem:
    def __init__(self, age: int, time: str, genre: str):
        self.age = age
        self.time = time
        self.genre = genre

    def __repr__(self):
        return f"Problem(age={self.age}, time='{self.time}', genre='{self.genre}')"

def encode_problem(problem: Problem) -> List[int]:
    '''
    Function to encode categorical data to numerical values
    '''
    time_encoding = {"mucho": 3, "normal": 2, "poco": 1}
    genre_encoding = {"Ficcion": 1, "No Ficcion": 2}

    return [
        problem.age,
        time_encoding[problem.time],
        genre_encoding[problem.genre]
    ]

def scale_features(problems: List[Problem]) -> np.ndarray:
    '''
    Function to scale features between 0 and 1
    '''
    features = np.array([encode_problem(problem) for problem in problems])

    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)

    return scaled_features

def most_similar(new_problem: Problem, problems: List[Problem], linkage_matrix: np.ndarray) -> Problem:
    # Scale the new problem's features
    scaled_new_problem = MinMaxScaler().fit_transform([encode_problem(new_problem)])[0]

    def get_cluster_representative(node):
        if node < len(problems):
            return scaled_problems[node]
        else:
            # For a merged node, return the mean of the representatives of its children
            left, right = int(linkage_matrix[node - len(problems), 0]), int(linkage_matrix[node - len(problems), 1])
            return (get_cluster_representative(left) + get_cluster_representative(right)) / 2

    def traverse(node):
        if node < len(problems):
            return node

        left, right = int(linkage_matrix[node - len(problems), 0]), int(linkage_matrix[node - len(problems), 1])

        # Calculate distance to left and right child cluster representatives
        left_rep = get_cluster_representative(left)
        right_rep = get_cluster_representative(right)
        left_distance = np.linalg.norm(scaled_new_problem - left_rep)
        right_distance = np.linalg.norm(scaled_new_problem - right_rep)

        # Move to the closer child
        return traverse(left if left_distance < right_distance else right)

    # Start at the root of the dendrogram and traverse down
    closest_node = traverse(len(linkage_matrix) + len(problems) - 2)
    return problems[closest_node]

if __name__ == "__main__":

    # Creem 10 instancies de Problem aleatòries que seran la nostra Database
    db = [
        Problem(
            age=random.randint(10, 70), 
            time=random.choice(["mucho", "normal", "poco"]),
            genre=random.choice(["Ficcion", "No Ficcion"])
        ) for _ in range(10)
    ]

    print("--- BASE DE DADES ---")
    for p in db:
        print(p)

    scaled_problems = scale_features(db)

    # Perform linkage for the hierarchical clustering on scaled features
    linked_scaled = linkage(scaled_problems, method='ward')
    
    new = Problem(age=25, time="normal", genre="Ficcion")
    print("\n--- CAS NOU ---")
    print(new)
    most_similar_problem = most_similar(new, db, linked_scaled)
    most_similar_problem
    print("\n--- RESULTAT ---")
    print(most_similar_problem)
