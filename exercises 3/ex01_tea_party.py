"""A program to determine the cost of a tea party based on the number of guests."""

__author__: str = "730804613"


def main_planner(guests: int) -> None:
    """Function to determine cost of tea party"""
    print("A cozy tea party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Function to calculate the number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Function to calculate the number of treats needed"""
    return tea_bags(people) * 3 // 2


def cost(tea_count: int, treat_count: int) -> float:
    """Function to determine total cost of tea party"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
