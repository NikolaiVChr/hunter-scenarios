import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import (ScenarioContainer, StaticTarget)


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        # Column south of KXTA
        StaticTarget(mpt.MPTarget.TOWER, g.Position(35.6103, -116.2231, 187.6190),  91.4, 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(35.6125, -116.1486, 256.1100),  81.8, 0),
        StaticTarget(mpt.MPTarget.RADAR_STATION, g.Position(35.6226, -116.0910, 378.3086),  77.3, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(35.6410, -116.0137, 624.9638),  59.7, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(35.7070, -115.9777, 1058.3224), 359.9, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(35.7704, -115.9812, 1482.2138), 356.8, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(35.8164, -115.9826, 900.6131),   3.5, 0),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(35.9476, -115.9677, 860.4252),   5.5, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(36.0120, -115.9831, 765.9694), 315.4, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(36.5209, -115.9181, 1378.2810),  14.8, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(36.7877, -115.9284, 938.9772), 327.5, 0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(37.1585, -115.9568, 1608.0141),  10.2, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(37.2441, -115.9413, 1381.5435),   8.7, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(37.2551, -115.9392, 1381.8207),   9.4, 0),
        StaticTarget(mpt.MPTarget.STRYKER_TANK, g.Position(37.2668, -115.9367, 1384.3818),  10.1, 0),
        StaticTarget(mpt.MPTarget.DVINA, g.Position(37.2841, -115.9326, 1388.4119),  11.3, 0),
        StaticTarget(mpt.MPTarget.BUFFALO_MINE, g.Position(37.4857, -115.8449, 1729.6321),  45.6, 0),
        StaticTarget(mpt.MPTarget.BRADLEY_TANK, g.Position(37.4832, -115.7405, 2307.9216), 162.6, 0),
        StaticTarget(mpt.MPTarget.MLRS_ROCKET_LAUNCHER, g.Position(37.3511, -115.7258, 1990.4022), 202.6, 0),
        StaticTarget(mpt.MPTarget.M1_TANK, g.Position(37.0683, -115.7330, 1801.5064), 173.5, 0),
    ]

    scenario = ScenarioContainer('nevada', 'Nevada',  'Cf. http://opredflag.com/forum_threads/3154248',
                                 (35., -115.), (38., -117.),
                                 'KXTA', None, 60)
    scenario.add_static_targets(static_targets)
    return scenario
