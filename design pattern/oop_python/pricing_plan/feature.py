from abc import ABCMeta, abstractmethod
from typing import Dict, ClassVar


class AbstractFeaturePricePlan(metaclass=ABCMeta):

    def __init__(self, feature_name: str):
        self.feature_name = feature_name

    @abstractmethod
    def get_feature_price(self) -> float:
        pass

    def get_name(self):
        return self.feature_name


class FeaturePricePlan0(AbstractFeaturePricePlan):
    feature_price: ClassVar[Dict[str, float]] = {
        "reinstall": 1,
        "partners": 2,
    }

    def __init__(self, feature_name: str):
        super().__init__(feature_name=feature_name)

    def get_feature_price(self) -> float:
        return self.feature_price.get(self.feature_name)


class FeaturePricePlan1(AbstractFeaturePricePlan):
    feature_price: ClassVar[Dict[str, float]] = {
        "reinstall": 10,
        "partners": 11,
        "revenue": 12,
    }

    def __init__(self, feature_name: str):
        super().__init__(feature_name=feature_name)

    def get_feature_price(self) -> float:
        return self.feature_price.get(self.feature_name)


class FeaturePricePlan2(AbstractFeaturePricePlan):
    feature_price: ClassVar[Dict[str, float]] = {
        "reinstall": 100,
        "partners": 110,
        "revenue": 120,
        "callback": 130
    }

    def __init__(self, feature_name: str):
        super().__init__(feature_name=feature_name)

    def get_feature_price(self) -> float:
        return self.feature_price.get(self.feature_name)


class FeaturePricePlan3(AbstractFeaturePricePlan):
    feature_price: ClassVar[Dict[str, float]] = {
        "reinstall": 1000,
        "partners": 1100,
        "revenue": 1200,
        "callback": 1300,
        "uninstall": 1400,
    }

    def __init__(self, feature_name: str):
        super().__init__(feature_name=feature_name)

    def get_feature_price(self) -> float:
        return self.feature_price.get(self.feature_name)


class FeaturePricePlan4(AbstractFeaturePricePlan):
    feature_price: ClassVar[Dict[str, float]] = {
        "reinstall": 10000,
        "partners": 11000,
        "revenue": 12000,
        "callback": 13000,
        "uninstall": 14000,
        "deeplink": 15000,
    }

    def __init__(self, feature_name: str):
        super().__init__(feature_name=feature_name)

    def get_feature_price(self) -> float:
        return self.feature_price.get(self.feature_name)


class FeaturePricePlan5(AbstractFeaturePricePlan):
    feature_price: ClassVar[Dict[str, float]] = {
        "reinstall": 100000,
        "partners": 110000,
        "revenue": 120000,
        "callback": 130000,
        "uninstall": 140000,
        "deeplink": 150000,
        "s2s": 160000
    }

    def __init__(self, feature_name: str):
        super().__init__(feature_name=feature_name)

    def get_feature_price(self) -> float:
        return self.feature_price.get(self.feature_name)


class Feature:
    def __init__(self, feature_price: AbstractFeaturePricePlan):
        self.feature_price = feature_price

    def perform_price(self) -> float:
        return self.feature_price.get_feature_price()


# ==============================================================
class ReinstallFeaturePlan0(Feature):
    feature_price: ClassVar[FeaturePricePlan0] = FeaturePricePlan0(feature_name="reinstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "reinstall"


class ReinstallFeaturePlan1(Feature):
    feature_price: ClassVar[FeaturePricePlan1] = FeaturePricePlan1(feature_name="reinstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "reinstall"


class ReinstallFeaturePlan2(Feature):
    feature_price: ClassVar[FeaturePricePlan2] = FeaturePricePlan2(feature_name="reinstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "reinstall"


class ReinstallFeaturePlan3(Feature):
    feature_price: ClassVar[FeaturePricePlan3] = FeaturePricePlan3(feature_name="reinstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "reinstall"


class ReinstallFeaturePlan4(Feature):
    feature_price: ClassVar[FeaturePricePlan4] = FeaturePricePlan4(feature_name="reinstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "reinstall"


class ReinstallFeaturePlan5(Feature):
    feature_price: ClassVar[FeaturePricePlan5] = FeaturePricePlan5(feature_name="reinstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "reinstall"


# ==============================================================
class PartnersFeaturePlan0(Feature):
    feature_price: ClassVar[FeaturePricePlan0] = FeaturePricePlan0(feature_name="partners")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "partners"


class PartnersFeaturePlan1(Feature):
    feature_price: ClassVar[FeaturePricePlan1] = FeaturePricePlan1(feature_name="partners")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "partners"


class PartnersFeaturePlan2(Feature):
    feature_price: ClassVar[FeaturePricePlan2] = FeaturePricePlan2(feature_name="partners")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "partners"


class PartnersFeaturePlan3(Feature):
    feature_price: ClassVar[FeaturePricePlan3] = FeaturePricePlan3(feature_name="partners")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "partners"


class PartnersFeaturePlan4(Feature):
    feature_price: ClassVar[FeaturePricePlan4] = FeaturePricePlan4(feature_name="partners")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "partners"


class PartnersFeaturePlan5(Feature):
    feature_price: ClassVar[FeaturePricePlan5] = FeaturePricePlan5(feature_name="partners")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "partners"


# ==============================================================
class RevenueFeaturePlan0(Feature):
    feature_price: ClassVar[FeaturePricePlan0] = FeaturePricePlan0(feature_name="revenue")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "revenue"


class RevenueFeaturePlan1(Feature):
    feature_price: ClassVar[FeaturePricePlan1] = FeaturePricePlan1(feature_name="revenue")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "revenue"


class RevenueFeaturePlan2(Feature):
    feature_price: ClassVar[FeaturePricePlan2] = FeaturePricePlan2(feature_name="revenue")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "revenue"


class RevenueFeaturePlan3(Feature):
    feature_price: ClassVar[FeaturePricePlan3] = FeaturePricePlan3(feature_name="revenue")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "revenue"


class RevenueFeaturePlan4(Feature):
    feature_price: ClassVar[FeaturePricePlan4] = FeaturePricePlan4(feature_name="revenue")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "revenue"


class RevenueFeaturePlan5(Feature):
    feature_price: ClassVar[FeaturePricePlan5] = FeaturePricePlan5(feature_name="revenue")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "revenue"


# ==============================================================
class CallbackFeaturePlan0(Feature):
    feature_price: ClassVar[FeaturePricePlan0] = FeaturePricePlan0(feature_name="callback")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "callback"


class CallbackFeaturePlan1(Feature):
    feature_price: ClassVar[FeaturePricePlan1] = FeaturePricePlan1(feature_name="callback")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "callback"


class CallbackFeaturePlan2(Feature):
    feature_price: ClassVar[FeaturePricePlan2] = FeaturePricePlan2(feature_name="callback")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "callback"


class CallbackFeaturePlan3(Feature):
    feature_price: ClassVar[FeaturePricePlan3] = FeaturePricePlan3(feature_name="callback")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "callback"


class CallbackFeaturePlan4(Feature):
    feature_price: ClassVar[FeaturePricePlan4] = FeaturePricePlan4(feature_name="callback")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "callback"


class CallbackFeaturePlan5(Feature):
    feature_price: ClassVar[FeaturePricePlan5] = FeaturePricePlan5(feature_name="callback")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "callback"


# ==============================================================
class UninstallFeaturePlan0(Feature):
    feature_price: ClassVar[FeaturePricePlan0] = FeaturePricePlan0(feature_name="uninstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "uninstall"


class UninstallFeaturePlan1(Feature):
    feature_price: ClassVar[FeaturePricePlan1] = FeaturePricePlan1(feature_name="uninstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "uninstall"


class UninstallFeaturePlan2(Feature):
    feature_price: ClassVar[FeaturePricePlan2] = FeaturePricePlan2(feature_name="uninstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "uninstall"


class UninstallFeaturePlan3(Feature):
    feature_price: ClassVar[FeaturePricePlan3] = FeaturePricePlan3(feature_name="uninstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "uninstall"


class UninstallFeaturePlan4(Feature):
    feature_price: ClassVar[FeaturePricePlan4] = FeaturePricePlan4(feature_name="uninstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "uninstall"


class UninstallFeaturePlan5(Feature):
    feature_price: ClassVar[FeaturePricePlan5] = FeaturePricePlan5(feature_name="uninstall")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "uninstall"


# ==============================================================
class DeeplinkFeaturePlan0(Feature):
    feature_price: ClassVar[FeaturePricePlan0] = FeaturePricePlan0(feature_name="deeplink")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "deeplink"


class DeeplinkFeaturePlan1(Feature):
    feature_price: ClassVar[FeaturePricePlan1] = FeaturePricePlan1(feature_name="deeplink")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "deeplink"


class DeeplinkFeaturePlan2(Feature):
    feature_price: ClassVar[FeaturePricePlan2] = FeaturePricePlan2(feature_name="deeplink")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "deeplink"


class DeeplinkFeaturePlan3(Feature):
    feature_price: ClassVar[FeaturePricePlan3] = FeaturePricePlan3(feature_name="deeplink")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "deeplink"


class DeeplinkFeaturePlan4(Feature):
    feature_price: ClassVar[FeaturePricePlan4] = FeaturePricePlan4(feature_name="deeplink")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "deeplink"


class DeeplinkFeaturePlan5(Feature):
    feature_price: ClassVar[FeaturePricePlan5] = FeaturePricePlan5(feature_name="deeplink")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "deeplink"


# ==============================================================
class S2SFeaturePlan0(Feature):
    feature_price: ClassVar[FeaturePricePlan0] = FeaturePricePlan0(feature_name="s2s")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "s2s"


class S2SFeaturePlan1(Feature):
    feature_price: ClassVar[FeaturePricePlan1] = FeaturePricePlan1(feature_name="s2s")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "s2s"


class S2SFeaturePlan2(Feature):
    feature_price: ClassVar[FeaturePricePlan2] = FeaturePricePlan2(feature_name="s2s")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "s2s"


class S2SFeaturePlan3(Feature):
    feature_price: ClassVar[FeaturePricePlan3] = FeaturePricePlan3(feature_name="s2s")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "s2s"


class S2SFeaturePlan4(Feature):
    feature_price: ClassVar[FeaturePricePlan4] = FeaturePricePlan4(feature_name="s2s")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "s2s"


class S2SFeaturePlan5(Feature):
    feature_price: ClassVar[FeaturePricePlan5] = FeaturePricePlan5(feature_name="s2s")

    def __init__(self):
        super().__init__(feature_price=self.feature_price)

    def __repr__(self):
        return "s2s"
