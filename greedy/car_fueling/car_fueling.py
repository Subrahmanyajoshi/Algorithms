from typing import List


class CarFueling(object):

    @staticmethod
    def compute_min_refills(distance: int, tank: int, stops: List):
        remaining_tank = tank
        refuels = 0
        if stops[-1] != distance:
            stops.append(distance)

        for i in range(len(stops) - 1):
            dist_covered = stops[i] - stops[i - 1] if i != 0 else stops[i]
            remaining_tank -= dist_covered
            next_station = stops[i + 1] - stops[i]

            if next_station > tank:
                return -1

            if next_station > remaining_tank:
                remaining_tank = tank
                refuels += 1

        return refuels


if __name__ == '__main__':
    d = 950
    m = 400
    stops = [200, 375, 550, 750]

    # d, m, _, *stops = map(int, sys.stdin.read().split())
    print(CarFueling.compute_min_refills(distance=d, tank=m, stops=stops))
