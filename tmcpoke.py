#!/usr/bin/env python

import usbtmc

instr =  usbtmc.Instrument(0xc03e, 0xb007)
instr.pulse()