import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import ScenarioContainer, StaticTarget


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        StaticTarget(mpt.MPTarget.DVINA, g.Position(24.9792, 70.0577, 7), 0, 2),
        StaticTarget(mpt.MPTarget.M1_TANK, g.Position(24.9799, 70.0585, 7), 0, 2),
    ]
    scenario = ScenarioContainer('Testing', 'Testing',  '',
                                 (20., 69.5), (27., 71.5),
                                 'ENNA', None, 60)
    scenario.add_static_targets(static_targets)
    return scenario
