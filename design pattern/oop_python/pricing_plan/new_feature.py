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


class Feature:
    def __init__(self):
        self.is_extra_feature: bool = False
        self.feature_name: str = str()
        self.plan: int = 0

    def set_feature_name(self, feature_name: FeatureName) -> "Feature":
        self.feature_name: str = feature_name.value
        return self

    def set_plan(self, plan: int) -> "Feature":
        self.plan: int = plan
        return self

    def set_extra_feature(self) -> "Feature":
        self.is_extra_feature: bool = True
        return self

    def __repr__(self) -> str:
        return self.feature_name

    @property
    def get_feature_price(self) -> float:
        return FeaturePriceManager.feature_prices[self.feature_name][f"plan{self.plan}"]
