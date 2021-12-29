import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import (ScenarioContainer, StaticTarget)


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        # Event
        StaticTarget(mpt.MPTarget.TOWER, g.Position(-116.321, 33.259, 159.),  91.4, 0),#L08
        StaticTarget(mpt.MPTarget.TOWER, g.Position(-118.439, 35.135, 1207.), 324.8, 0),#KLSP
    ]

    scenario = ScenarioContainer('kittens', 'Kittens',  'Cf. http://opredflag.com/forum_threads/3154248',
                                 (-119., 35), (-115., 38),
                                 'KXTA', None, 60)
    scenario.add_static_targets(static_targets)
    return scenario
