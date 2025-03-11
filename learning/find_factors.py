
class AlgorithmCalculator:

    def __init__(self, sample_list):
        self.sample_list = sample_list

    def find_pair_of_factors(self, target_sum):
        list_of_pairs = []
        seen = set()

        for number in self.sample_list:
            second_factor = target_sum - number
            if second_factor in seen:
                list_of_pairs.append((number, second_factor))
            seen.add(number)

        return list_of_pairs

    def clean_up(self):
        print("CLEANING")
        pass

