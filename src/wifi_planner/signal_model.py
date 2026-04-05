"""
WiFi Signal Propagation Model
Implements path loss and signal strength calculations
"""

import math

def signal_strength(x, y, transmitter_x=0, transmitter_y=0, tx_power=20):
    """
    Calculate signal strength at point (x, y)
    Uses free space path loss model: P(d) = P0 - 20*log10(d)
    """
    distance = math.sqrt((x - transmitter_x)**2 + (y - transmitter_y)**2)
    if distance < 0.1:
        return tx_power
    path_loss = 20 * math.log10(distance)
    return tx_power - path_loss

def coverage_area(grid_size, threshold=-70):
    """
    Generate coverage heatmap for given grid size
    Returns list of coordinates with signal strength >= threshold
    """
    coverage = []
    for x in range(0, grid_size):
        for y in range(0, grid_size):
            strength = signal_strength(x, y)
            if strength >= threshold:
                coverage.append({'x': x, 'y': y, 'signal_dbm': strength})
    return coverage