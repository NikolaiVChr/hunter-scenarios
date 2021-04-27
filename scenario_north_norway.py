from typing import List, Tuple

import networkx as nx

import hunter.fg_targets as fgt
import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import (OPFOR_defaults, ScenarioContainer, StaticTarget, CarrierDefinition, TankerDefinition,
                              AutomatTarget, AutomatType, ENTC,
                              default_ships_list, default_helis_list, default_drones_list)


def _construct_north_norway_ship(above_ground_m: float) -> nx.Graph:
    # Stjernøya
    wp_0 = g.WayPoint(0, 23.052063, 70.226493)
    wp_1 = g.WayPoint(1, 23., 70.325906)
    wp_2 = g.WayPoint(2, 22.841263, 70.357091)
    wp_3 = g.WayPoint(3, 22.785645, 70.402051)
    wp_4 = g.WayPoint(4, 22.532272, 70.391224)
    wp_5 = g.WayPoint(5, 22.312546, 70.345084)
    wp_6 = g.WayPoint(6, 22.397003, 70.280546)
    wp_7 = g.WayPoint(7, 22.60437, 70.242747)
    # from Stjernøya to ALTA
    wp_101 = g.WayPoint(101, 23.0809, 70.0688)
    wp_102 = g.WayPoint(102, 23.1729, 69.9793)
    wp_103 = g.WayPoint(103, 23.3116, 70.0173)

    # Seiland
    wp_8 = g.WayPoint(8, 23.118668, 70.249013)
    wp_9 = g.WayPoint(9, 23.343201, 70.291896)
    wp_10 = g.WayPoint(10, 23.681030, 70.445764)
    wp_11 = g.WayPoint(11, 23.598633, 70.586613)
    wp_12 = g.WayPoint(12, 23.584213, 70.601898)
    wp_13 = g.WayPoint(13, 23.6075559, 70.628563)
    wp_14 = g.WayPoint(14, 23.349380, 70.637216)
    wp_15 = g.WayPoint(15, 23.047256, 70.541373)
    wp_16 = g.WayPoint(16, 22.767105, 70.419778)

    # Sørøya
    wp_17 = g.WayPoint(17, 22.76878, 70.500000)
    wp_18 = g.WayPoint(18, 22.50000, 70.484337)
    wp_19 = g.WayPoint(19, 22.22122, 70.472405)

    # Silda
    wp_20 = g.WayPoint(20, 21.953430, 70.352935)
    wp_21 = g.WayPoint(21, 21.708298, 70.399057)
    wp_22 = g.WayPoint(22, 21.566162, 70.353397)
    wp_23 = g.WayPoint(23, 21.684952, 70.256437)
    wp_24 = g.WayPoint(24, 21.739197, 70.261771)

    # Northern part of Sørøya inkl. Rolvsøya
    wp_110 = g.WayPoint(110, 23.5, 70.75)
    wp_111 = g.WayPoint(111, 24., 70.75)
    wp_112 = g.WayPoint(112, 24., 70.875)
    wp_113 = g.WayPoint(113, 23.5821, 70.9113)
    wp_114 = g.WayPoint(114, 24.5, 71.)
    wp_115 = g.WayPoint(115, 24.5, 71.125)
    wp_116 = g.WayPoint(116, 23.7, 71.125)
    wp_117 = g.WayPoint(117, 23., 70.875)

    # North-Western part of Sørøya
    wp_118 = g.WayPoint(118, 22.5, 70.75)
    wp_119 = g.WayPoint(119, 22., 70.6790)
    wp_120 = g.WayPoint(120, 21.8806, 70.625)
    wp_121 = g.WayPoint(121, 22., 70.4377)
    wp_122 = g.WayPoint(122, 22.1498, 70.5761)
    wp_123 = g.WayPoint(123, 21.9616, 70.5742)
    wp_124 = g.WayPoint(124, 22.7362, 70.6608)
    wp_125 = g.WayPoint(125, 22.6263, 70.75)

    graph = nx.Graph()
    graph.add_nodes_from([wp_0, wp_1, wp_2, wp_3, wp_4, wp_5, wp_6, wp_7,
                          wp_101, wp_102, wp_103,
                          wp_8, wp_9, wp_10, wp_11, wp_12, wp_13, wp_14, wp_15, wp_16,
                          wp_17, wp_18, wp_19,
                          wp_20, wp_21, wp_22, wp_23, wp_24,
                          wp_110, wp_111, wp_112, wp_113, wp_114, wp_115, wp_116, wp_117,
                          wp_118, wp_119, wp_120, wp_121, wp_122, wp_123, wp_124, wp_125])
    for wp in graph.nodes:
        wp.alt_m = wp.ground_m + above_ground_m
        wp.is_point_of_interest = True

    # Stjernøya
    graph.add_edge(wp_0, wp_1)
    graph.add_edge(wp_1, wp_2)
    graph.add_edge(wp_2, wp_3)
    graph.add_edge(wp_3, wp_4)
    graph.add_edge(wp_4, wp_5)
    graph.add_edge(wp_5, wp_6)
    graph.add_edge(wp_6, wp_7)
    graph.add_edge(wp_7, wp_0)
    # Stjernøya to Alta
    graph.add_edge(wp_0, wp_101)
    graph.add_edge(wp_101, wp_102)
    graph.add_edge(wp_102, wp_103)
    graph.add_edge(wp_103, wp_101)
    # Seiland
    graph.add_edge(wp_0, wp_8)
    graph.add_edge(wp_1, wp_8)
    graph.add_edge(wp_8, wp_9)
    graph.add_edge(wp_9, wp_10)
    graph.add_edge(wp_10, wp_11)
    graph.add_edge(wp_11, wp_12)
    graph.add_edge(wp_12, wp_13)
    graph.add_edge(wp_13, wp_14)
    graph.add_edge(wp_14, wp_15)
    graph.add_edge(wp_15, wp_16)
    graph.add_edge(wp_16, wp_3)
    graph.add_edge(wp_16, wp_4)
    # Sørøya
    graph.add_edge(wp_15, wp_17)
    graph.add_edge(wp_17, wp_18)
    graph.add_edge(wp_18, wp_19)
    graph.add_edge(wp_17, wp_16)
    graph.add_edge(wp_18, wp_4)
    graph.add_edge(wp_18, wp_5)
    graph.add_edge(wp_18, wp_16)
    graph.add_edge(wp_19, wp_5)
    # Silda
    graph.add_edge(wp_19, wp_20)
    graph.add_edge(wp_19, wp_21)
    graph.add_edge(wp_20, wp_21)
    graph.add_edge(wp_21, wp_22)
    graph.add_edge(wp_22, wp_23)
    graph.add_edge(wp_23, wp_24)
    graph.add_edge(wp_24, wp_20)
    graph.add_edge(wp_20, wp_5)
    graph.add_edge(wp_20, wp_6)
    # Northern part of Sørøya inkl. Rolvsøya
    graph.add_edge(wp_13, wp_110)
    graph.add_edge(wp_14, wp_110)
    graph.add_edge(wp_110, wp_111)
    graph.add_edge(wp_111, wp_112)
    graph.add_edge(wp_112, wp_114)
    graph.add_edge(wp_114, wp_115)
    graph.add_edge(wp_115, wp_116)
    graph.add_edge(wp_116, wp_117)
    graph.add_edge(wp_110, wp_112)
    graph.add_edge(wp_110, wp_113)
    graph.add_edge(wp_112, wp_113)
    graph.add_edge(wp_113, wp_117)
    # North-Western part of Sørøya
    graph.add_edge(wp_117, wp_118)
    graph.add_edge(wp_118, wp_119)
    graph.add_edge(wp_119, wp_120)
    graph.add_edge(wp_120, wp_121)
    graph.add_edge(wp_121, wp_19)
    graph.add_edge(wp_121, wp_21)
    graph.add_edge(wp_121, wp_122)
    graph.add_edge(wp_122, wp_123)
    graph.add_edge(wp_123, wp_120)
    graph.add_edge(wp_118, wp_124)
    graph.add_edge(wp_124, wp_125)
    graph.add_edge(wp_118, wp_125)
    graph.add_edge(wp_117, wp_125)

    return graph


def _construct_north_norway_heli(above_ground_m: float) -> nx.Graph:
    # Kvaløya
    wp_1 = g.WayPoint(1, 23.8966, 70.5)
    wp_2 = g.WayPoint(2, 24., 70.5175)
    wp_3 = g.WayPoint(3, 24.1768, 70.625)
    wp_4 = g.WayPoint(4, 23.9501, 70.75)
    wp_5 = g.WayPoint(5, 23.5, 70.75)
    wp_6 = g.WayPoint(6, 23.5753, 70.625)
    wp_7 = g.WayPoint(7, 23.6329, 70.5)
    wp_8 = g.WayPoint(8, 23.6467, 70.6636)
    # Around Seiland to Alta
    wp_11 = g.WayPoint(11, 23., 70.5)
    wp_12 = g.WayPoint(12, 22.7499, 70.4124)
    wp_13 = g.WayPoint(13, 23.2045, 70.2511, 300.)
    wp_14 = g.WayPoint(14, 23.0768, 70.0328, 300.)
    wp_15 = g.WayPoint(15, 23.4091, 70., 100.)
    # Seiland to Hasvik and back
    wp_21 = g.WayPoint(21, 22.1740, 70.4802, 100.)
    wp_22 = g.WayPoint(22, 22.09917, 70.493854, 100.)
    wp_23 = g.WayPoint(23, 22., 70.4683)
    wp_24 = g.WayPoint(24, 22.1896, 70.4675, 100.)
    # Alta across the country to Hammerfest
    wp_30 = g.WayPoint(30, 23.5464, 70.0252, 1000.)
    wp_31 = g.WayPoint(31, 23.5656, 70.1151, 1000.)
    wp_32 = g.WayPoint(32, 24., 70.1888, 1000.)
    wp_33 = g.WayPoint(33, 24.5, 70.4220, 1000.)
    wp_34 = g.WayPoint(34, 24.3429, 70.4525, 1100.)
    wp_35 = g.WayPoint(35, 24.22, 70.5, 200.)
    # Across the country to/from Lakselv
    wp_41 = g.WayPoint(41, 25., 70.25, 1000.)
    wp_42 = g.WayPoint(42, 25., 70.05, 100.)
    wp_43 = g.WayPoint(43, 24.9444, 70., 1000.)
    wp_44 = g.WayPoint(44, 24.5, 70., 1500.)
    wp_45 = g.WayPoint(45, 24.85, 70.125, 1500.)

    graph = nx.Graph()
    graph.add_nodes_from([wp_1, wp_2, wp_3, wp_4, wp_5, wp_6, wp_7, wp_8,
                          wp_11, wp_12, wp_13, wp_14, wp_15,
                          wp_21, wp_22, wp_23, wp_24,
                          wp_30, wp_31, wp_32, wp_33, wp_34, wp_35,
                          wp_41, wp_42, wp_43, wp_44, wp_45])
    for wp in graph.nodes:
        wp.alt_m = wp.ground_m + above_ground_m
        wp.is_point_of_interest = True

    # Kvaløya
    graph.add_edge(wp_1, wp_2)
    graph.add_edge(wp_2, wp_3)
    graph.add_edge(wp_3, wp_4)
    graph.add_edge(wp_4, wp_5)
    graph.add_edge(wp_5, wp_6)
    graph.add_edge(wp_6, wp_7)
    graph.add_edge(wp_7, wp_1)
    graph.add_edge(wp_6, wp_8)
    graph.add_edge(wp_8, wp_5)
    # Around Seiland to Alta
    graph.add_edge(wp_5, wp_11)
    graph.add_edge(wp_11, wp_12)
    graph.add_edge(wp_12, wp_13)
    graph.add_edge(wp_13, wp_14)
    graph.add_edge(wp_14, wp_15)
    graph.add_edge(wp_13, wp_1)
    # Seiland to Hasvik and back
    graph.add_edge(wp_21, wp_22)
    graph.add_edge(wp_22, wp_23)
    graph.add_edge(wp_23, wp_24)
    graph.add_edge(wp_12, wp_21)
    # Alta across the country to Hammerfest
    graph.add_edge(wp_15, wp_30)
    graph.add_edge(wp_30, wp_31)
    graph.add_edge(wp_31, wp_32)
    graph.add_edge(wp_32, wp_33)
    graph.add_edge(wp_33, wp_34)
    graph.add_edge(wp_34, wp_35)
    graph.add_edge(wp_35, wp_2)
    # Across the country to/from Lakselv
    graph.add_edge(wp_33, wp_41)
    graph.add_edge(wp_41, wp_42)
    graph.add_edge(wp_42, wp_43)
    graph.add_edge(wp_43, wp_44)
    graph.add_edge(wp_44, wp_31)
    graph.add_edge(wp_44, wp_32)
    graph.add_edge(wp_43, wp_45)
    graph.add_edge(wp_45, wp_42)
    graph.add_edge(wp_45, wp_41)
    graph.add_edge(wp_45, wp_32)

    return graph


def _construct_north_norway_tanker(flight_level_m: float) -> nx.Graph:
    wp_1 = g.WayPoint(1, 20.5, 70.25, 0, flight_level_m)  # just north of Arnøya
    wp_2 = g.WayPoint(2, 21., 70.75, 0, flight_level_m)  # ca. 55 km to North North East
    graph = nx.Graph()
    graph.add_nodes_from([wp_1, wp_2])
    graph.add_edge(wp_1, wp_2)
    return graph


def _construct_sail_area_carrier_enat() -> List[Tuple[float, float]]:
    return [(24., 71.25), (23.5, 71.125), (23., 71), (22.5, 70.875), (22., 70.75), (21.5, 70.625), (21., 70.5),
            (20.5, 70.375), (20., 70.375), (20., 71.), (21., 71.25),
            (22., 71.375), (23., 71.375), (24., 71.375)]


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        # Airport ENAT Alta
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(23.3584, 69.9709, g.feet_to_metres(187.)), 0, 2),
        StaticTarget(mpt.MPTarget.S_300, g.Position(23.2561, 69.8920, 22), 0, 1),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(23.2868, 69.9833, g.feet_to_metres(610.)), 0, 1),
        StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(23.3429, 69.9805, 0), 120),
        StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(23.3466, 69.9798, 0), 120),
        StaticTarget(mpt.MPTarget.TOWER, g.Position(23.3555, 69.9775, 3), 30),
        StaticTarget(mpt.MPTarget.LIGHT_HANGAR, g.Position(23.3830, 69.9722, 1), 217),
        StaticTarget(mpt.MPTarget.BRIDGE, g.Position(23.3750, 69.9685, 0), 152),
        StaticTarget(mpt.MPTarget.POWER_PLANT, g.Position(23.5154, 70.0239, 7), 0),
        # Airport ENHF Hammerfest
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(23.6673, 70.6805, 81), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(23.6752, 70.6820, 80), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(23.6513, 70.6789, 76), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(23.6793, 70.6803, 77), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(23.6665, 70.6796, 79), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(23.6776, 70.6827, 80), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(23.6745, 70.6855, 159), 0, 1),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(23.7201, 70.6806, 191), 0, 2),
        # Airport ENHV Honningsvåg
        StaticTarget(mpt.MPTarget.LIGHT_HANGAR, g.Position(25.9764, 71.0091, 3), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(25.9703, 71.0093, 0), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(25.9963, 71.0102, 3), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(25.9786, 71.0091, 5), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(25.9803, 70.9878, 278), 0, 3),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(25.8925, 70.9844, 377), 0, 3),
        # airport ENNA Lakselv
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(24.9792, 70.0577, 7), 0, 2),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(24.9699, 70.064, 9), 85),  # along taxiway from south to north
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(24.9688, 70.0686, 8), 85),
        StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(24.9678, 70.0715, 5), 0),
        StaticTarget(mpt.MPTarget.HARD_SHELTER, g.Position(24.9676, 70.0737, 3.5), 270),  # north end
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(24.9730, 70.0555, 13), 45),  # south end
        StaticTarget(mpt.MPTarget.CHECKPOINT, g.Position(24.9847, 70.0628, 2), 110),
        StaticTarget(mpt.MPTarget.RADAR_STATION, g.Position(24.9828, 70.0531, 8), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(24.9689, 70.0801, 1), 0, 2),
        StaticTarget(mpt.MPTarget.S_300, g.Position(24.9946, 70.0493, 12), 0, 1),
        # StaticTarget(wa.MPTarget.GASOMETER, g.Position(24.9818, 70.0669, 3), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(24.9833, 70.0648, 3), 0),
        StaticTarget(mpt.MPTarget.OILRIG, g.Position(25.3508, 70.3837, 0), 0),
        # airport ENHK Hasvik
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(22.1347, 70.4861, 5), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(22.1421, 70.4848, 10), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(22.2054, 70.4917, 46), 0, 2),
        StaticTarget(mpt.MPTarget.S_300, g.Position(22.1351, 70.4966, 1), 0, 2),
        # StaticTarget(MPTarget.TRUCK, g.Position(22.1384, 70.4865, 10), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(22.1448, 70.4845, 12), 0),
        StaticTarget(mpt.MPTarget.CONTAINERS, g.Position(22.1558, 70.4837, 0), 0),
        # North-East to ENAT along the street
        # StaticTarget(MPTarget.TRUCK, g.Position(23.8913, 70.1761, 383), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(23.9093, 70.1769, 352), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(23.9321, 70.1794, 345), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(23.9693, 70.1849, 326), 0, 3),

        # StaticTarget(MPTarget.TRUCK, g.Position(24.5114, 70.4236, 85), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(24.5110, 70.4268, 77), 0, 3),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(24.5077, 70.4177, 107), 0),

        # StaticTarget(MPTarget.TRUCK, g.Position(24.9109, 70.2044, 18), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(24.9091, 70.2133, 41), 0, 1),

        # StaticTarget(MPTarget.TRUCK, g.Position(24.2908, 69.9208, 475), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(24.3015, 69.9244, 469), 0, 2),
        # StaticTarget(MPTarget.TRUCK, g.Position(24.2836, 69.9192, 468), 0),
        # StaticTarget(MPTarget.TRUCK, g.Position(24.2759, 69.9173, 468), 0),
    ]
    automat_1 = AutomatTarget('br-enhf.fgfp', AutomatType.mig_29, True, True,
                              True, True, 150,
                              4000, 8000, 0, False, 50,
                              True, 1, 1, 3, tacview=False)
    automat_2 = AutomatTarget('br-enna.fgfp', AutomatType.su_27, True, True,
                              True, True, 150,
                              4000, 8000, 0, False, 50,
                              True, 1, 2, 3, tacview=False)
    vinson_carrier = CarrierDefinition(fgt.CarrierType.vinson, _construct_sail_area_carrier_enat(), (21.5, 70.9))
    tanker = TankerDefinition(ENTC, _construct_north_norway_tanker(g.feet_to_metres(20000)))
    scenario = ScenarioContainer('north_norway', 'North Norway',  'Cf. http://opredflag.com/forum_threads/3154248',
                                 OPFOR_defaults,
                                 (20., 69.5), (27., 71.5),
                                 'ENNA', 12.3, None, 60)
    scenario.add_static_targets(static_targets)
    scenario.add_automats([automat_1, automat_2])
    scenario.add_carrier(vinson_carrier)
    scenario.add_tanker(tanker)
    scenario.add_helicopters(3, 5, _construct_north_norway_heli(100.), default_helis_list)
    scenario.add_drones(3, 5, _construct_north_norway_heli(100.), default_drones_list)
    scenario.add_ships(3, 5, 8, _construct_north_norway_ship(0.), default_ships_list)
    return scenario
