# This file is Copyright (c) 2018 Florent Kermarrec <florent@enjoy-digital.fr>
# License: BSD

from litex.build.generic_platform import *
from litex.build.microsemi import MicrosemiPlatform

_io = [
    ("clk50", 0, Pins("R1"), IOStandard("LVCMOS25")),
    ("clk50", 1, Pins("J3"), IOStandard("LVCMOS25")),

    ("rst", 0, Pins("F5"), IOStandard("LVCMOS33")),

    ("user_led", 0, Pins("D6"), IOStandard("LVCMOS33")),
    ("user_led", 1, Pins("D7"), IOStandard("LVCMOS33")),
    ("user_led", 2, Pins("D8"), IOStandard("LVCMOS33")),
    ("user_led", 3, Pins("D9"), IOStandard("LVCMOS33")),

    ("user_btn", 0, Pins("E13"), IOStandard("LVCMOS33")),
    ("user_btn", 1, Pins("E14"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("F16")),
        Subsignal("rx", Pins("F17")),
        IOStandard("LVCMOS33")
    ),

    ("spiflash4x", 0,
        Subsignal("clk", Pins("J1")),
        Subsignal("cs_n", Pins("H1")),
        Subsignal("dq", Pins("F2 F1 M7 M8")),
        IOStandard("LVCMOS25")
    ),
    ("spiflash", 0,
        Subsignal("clk", Pins("J1")),
        Subsignal("cs_n", Pins("H1")),
        Subsignal("mosi", Pins("F2")),
        Subsignal("miso", Pins("F1")),
        Subsignal("wp", Pins("M7")),
        Subsignal("hold", Pins("M8")),
        IOStandard("LVCMOS25"),
    ),

    # FIXME: add IO constraints
    ("ddram", 0,
        Subsignal("a", Pins(
            "U5 U4 V4 W3 V5 W4 Y3 AA3",
            "Y4 Y5 AA2 AB2 V6 W6 AB3")),
        Subsignal("ba", Pins("V7 Y6 U7")),
        Subsignal("ras_n", Pins("AA6")),
        Subsignal("cas_n", Pins("AA5")),
        Subsignal("we_n", Pins("AB5")),
        Subsignal("cs_n", Pins("W7")),
        Subsignal("dm", Pins("Y9 R15")),
        Subsignal("dq", Pins(
            "T7 T8 U8 U9 R10 V9 V10 D7",
            "V14 U14 R12 T11 U15 T13 U13 T15")),
        Subsignal("dqs_p", Pins("T10 R13")),
        Subsignal("dqs_n", Pins("U10 T12")),
        Subsignal("clk_p", Pins("V2")),
        Subsignal("clk_n", Pins("W2")),
        Subsignal("cke", Pins("W8")),
        Subsignal("odt", Pins("AA7")),
        Subsignal("reset_n", Pins("AB7")),
    ),

    ("eth_clocks", 0,
        Subsignal("tx", Pins("J8")),
        Subsignal("rx", Pins("K3")),
        IOStandard("LVCMOS25")
    ),
    ("eth", 0,
        Subsignal("rst_n", Pins("L8"), IOStandard("LVCMOS33")),
        Subsignal("int_n", Pins("J4")),
        Subsignal("mdio", Pins("H2")),
        Subsignal("mdc", Pins("J2")),
        Subsignal("rx_ctl", Pins("K5")),
        Subsignal("rx_data", Pins("J9 K1 K6 K4")),
        Subsignal("tx_ctl", Pins("L5")),
        Subsignal("tx_data", Pins("K8 L1 L2 L3")),
        IOStandard("LVCMOS25")
    ),
]

class Platform(MicrosemiPlatform):
    default_clk_name = "clk50"
    default_clk_period = 20.0

    def __init__(self):
        MicrosemiPlatform.__init__(self, "MPF300TS_ES", _io)
