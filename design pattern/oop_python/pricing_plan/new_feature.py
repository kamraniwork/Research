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


class FeaturePricePlan:
    def __init__(self, feature_name: str, plan: int, is_extra_feature: bool = False):
        self.feature_name: str = feature_name
        self.plan: int = plan
        self.is_extra_feature: bool = is_extra_feature

    def get_feature_price(self) -> float:
        return FeaturePriceManager.feature_prices[self.feature_name][f"plan{self.plan}"]


class FeatureFactory:
    @staticmethod
    def create_feature(feature_name: FeatureName, plan: int, is_extra_feature: bool = False) -> "Feature":
        feature_plan: FeaturePricePlan = FeaturePricePlan(feature_name.value, plan, is_extra_feature=is_extra_feature)
        return Feature(feature_plan)


class Feature:
    def __init__(self, feature_price: FeaturePricePlan):
        self.feature_price: FeaturePricePlan = feature_price

    def perform_price(self) -> float:
        return self.feature_price.get_feature_price()

    def __repr__(self):
        return self.feature_price.feature_name
