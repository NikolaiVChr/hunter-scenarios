import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import OPFOR_defaults, ScenarioContainer, StaticTarget


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(24.9792, 70.0577, 7), 0, 2),
    ]
    scenario = ScenarioContainer('Testing', 'Testing',  '',
                                 OPFOR_defaults,
                                 (20., 69.5), (27., 71.5),
                                 'ENNA', 12.3, None, 60)
    scenario.add_static_targets(static_targets)
    return scenario
