import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import OPFOR_defaults, ScenarioContainer, StaticTarget


def build_scenario() -> ScenarioContainer:
    static_targets = [
        StaticTarget(mpt.MPTarget.RADAR_STATION, g.Position(19.31797133, 66.39282943, 742.4591), 16.0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(19.31513378, 66.39379173, 741.1738), 120.0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(19.31950926, 66.38849880, 692.8698), 144.0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(19.31904186, 66.38835333, 692.9743), 144.0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(19.31863179, 66.38822920, 690.5679), 144.0),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(19.30359813, 66.40229434, 622.5152), 144.0),
        StaticTarget(mpt.MPTarget.HANGAR, g.Position(19.31127886, 66.39751473, 670.2058), 48.0),
        StaticTarget(mpt.MPTarget.HANGAR, g.Position(19.31045241, 66.39787278, 667.6615), 48.0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(19.30464126, 66.40767511, 657.9343), -24.0),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(19.31605033, 66.39240587, 740.9106), -168.0),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(19.30184618, 66.40491959, 627.9796), -96.0),
        StaticTarget(mpt.MPTarget.WATER_TARGET, g.Position(19.54349283, 66.26228163, 476.9979), 72.0),
        StaticTarget(mpt.MPTarget.WATER_TARGET, g.Position(19.27394310, 66.35653929, 459.9960), 24.0),
        StaticTarget(mpt.MPTarget.HILL_TARGET, g.Position(19.40638195, 66.30230167, 644.1675), -168.0),
        StaticTarget(mpt.MPTarget.HILL_TARGET, g.Position(19.40369599, 66.30258359, 651.8440), -168.0),
        StaticTarget(mpt.MPTarget.HILL_TARGET, g.Position(19.40321754, 66.29985320, 660.307), -168.0),
        StaticTarget(mpt.MPTarget.CONTARGET, g.Position(19.20640023, 66.31270131, 589.7704), -96.0),
        StaticTarget(mpt.MPTarget.CONTARGET, g.Position(19.20908678, 66.31575506, 594.6803), -24.0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(19.20882646, 66.31381915, 592.3608), 0.0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(19.21143275, 66.31377540, 592.9721), 0.0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(19.21143915, 66.31202278, 590.7862), -52.0),
        StaticTarget(mpt.MPTarget.HARD_SHELTER, g.Position(19.21291479, 66.32204313, 606.6444), 0.0),
        StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(19.21634312, 66.32102837, 609.8731), 0.0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(19.21644677, 66.31984714, 609.7659), -88.0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(19.21643993, 66.31920160, 605.4502), -88.0),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(19.21058105, 66.32030831, 603.9304), 0.0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(19.20065322, 66.33814333, 638.4920), 96.0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(19.19668719, 66.33828890, 639.4189), -24.0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(19.19737021, 66.33849553, 638.9823), -24.0),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(19.19362982, 66.33854382, 633.8489), -24.0),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(19.19893407, 66.32989331, 616.1330), 120.0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(19.48019603, 66.25903261, 600.9570), 0.0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(19.46090564, 66.26839320, 658.0189), 0.0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(19.46517561, 66.26676383, 652.0435), 0.0),
        StaticTarget(mpt.MPTarget.FUEL_FARM, g.Position(19.46220665, 66.26716873, 658.5374), 24.0),
        StaticTarget(mpt.MPTarget.LIGHT_HANGAR, g.Position(19.47733422, 66.26138108, 618.4640), -72.0),
        StaticTarget(mpt.MPTarget.LIGHT_HANGAR, g.Position(19.47423907, 66.26184409, 628.6353), -72.0),
        StaticTarget(mpt.MPTarget.WAREHOUSE, g.Position(19.45869373, 66.25975203, 631.5842), -72.0),
        StaticTarget(mpt.MPTarget.WAREHOUSE, g.Position(19.45983429, 66.26061953, 635.0258), -72.0),
        StaticTarget(mpt.MPTarget.FACTORY, g.Position(19.46658283, 66.25928029, 625.5227), 12.0),
        StaticTarget(mpt.MPTarget.POWER_PLANT, g.Position(19.45015968, 66.26757949, 659.2291), 48.0),
    ]
    scenario = ScenarioContainer('vidsel', 'Vidsel test range', 'Vidsel test range',
                                 OPFOR_defaults,
                                 (18.0, 65.7), (20.5, 67.0),
                                 'ESNJ', 8.8, None, 60)
    scenario.add_static_targets(static_targets)
    return scenario
