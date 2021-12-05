from collections import Counter


def binary_to_int(binary: str):
    return int(binary, 2)


def parse_input(filepath):
    with open(filepath, "r") as f:
        binary_nums = [line.strip() for line in f]
    return binary_nums


class SubmarineDiagnostics:
    def __init__(self, report: list[str]):
        self.report = report

    @property
    def power_consumption(self):
        return self.gamma * self.epsilon

    @property
    def _gamma(self) -> str:
        gamma = ""
        for i in zip(*self.report):
            c = Counter(i).most_common()
            gamma += c[0][0]
        return gamma

    @property
    def gamma(self) -> int:
        return binary_to_int(self._gamma)

    @property
    def _epsilon(self) -> str:
        epsilon = ""
        for i in zip(*self.report):
            c = Counter(i).most_common()
            epsilon += c[1][0]
        return epsilon

    @property
    def epsilon(self):
        return binary_to_int(self._epsilon)

    @property
    def life_support_rating(self):
        return self.c02_scrubber_rating * self.oxygen_generator_rating

    @property
    def _c02_scrubber_rating(self):
        nums = self.report.copy()
        position = 0
        while len(nums) != 1:
            number = [number[position] for number in nums]
            c = Counter(number).most_common()
            if c[0][1] == c[1][1]:
                least_common_bit = "0"
            else:
                least_common_bit = c[1][0]
            nums = [number for number in nums if number[position] == least_common_bit]
            position += 1
        return nums[0]

    @property
    def c02_scrubber_rating(self):
        return binary_to_int(self._c02_scrubber_rating)

    @property
    def _oxygen_generator_rating(self):
        nums = self.report.copy()
        position = 0
        while len(nums) != 1:
            number = [number[position] for number in nums]
            c = Counter(number).most_common()
            if len(c) > 1 and c[0][1] == c[1][1]:
                most_common_bit = "1"
            else:
                most_common_bit = c[0][0]
            nums = [number for number in nums if number[position] == most_common_bit]
            position += 1
        return nums[0]

    @property
    def oxygen_generator_rating(self):
        return binary_to_int(self._oxygen_generator_rating)


def part_1():
    filepath = r"input.txt"
    nums = parse_input(filepath)
    sub_diagnostics = SubmarineDiagnostics(nums)
    return sub_diagnostics.power_consumption


def part_2():
    filepath = r"input.txt"
    nums = parse_input(filepath)
    sub_diagnostics = SubmarineDiagnostics(nums)
    return sub_diagnostics.life_support_rating


if __name__ == "__main__":
    print(part_1())
    print(part_2())
