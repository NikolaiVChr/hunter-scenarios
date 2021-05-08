import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import ScenarioContainer, StaticTarget


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        StaticTarget(mpt.MPTarget.RADAR_STATION, g.Position(44.57241322, 40.17616257, 1343.4061), 312.0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(44.44050714, 40.12849988, 888.3779), 312.0, 1),
        StaticTarget(mpt.MPTarget.TOWER, g.Position(44.39579910, 40.14533647, 855.0697), 91.2),
        StaticTarget(mpt.MPTarget.RADAR_STATION, g.Position(44.56710058, 40.29689654, 1351.3494), 216.0),

        StaticTarget(mpt.MPTarget.DEPOT, g.Position(44.52005910, 40.80191240, 1415.3240), 168.0),
        StaticTarget(mpt.MPTarget.WAREHOUSE, g.Position(44.49295865, 40.81617438, 1307.8225), 76.0),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(44.51726290, 40.79210229, 1387.1468), 0.0),
        StaticTarget(mpt.MPTarget.BRIDGE, g.Position(44.49507787, 40.81573426, 1310.3151), 1.6),
        StaticTarget(mpt.MPTarget.HQ, g.Position(44.44110944, 40.83755432, 1387.2861), 268.0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(44.57084901, 40.78251061, 1702.7911), 0.0, 1),

        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(45.46095196, 40.17780984, 1917.0751), 0.0, 1),
        StaticTarget(mpt.MPTarget.S_300, g.Position(45.18958695, 40.27971637, 2021.5598), 0.0, 1),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(45.75087972, 40.17960826, 1977.7098), 0.0, 1),

        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(44.85904170, 39.68080877, 820.8468), 0.0, 1),
        StaticTarget(mpt.MPTarget.CHECKPOINT, g.Position(44.83915179, 39.71144901, 813.3471), 69.0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(44.69903495, 39.81048498, 812.2897), 0.0),

        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(45.15433004, 39.72076550, 967.2128), 0.0),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(45.08522124, 39.63377508, 885.2404), 240.0),
        StaticTarget(mpt.MPTarget.FACTORY, g.Position(45.10539653, 39.69182350, 938.0188), 352.0),
        StaticTarget(mpt.MPTarget.FUEL_FARM, g.Position(45.15632410, 39.72064390, 967.9493), 272.0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(45.16017899, 39.85386545, 2322.5837), 104.0),

        StaticTarget(mpt.MPTarget.TRUCK, g.Position(44.84040893, 39.70881589, 812.6038), 20.0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(44.84079339, 39.70799073, 813.5621), 20.0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(44.84117768, 39.70716755, 814.3620), 20.0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(44.84156342, 39.70634286, 813.7240), 20.0)

    ]
    scenario = ScenarioContainer('eastern_edge', 'Operation Eastern Edge',
                                 'OPRF event http://opredflag.com/events/941920?event_instance_id=16184118 ',
                                 (44.4, 39.6), (45.8, 40.9),
                                 'UBBN', None, 60)
    scenario.add_static_targets(static_targets)
    return scenario
