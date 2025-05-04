# 2025/05/03
# Revese engineering 3B6000 firmware
# Part:
#   Configuring 0x1fe001b0, calculating configuration from setted main clock

def MainClockTo1b0(mainclock): 
    a0 = mainclock
    s0 = 3 # might be 2, but that's for strange CPU SKU
    t0 = s0 * a0
    t1 = 100
    t0 = t0 << 1
    s2 = int(t0 / t1)
    t0 = s2 << 32
    s2 = s2 << 54 
    t0 = t0 | s2 
    s0 = s0 << 42 # recall, s0 depends on CPU SKU
    s0 = t0 | s0 
    t0 = 0x0002000008100f84 # default configuration
    s0 = s0 | t0
    return s0

clocks = [
        2300,
        2350, 
        2400,
        2450,
        2500,
        2600,
        2650,
        2700,
        2750
        ]

for freqs in clocks: 
    print("{}\t{}".format(freqs, hex(MainClockTo1b0(freqs))))
