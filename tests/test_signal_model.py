"""
Unit tests for WiFi signal model
"""

import sys
sys.path.insert(0, '../src')
from wifi_planner.signal_model import signal_strength, coverage_area

def test_signal_strength():
    """Test signal strength calculation"""
    # At origin, should be at transmit power
    assert signal_strength(0, 0) == 20
    print("✓ Signal strength at origin: PASS")
    
    # At distance, should be attenuated
    strength_dist = signal_strength(10, 0)
    assert strength_dist < 20
    print("✓ Signal attenuation over distance: PASS")

def test_coverage_area():
    """Test coverage area generation"""
    coverage = coverage_area(grid_size=10, threshold=-70)
    assert len(coverage) > 0
    print(f"✓ Coverage area generated: {len(coverage)} points")

if __name__ == "__main__":
    test_signal_strength()
    test_coverage_area()
    print("\n✅ All tests passed!")