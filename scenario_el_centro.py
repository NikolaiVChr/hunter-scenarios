# This scenario was automatically generated by tron2scenario.py
import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import ScenarioContainer, StaticTarget


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-113.96585, 32.523455, 284.226), 0, 1),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-114.13371833333333, 32.44497166666667, 272.923), 0, 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-113.96645333333333, 32.52565, 282.89), 0, 1),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(-113.96429166666667, 32.52499666666667, 280.999), 120.0, 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-113.96298333333333, 32.52525833333333, 279.541), 130.0, 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-113.96238010788758, 32.52583196061094, 277.32), 130.0, 0),
        StaticTarget(mpt.MPTarget.RADAR_STATION, g.Position(-115.39751666666666, 33.31332833333333, 155.366), 320.0, 0),
        StaticTarget(mpt.MPTarget.STRYKER_TANK, g.Position(-115.40205666666667, 33.31236166666667, 146.486), 0, 0),
        StaticTarget(mpt.MPTarget.STRYKER_TANK, g.Position(-115.40205166666667, 33.31185333333333, 145.736), 0, 0),
        StaticTarget(mpt.MPTarget.STRYKER_TANK, g.Position(-115.402035, 33.31152, 145.266), 0, 0),
        StaticTarget(mpt.MPTarget.STRYKER_TANK, g.Position(-115.40202166666667, 33.31118333333333, 144.785), 0, 0),
        StaticTarget(mpt.MPTarget.STRYKER_TANK, g.Position(-115.40197833333333, 33.310696666666665, 144.132), 0, 0),
        StaticTarget(mpt.MPTarget.HQ, g.Position(-115.397325, 33.31480666666667, 157.892), 0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40326666666667, 33.379221666666666, 348.138), 35.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40294666666667, 33.378636666666665, 346.501), 90.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40230166666667, 33.378433333333334, 346.555), 270.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40222833333333, 33.37816333333333, 345.838), 350.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.404515, 33.37934833333333, 347.573), 330.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40457833333333, 33.37887833333333, 345.719), 30.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40415, 33.37837, 344.511), 0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.403135, 33.377775, 343.788), 0.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40271166666666, 33.377575, 343.628), 0.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40213, 33.37728166666667, 343.354), 0.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40243166666667, 33.37697166666667, 342.143), 0.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40190833333334, 33.37751166666666, 344.252), 270.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40251666666667, 33.37799666666667, 345.058), 0.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40159333333334, 33.377985, 345.957), 240.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.40319833333334, 33.37824166666667, 345.09), 0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-113.96492833333333, 32.52450666666667, 281.588), 0, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-113.96365333333334, 32.524883333333335, 281.136), 160.0, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-113.96351166666666, 32.52495, 281.055), 160.0, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-113.96353833333333, 32.52476166666667, 281.282), 160.0, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-113.96335666666667, 32.52484833333333, 281.026), 160.0, 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(-113.96336833333334, 32.52466166666667, 281.402), 160.0, 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-113.96466666666667, 32.524076666666666, 282.104), 140.0, 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(-115.8585263639688, 32.92001995869601, 22.824), 90.0, 0),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(-115.43923166666667, 33.44363166666667, 570.456), 40.0, 1),
    ]
    scenario = ScenarioContainer('el_centro', 'El Centro NAF', 'El Centro NAF training complex', (-116.25, 32.44497166666667), (-113.96238010788758, 33.75), 'KNJK')
    scenario.add_static_targets(static_targets)
    return scenario
