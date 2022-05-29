
class SwapDetector(object):

    def __init__(self):
        self.array = [1, 2, 6, 4, 5, 3]

    def detect_swaps(self):
        x = y = None
        for i in range(len(self.array)-1):
            if self.array[i+1] < self.array[i]:
                y = self.array[i+1]

                if x is None:
                    x = self.array[i]
                else:
                    break

        return x, y


if __name__ == '__main__':
    print(SwapDetector().detect_swaps())
