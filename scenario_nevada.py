import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import (ScenarioContainer, StaticTarget)


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        # Column south of KXTA
        StaticTarget(mpt.MPTarget.TOWER, g.Position(-116.2231, 35.6103, 187.6190),  91.4, 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-116.1486, 35.6125, 256.1100),  81.8, 0),
        StaticTarget(mpt.MPTarget.RADAR_STATION, g.Position(-116.0910, 35.6226, 378.3086),  77.3, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-116.0137, 35.6410, 624.9638),  59.7, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-115.9777, 35.7070, 1058.3224), 359.9, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-115.9812, 35.7704, 1482.2138), 356.8, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-115.9826, 35.8164, 900.6131),   3.5, 0),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(-115.9677, 35.9476, 860.4252),   5.5, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-115.9831, 36.0120, 765.9694), 315.4, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-115.9181, 36.5209, 1378.2810),  14.8, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-115.9284, 36.7877, 938.9772), 327.5, 0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(-115.9568, 37.1585, 1608.0141),  10.2, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-115.9413, 37.2441, 1381.5435),   8.7, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-115.9392, 37.2551, 1381.8207),   9.4, 0),
        StaticTarget(mpt.MPTarget.STRYKER_TANK, g.Position(-115.9367, 37.2668, 1384.3818),  10.1, 0),
        StaticTarget(mpt.MPTarget.DVINA, g.Position(-115.9326, 37.2841, 1388.4119),  11.3, 0),
        StaticTarget(mpt.MPTarget.BUFFALO_MINE, g.Position(-115.8449, 37.4857, 1729.6321),  45.6, 0),
        StaticTarget(mpt.MPTarget.BRADLEY_TANK, g.Position(-115.7405, 37.4832, 2307.9216), 162.6, 0),
        StaticTarget(mpt.MPTarget.MLRS_ROCKET_LAUNCHER, g.Position(-115.7258, 37.3511, 1990.4022), 202.6, 0),
        StaticTarget(mpt.MPTarget.M1_TANK, g.Position(-115.7330, 37.0683, 1801.5064), 173.5, 0),
    ]

    scenario = ScenarioContainer('nevada', 'Nevada',  'Cf. http://opredflag.com/forum_threads/3154248',
                                 (-116., 35), (-115., 38),
                                 'KXTA', None, 60)
    scenario.add_static_targets(static_targets)
    return scenario
