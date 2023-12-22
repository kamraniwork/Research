from abc import ABCMeta, abstractmethod
from typing import ClassVar, List
from new_feature import FeatureFactory, FeatureName, Feature


class AbstractPlanPrice(metaclass=ABCMeta):
    @abstractmethod
    def get_plan_price(self):
        pass


class AbstractFeature(metaclass=ABCMeta):
    @abstractmethod
    def get_features(self):
        pass


class Plan0Price(AbstractPlanPrice):
    def get_plan_price(self) -> float:
        return 0


class FeaturePlan0(AbstractFeature):
    features = [
        FeatureFactory.create_feature(feature_name=FeatureName.REINSTALL, plan=0),
        FeatureFactory.create_feature(feature_name=FeatureName.PARTNERS, plan=0),
    ]

    def get_features(self):
        return self.features


class Plan:
    def __init__(self, price: AbstractPlanPrice, feature: AbstractFeature):
        self._price = price
        self._feature = feature

    def perform_price(self):
        return self._price.get_plan_price()

    def perform_feature(self):
        return self._feature.get_features()

    def add_feature(self, feature: Feature):
        self._feature.get_features().append(feature)

    def get_extra_features_price(self):
        extra_features: List[Feature] = self.get_extra_features_list()
        extra_price_features: float = 0
        for feature in extra_features:
            extra_price_features += feature.perform_price()

        return extra_price_features

    def get_extra_features_list(self) -> List[Feature]:
        all_features: List[Feature] = self.perform_feature()
        extra_features: List[Feature] = list()

        for feature in all_features:
            if feature.feature_price.is_extra_feature is True:
                extra_features.append(feature)

        return extra_features

    def __str__(self):
        features_str = ", ".join(map(str, self.perform_feature()))
        return f"Plan with price: {self.perform_price()} and features: {features_str}"


class Plan0(Plan):
    def __init__(self):
        super().__init__(price=Plan0Price(), feature=FeaturePlan0())

    def __str__(self):
        return "Plan0"


if __name__ == "__main__":
    plan = Plan0()
    print(plan.perform_price())
    print(plan.perform_feature())
    plan.add_feature(FeatureFactory.create_feature(feature_name=FeatureName.S2S, plan=0, is_extra_feature=True))
    print(plan.perform_feature())
    print(plan.get_extra_features_price())
    print(plan.get_extra_features_list())
    print(plan)
