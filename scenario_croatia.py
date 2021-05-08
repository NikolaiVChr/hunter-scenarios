from typing import List, Tuple

import networkx as nx

import hunter.fg_targets as fgt
import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import (ScenarioContainer, StaticTarget, load_network,
                              CarrierDefinition, TankerDefinition, LIPA)


def _construct_croatia_grgurov_kanal_speedboat_track() -> nx.Graph:
    # island of Prvić
    wp_1 = g.WayPoint(1, 14.766, 44.9358, alt_m=0)
    wp_2 = g.WayPoint(2, 14.7934, 44.9315, alt_m=0)
    wp_3 = g.WayPoint(3, 14.8354, 44.9045, alt_m=0)
    wp_4 = g.WayPoint(4, 14.8412, 44.8814, alt_m=0)
    wp_5 = g.WayPoint(5, 14.7643, 44.9109, alt_m=0)
    # island of Sveti Grgur
    wp_11 = g.WayPoint(11, 14.7457, 44.8878, alt_m=0)
    wp_12 = g.WayPoint(12, 14.7895, 44.8618, alt_m=0)
    wp_13 = g.WayPoint(13, 14.7718, 44.8519, alt_m=0)
    wp_14 = g.WayPoint(14, 14.7391, 44.8609, alt_m=0)
    wp_15 = g.WayPoint(15, 14.7317, 44.8769, alt_m=0)
    wp_16 = g.WayPoint(16, 14.7424, 44.8773, alt_m=0)
    # island of Goli otok
    wp_21 = g.WayPoint(21, 14.7963, 44.8536, alt_m=0)
    wp_22 = g.WayPoint(22, 14.8426, 44.8495, alt_m=0)
    wp_23 = g.WayPoint(23, 14.8400, 44.8356, alt_m=0)
    wp_24 = g.WayPoint(24, 14.8293, 44.8305, alt_m=0)
    wp_25 = g.WayPoint(25, 14.8300, 44.8204, alt_m=0)
    wp_26 = g.WayPoint(26, 14.7993, 44.8411, alt_m=0)
    # island of Rab
    wp_41 = g.WayPoint(41, 14.7678, 44.8472, alt_m=0)
    wp_42 = g.WayPoint(42, 14.7574, 44.8218, alt_m=0)
    wp_43 = g.WayPoint(43, 14.7497, 44.8150, alt_m=0)
    wp_44 = g.WayPoint(44, 14.8295, 44.7590, alt_m=0)
    wp_45 = g.WayPoint(45, 14.8784, 44.7215, alt_m=0)
    wp_46 = g.WayPoint(46, 14.8514, 44.6901, alt_m=0)
    wp_47 = g.WayPoint(47, 14.7951, 44.7336, alt_m=0)
    wp_48 = g.WayPoint(48, 14.7647, 44.7467, alt_m=0)
    wp_49 = g.WayPoint(49, 14.7594, 44.7436, alt_m=0)
    wp_50 = g.WayPoint(50, 14.6889, 44.7560, alt_m=0)
    wp_51 = g.WayPoint(51, 14.6523, 44.7918, alt_m=0)
    wp_52 = g.WayPoint(52, 14.6935, 44.8232, alt_m=0)
    wp_53 = g.WayPoint(53, 14.6716, 44.8467, alt_m=0)
    wp_54 = g.WayPoint(54, 14.7373, 44.8574, alt_m=0)

    # Coast
    wp_61 = g.WayPoint(61, 14.8720, 44.8162, alt_m=0)  # Kladd
    wp_62 = g.WayPoint(62, 14.8761, 44.7925, alt_m=0)  # Starigrad
    wp_63 = g.WayPoint(63, 14.8792, 44.7129, alt_m=0)  # Stinica

    graph = nx.Graph()
    graph.add_nodes_from([wp_1, wp_2, wp_3, wp_4, wp_5,
                          wp_11, wp_12, wp_13, wp_14, wp_15, wp_16,
                          wp_21, wp_22, wp_23, wp_24, wp_25, wp_26,
                          wp_41, wp_42, wp_43, wp_44, wp_45, wp_46, wp_47, wp_48, wp_49,
                          wp_50, wp_51, wp_52, wp_53, wp_54,
                          wp_61, wp_62, wp_63])

    graph.add_edge(wp_1, wp_2)
    graph.add_edge(wp_2, wp_3)
    graph.add_edge(wp_3, wp_4)
    graph.add_edge(wp_4, wp_5)
    graph.add_edge(wp_5, wp_1)

    graph.add_edge(wp_11, wp_12)
    graph.add_edge(wp_12, wp_13)
    graph.add_edge(wp_13, wp_14)
    graph.add_edge(wp_14, wp_15)
    graph.add_edge(wp_15, wp_16)
    graph.add_edge(wp_16, wp_11)

    graph.add_edge(wp_21, wp_22)
    graph.add_edge(wp_22, wp_23)
    graph.add_edge(wp_23, wp_24)
    graph.add_edge(wp_24, wp_25)
    graph.add_edge(wp_25, wp_26)
    graph.add_edge(wp_26, wp_21)

    graph.add_edge(wp_5, wp_11)
    graph.add_edge(wp_4, wp_21)
    graph.add_edge(wp_12, wp_21)
    graph.add_edge(wp_13, wp_21)
    graph.add_edge(wp_13, wp_26)

    # Rab
    graph.add_edge(wp_41, wp_42)
    graph.add_edge(wp_42, wp_43)
    graph.add_edge(wp_43, wp_44)
    graph.add_edge(wp_44, wp_45)
    # not 45-46
    graph.add_edge(wp_45, wp_63)
    graph.add_edge(wp_63, wp_46)
    graph.add_edge(wp_46, wp_47)
    graph.add_edge(wp_47, wp_48)
    graph.add_edge(wp_48, wp_49)
    graph.add_edge(wp_49, wp_50)
    graph.add_edge(wp_50, wp_51)
    graph.add_edge(wp_51, wp_52)
    graph.add_edge(wp_52, wp_53)
    graph.add_edge(wp_53, wp_54)
    graph.add_edge(wp_54, wp_41)

    # coast and connections
    graph.add_edge(wp_61, wp_62)
    graph.add_edge(wp_62, wp_63)
    graph.add_edge(wp_45, wp_62)
    graph.add_edge(wp_23, wp_61)
    graph.add_edge(wp_25, wp_61)
    graph.add_edge(wp_14, wp_54)
    graph.add_edge(wp_13, wp_41)
    graph.add_edge(wp_26, wp_41)

    return graph


def _construct_sail_area_carrier_adria() -> List[Tuple[float, float]]:
    return [(13.66, 44.83),  # Pula
            (12.5, 44.5),  # Ravenna
            (13.6, 43.67),  # Ancona
            (14.35, 42.55),  # Pescara
            (16.0, 43.28)  # Split
            ]


def _construct_croatia_tanker(flight_level_m: float) -> nx.Graph:
    wp_1 = g.WayPoint(1, 13.43, 44.1, 0, flight_level_m)
    wp_2 = g.WayPoint(2, 14.17, 44.1, 0, flight_level_m)
    graph = nx.Graph()
    graph.add_nodes_from([wp_1, wp_2])
    graph.add_edge(wp_1, wp_2)
    return graph


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(15.45134603, 45.12084095, 315.22), 190),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(15.47817711, 45.15597383, 278.89), 225),
        StaticTarget(mpt.MPTarget.CHECKPOINT, g.Position(15.46642110, 45.15227261, 258.38), 0),
        StaticTarget(mpt.MPTarget.CONTARGET, g.Position(15.35403661, 45.17658397, 415.64), 350),
        StaticTarget(mpt.MPTarget.CONTARGET, g.Position(15.35605100, 45.17734675, 407.75), 350),
        StaticTarget(mpt.MPTarget.CONTARGET, g.Position(15.35764889, 45.17402033, 461.74), 350),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(15.44395520, 45.13041282, 285.39), 105),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(15.44569273, 45.13307877, 281.03), 105),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(15.43930508, 45.13526179, 285.17), 105),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(15.43756785, 45.13230291, 295.75), 105),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(15.47054590, 45.14772888, 259.03), 121),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.48843116, 45.13102892, 279.85), 330),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.48885112, 45.13049413, 280.77), 330),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.48919529, 45.13005391, 281.47), 330),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.48958546, 45.12957522, 280.956), 330),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(15.48677027, 45.08705502, 374.29), 24),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.49388525, 45.09844544, 279.30), 60),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.49090056, 45.09978517, 284.96), 60),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.48753297, 45.10134146, 293.71), 60),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.48461009, 45.10268827, 289.39), 60),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(15.49277869, 45.11349851, 282.90), 70),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(15.48581480, 45.11163144, 286.13), 70),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(15.48928243, 45.11853318, 282.78), 70),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(15.48252808, 45.11650189, 293.97), 70),
        StaticTarget(mpt.MPTarget.S_300, g.Position(15.54694001, 45.05560442, 389.95), 32),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(15.48643459, 45.15477019, 358.81), 336),
        StaticTarget(mpt.MPTarget.S_300, g.Position(15.42062364, 45.18303639, 298.64), 4),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(15.46957855, 45.11545707, 364.92), 310),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(15.44195858, 45.17045487, 255.98), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(15.46779326, 45.13225982, 300.97), 265),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.50651187, 45.10753776, 275.17), 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.50637840, 45.10665494, 277.76), 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.50528944, 45.10668555, 280.64), 0),
        StaticTarget(mpt.MPTarget.TRUCK, g.Position(15.50540209, 45.10758750, 278.06), 0),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(15.52031985, 45.09005467, 274.88), 336),
        StaticTarget(mpt.MPTarget.COMPOUND, g.Position(15.52174861, 45.08477434, 288.44), 336),
        StaticTarget(mpt.MPTarget.CONTARGET, g.Position(15.56593041, 45.05902512, 427.084), 30),
        StaticTarget(mpt.MPTarget.CONTARGET, g.Position(15.56397648, 45.06171625, 444.30), 30),
        StaticTarget(mpt.MPTarget.CONTARGET, g.Position(15.46176065, 45.10051699, 495.03), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(15.51104405, 45.11098530, 263.94), 240),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(15.52441082, 45.06357041, 528.66), 48),
        StaticTarget(mpt.MPTarget.SHILKA, g.Position(15.53218093, 45.09672772, 299.10), 144),
        # lake / sump at South-West corner just a bit outside
        StaticTarget(mpt.MPTarget.WATER_TARGET, g.Position(15.4052, 45.0218, 484), 80),
        StaticTarget(mpt.MPTarget.WATER_TARGET, g.Position(15.4058, 45.0181, 484), 260),
        StaticTarget(mpt.MPTarget.WATER_TARGET, g.Position(15.4136, 45.0162, 485), 180),
        StaticTarget(mpt.MPTarget.HILL_TARGET, g.Position(15.4246, 45.0212, 607), 60),
        StaticTarget(mpt.MPTarget.HILL_TARGET, g.Position(15.4239, 45.0224, 617), 60)
    ]
    speedboat_graph = _construct_croatia_grgurov_kanal_speedboat_track()
    origin_1 = g.Position(14.766, 44.9358)  # WP_1
    speedboat_1 = mpt.MPTargetTrips.create_random_target(mpt.MPTarget.SPEEDBOAT, speedboat_graph, origin_1,
                                                         mpt.MPTargetTrips.STATIC_HP, 5, 10000, 0)
    origin_2 = g.Position(14.8300, 44.8204)  # WP_25
    speedboat_2 = mpt.MPTargetTrips.create_random_target(mpt.MPTarget.SPEEDBOAT, speedboat_graph, origin_2,
                                                         mpt.MPTargetTrips.STATIC_HP, 5, 10000, 0)

    # a convoy of trucks close to Slunj at Glavicica
    # road_network.py: -f TEST/params.py -b *15.526_45.106_15.545_45.122 -o croatia_glavicica_roads.pkl -s
    convoy_graph = load_network('croatia_glavicica_roads.pkl', path)
    origin_trip_convoy = g.Position(15.5429, 45.1121)  # helicopter North-West
    dests_convoy = [g.Position(15.5320, 45.1098),
                    g.Position(15.5281, 45.1125),
                    g.Position(15.5335, 45.1171)  # Glavicica
                    ]
    convoy = mpt.MPTargetTrips.create_routed_convoy_targets(mpt.MPTarget.TRUCK,
                                                            convoy_graph, origin_trip_convoy,
                                                            mpt.MPTargetTrips.STATIC_HP, 5, dests_convoy, True,
                                                            30, 3, 2)

    trip_targets = [speedboat_1, speedboat_2]
    trip_targets.extend(convoy)

    vinson_carrier = CarrierDefinition(fgt.CarrierType.vinson, _construct_sail_area_carrier_adria(), (14.25, 44.0))

    tanker = TankerDefinition(LIPA, _construct_croatia_tanker(g.feet_to_metres(20000)))

    scenario = ScenarioContainer('croatia', 'Eugen Kvaternik', 'Croatian Military Range near Slunj',
                                 (14.5, 44.625), (15.75, 45.25),
                                 'LDRI', None, 60)
    scenario.add_static_targets(static_targets)
    scenario.add_targets_with_trips(trip_targets)
    scenario.add_carrier(vinson_carrier)
    scenario.add_tanker(tanker)
    return scenario
