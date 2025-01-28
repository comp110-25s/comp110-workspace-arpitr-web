"""To calculate things needed"""

__author__: str = "730698517"


def main_planner(guests: int) -> None:
    """to calculate eveyrhting"""
    print("A cozy tea party for " + str(guests) + " people")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """To calculate teabags"""
    return 2 * people


def treats(people: int) -> int:
    """To calculate treats"""
    return int(1.5 * (tea_bags(people=people)))


def cost(tea_count: int, treat_count: int) -> float:
    """to calculate cost of party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
