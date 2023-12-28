from abc import ABCMeta, abstractmethod
from typing import ClassVar, List
from new_feature import FeatureName, Feature


class AbstractPlanPrice(metaclass=ABCMeta):
    @abstractmethod
    def get_plan_price(self) -> float:
        pass


class Plan0Price(AbstractPlanPrice):
    def get_plan_price(self) -> float:
        return 0


class Plan1Price(AbstractPlanPrice):
    def get_plan_price(self) -> float:
        return 1000


class Plan2Price(AbstractPlanPrice):
    def get_plan_price(self) -> float:
        return 2000


class Plan3Price(AbstractPlanPrice):
    def get_plan_price(self) -> float:
        return 3000


class Plan4Price(AbstractPlanPrice):
    def get_plan_price(self) -> float:
        return 4000


class Plan5Price(AbstractPlanPrice):
    def get_plan_price(self) -> float:
        return 5000


class AbstractFeature(metaclass=ABCMeta):
    @abstractmethod
    def get_features(self):
        pass


class FeaturePlan0(AbstractFeature):
    features = [
        Feature().set_feature_name(feature_name=FeatureName.REINSTALL).set_plan(plan=0),
        Feature().set_feature_name(feature_name=FeatureName.PARTNERS).set_plan(plan=0),
    ]

    def get_features(self):
        return self.features


class FeaturePlan1(AbstractFeature):
    features = [
        Feature().set_feature_name(feature_name=FeatureName.REINSTALL).set_plan(plan=1),
        Feature().set_feature_name(feature_name=FeatureName.PARTNERS).set_plan(plan=1),
        Feature().set_feature_name(feature_name=FeatureName.CALLBACK).set_plan(plan=1),
    ]

    def get_features(self):
        return self.features


class FeaturePlan2(AbstractFeature):
    features = [
        Feature().set_feature_name(feature_name=FeatureName.REINSTALL).set_plan(plan=2),
        Feature().set_feature_name(feature_name=FeatureName.PARTNERS).set_plan(plan=2),
        Feature().set_feature_name(feature_name=FeatureName.CALLBACK).set_plan(plan=2),
    ]

    def get_features(self):
        return self.features


class FeaturePlan3(AbstractFeature):
    features = [
        Feature().set_feature_name(feature_name=FeatureName.REINSTALL).set_plan(plan=3),
        Feature().set_feature_name(feature_name=FeatureName.PARTNERS).set_plan(plan=3),
        Feature().set_feature_name(feature_name=FeatureName.CALLBACK).set_plan(plan=3),
        Feature().set_feature_name(feature_name=FeatureName.UNINSTALL).set_plan(plan=3),
    ]

    def get_features(self):
        return self.features


class FeaturePlan4(AbstractFeature):
    features = [
        Feature().set_feature_name(feature_name=FeatureName.REINSTALL).set_plan(plan=4),
        Feature().set_feature_name(feature_name=FeatureName.PARTNERS).set_plan(plan=4),
        Feature().set_feature_name(feature_name=FeatureName.CALLBACK).set_plan(plan=4),
        Feature().set_feature_name(feature_name=FeatureName.UNINSTALL).set_plan(plan=4),
        Feature().set_feature_name(feature_name=FeatureName.S2S).set_plan(plan=4),
    ]

    def get_features(self):
        return self.features


class FeaturePlan5(AbstractFeature):
    features = [
        Feature().set_feature_name(feature_name=FeatureName.REINSTALL).set_plan(plan=5),
        Feature().set_feature_name(feature_name=FeatureName.PARTNERS).set_plan(plan=5),
        Feature().set_feature_name(feature_name=FeatureName.CALLBACK).set_plan(plan=5),
        Feature().set_feature_name(feature_name=FeatureName.UNINSTALL).set_plan(plan=5),
        Feature().set_feature_name(feature_name=FeatureName.REVENUE).set_plan(plan=5),
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
            extra_price_features += feature.get_feature_price

        return extra_price_features

    def get_extra_features_list(self) -> List[Feature]:
        all_features: List[Feature] = self.perform_feature()
        extra_features: List[Feature] = list()

        for feature in all_features:
            if feature.is_extra_feature is True:
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
    plan.add_feature(Feature().set_feature_name(feature_name=FeatureName.S2S).set_plan(plan=0).set_extra_feature())
    print(plan.perform_feature())
    print(plan.get_extra_features_price())
    print(plan.get_extra_features_list())
    print(plan)
