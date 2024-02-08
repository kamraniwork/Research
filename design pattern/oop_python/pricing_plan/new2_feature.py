from abc import ABC, abstractmethod
from enum import Enum
from typing import ClassVar, Dict
from typing_extensions import Doc, Annotated


class FeatureName(Enum):
    REINSTALL = "reinstall"
    PARTNERS = "partners"
    REVENUE = "revenue"
    CALLBACK = "callback"
    UNINSTALL = "uninstall"
    DEEPLINK = "deeplink"
    S2S = "s2s"


class PlanName(Enum):
    Plan0 = 0
    Plan1 = 1
    Plan2 = 2
    Plan3 = 3
    Plan4 = 4
    Plan5 = 5

    __REVERSE_MAPPING__: Dict[int, str] = {
        0: "Plan0",
        1: "Plan1",
        2: "Plan2",
        3: "Plan3",
        4: "Plan4",
        5: "Plan5",
    }

    @classmethod
    def get(cls, name: int) -> str:
        return cls.__REVERSE_MAPPING__.get(name)


class PlanNamePrice(Enum):
    Plan0 = 0
    Plan1 = 1000
    Plan2 = 2000
    Plan3 = 3000
    Plan4 = 4000
    Plan5 = 5000

    @classmethod
    def get(cls, name: str) -> float | None:
        for x in cls:
            if x.name == name:
                return x.value

        return None


class FeaturePriceManager:
    feature_prices: ClassVar[Annotated[Dict[str, Dict[str, float]], Doc(
        """
        A dictionary mapping feature keys to their corresponding prices.
        Dict structure ==>
        {
            (feature_name str): {
                (plan_name str): (price_this_feature_in_plan int),
                ...
            },
            ...
        }
        """
    )]] = {
        FeatureName.REINSTALL.value: {
            "plan0": 1,
            "plan1": 10,
            "plan2": 100,
            "plan3": 1000,
            "plan4": 10000,
            "plan5": 100000,
        },
        FeatureName.PARTNERS.value: {
            "plan0": 2,
            "plan1": 11,
            "plan2": 110,
            "plan3": 1100,
            "plan4": 11000,
            "plan5": 110000,
        },
        FeatureName.REVENUE.value: {
            "plan0": 3,
            "plan1": 12,
            "plan2": 13,
            "plan3": 14,
            "plan4": 15,
            "plan5": 16,
        },
        FeatureName.CALLBACK.value: {
            "plan0": 4,
            "plan1": 13,
            "plan2": 14,
            "plan3": 15,
            "plan4": 16,
            "plan5": 17,
        },
        FeatureName.UNINSTALL.value: {
            "plan0": 5,
            "plan1": 14,
            "plan2": 15,
            "plan3": 16,
            "plan4": 17,
            "plan5": 18,
        },
        FeatureName.DEEPLINK.value: {
            "plan0": 6,
            "plan1": 15,
            "plan2": 16,
            "plan3": 17,
            "plan4": 18,
            "plan5": 19,
        },
        FeatureName.S2S.value: {
            "plan0": 7,
            "plan1": 16,
            "plan2": 17,
            "plan3": 18,
            "plan4": 19,
            "plan5": 20,
        }
    }


class Component(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def add_feature(self, feature: 'Component'):
        pass


class Feature(Component):
    def __init__(self, name: str, plan: int):
        self.name = name
        self.plan = plan

    def get_price(self) -> float:
        return FeaturePriceManager.feature_prices[self.name][f"plan{self.plan}"]

    def add_feature(self, feature: 'Component'):
        pass


class Plan(Component):
    def __init__(self, name: int):
        self.name = name
        self.features = []

    def add_feature(self, feature: 'Component'):
        self.features.append(feature)

    def get_price(self) -> float:
        plan_name = PlanName.get(name=self.name)
        return PlanNamePrice.get(name=plan_name)


class CompositePlan(Component):
    def __init__(self, name: str):
        self.name = name
        self.components = []

    def add_component(self, component: 'Component'):
        self.components.append(component)

    def get_price(self) -> float:
        total_price = sum(component.get_price() for component in self.components)
        return total_price

    def add_feature(self, feature: 'Component'):
        for component in self.components:
            component.add_feature(feature)


if __name__ == "__main__":
    # ایجاد فیچرها
    extra_feature = Feature(name="Extra Feature", price=50.0)
    premium_feature = Feature(name="Premium Feature", price=100.0)

    # ایجاد پلن‌ها
    basic_plan = Plan(name="Basic Plan")
    basic_plan.add_feature(extra_feature)

    premium_plan = Plan(name="Premium Plan")
    premium_plan.add_feature(extra_feature)
    premium_plan.add_feature(premium_feature)

    # ایجاد یک CompositePlan
    composite_plan = CompositePlan(name="Composite Plan")
    composite_plan.add_component(basic_plan)
    composite_plan.add_component(premium_plan)

    # اضافه کردن فیچر به Composite Plan
    composite_plan.add_feature(extra_feature)

    # محاسبه قیمت کل
    total_price = composite_plan.get_price()
    print(f"Total Price: {total_price}")
