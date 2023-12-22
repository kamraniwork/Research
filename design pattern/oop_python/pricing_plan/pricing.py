from abc import ABCMeta, abstractmethod
from typing import ClassVar, override


class AbstractPlanPrice(metaclass=ABCMeta):
    @abstractmethod
    def get_plan_price(self):
        pass


class AbstractFeature(metaclass=ABCMeta):
    @abstractmethod
    def get_features(self):
        pass


class Plan0Price(AbstractPlanPrice):
    def get_plan_price(self):
        return 0


class Plan1Price(AbstractPlanPrice):
    def get_plan_price(self):
        return 10


class Plan2Price(AbstractPlanPrice):
    def get_plan_price(self):
        return 20


class Plan3Price(AbstractPlanPrice):
    def get_plan_price(self):
        return 30


class Plan4Price(AbstractPlanPrice):
    def get_plan_price(self):
        return 40


class Plan5Price(AbstractPlanPrice):
    def get_plan_price(self):
        return 50


from feature import (
    ReinstallFeaturePlan0, PartnersFeaturePlan0,
    ReinstallFeaturePlan1, PartnersFeaturePlan1, RevenueFeaturePlan1,
    ReinstallFeaturePlan2, PartnersFeaturePlan2, RevenueFeaturePlan2, CallbackFeaturePlan2,
    ReinstallFeaturePlan3, PartnersFeaturePlan3, RevenueFeaturePlan3, CallbackFeaturePlan3, UninstallFeaturePlan3,
    ReinstallFeaturePlan4, PartnersFeaturePlan4, RevenueFeaturePlan4, CallbackFeaturePlan4, UninstallFeaturePlan4,
    DeeplinkFeaturePlan4,
    ReinstallFeaturePlan5, PartnersFeaturePlan5, RevenueFeaturePlan5, CallbackFeaturePlan5, UninstallFeaturePlan5,
    DeeplinkFeaturePlan5, S2SFeaturePlan5,
    Feature)


class FeaturePlan0(AbstractFeature):
    def get_features(self):
        return [ReinstallFeaturePlan0(), PartnersFeaturePlan0()]


class FeaturePlan1(AbstractFeature):
    def get_features(self):
        return [ReinstallFeaturePlan1(), PartnersFeaturePlan1(), RevenueFeaturePlan1()]


class FeaturePlan2(AbstractFeature):
    def get_features(self):
        return [ReinstallFeaturePlan2(), PartnersFeaturePlan2(), RevenueFeaturePlan2(), CallbackFeaturePlan2]


class FeaturePlan3(AbstractFeature):
    def get_features(self):
        return [ReinstallFeaturePlan3(), PartnersFeaturePlan3(), RevenueFeaturePlan3(), CallbackFeaturePlan3,
                UninstallFeaturePlan3]


class FeaturePlan4(AbstractFeature):
    def get_features(self):
        return [ReinstallFeaturePlan4(), PartnersFeaturePlan4(), RevenueFeaturePlan4(), CallbackFeaturePlan4,
                UninstallFeaturePlan4, DeeplinkFeaturePlan4]


class FeaturePlan5(AbstractFeature):
    def get_features(self):
        return [ReinstallFeaturePlan5(), PartnersFeaturePlan5(), RevenueFeaturePlan5(), CallbackFeaturePlan5(),
                UninstallFeaturePlan5, DeeplinkFeaturePlan5, S2SFeaturePlan5]


class Plan:
    def __init__(self, price: AbstractPlanPrice, feature: AbstractFeature):
        self.price = price
        self.feature = feature

    def perform_price(self):
        return self.price.get_plan_price()

    def perform_feature(self):
        return self.feature.get_features()

    def set_feature(self, feature: Feature):
        return self.feature.get_features().append(feature)

    @staticmethod
    def get_plan_name():
        print("plan")


class Plan0(Plan):
    price: ClassVar[Plan0Price] = Plan0Price()
    feature: ClassVar[FeaturePlan0] = FeaturePlan0()

    def __init__(self):
        super().__init__(price=self.price, feature=self.feature)

    @override
    def get_plan_name(self):
        print("plan0")


if __name__ == "__main__":
    plan = Plan0()
    print(plan.perform_price())
    print(plan.perform_feature())
    plan.get_plan_name()
