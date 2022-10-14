from components.tvs.smarttv import SmartTV
from components.tvs.tvhd import TVHD
from components.tvs.tvfullhd import TVFullHD
from components.tvs.tv4k import TV4K

__MAP_COMPONENTS_DICT__ = {
    "SmartTV": SmartTV,
    "TVHD": TVHD,
    "TVFullHD": TVFullHD,
    "TV4k": TV4K
}

class CreateComponents:
    def __init__(self, type_tv, _amount) -> None:
        self.type_tv = type_tv
        self._amount = _amount

    def create(self):
        return __MAP_COMPONENTS_DICT__[self.type_tv](self._amount, self.type_tv)
        
    