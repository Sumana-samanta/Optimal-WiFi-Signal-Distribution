#!/usr/bin/env python3
import argparse
import pandas as pd
import math

def signal_strength(x, y, transmitter_x=0, transmitter_y=0, tx_power=20):
    """Calculate signal strength at point (x, y) using free space path loss"""
    distance = math.sqrt((x - transmitter_x)**2 + (y - transmitter_y)**2)
    if distance < 0.1:
        return tx_power
    path_loss = 20 * math.log10(distance)
    return tx_power - path_loss

def main():
    parser = argparse.ArgumentParser(description="Convert WiFi device points to signal heatmap CSV")
    parser.add_argument("--grid-size", type=int, required=True, help="Grid size for signal mapping")
    parser.add_argument("--points", required=True, help="Input CSV with device locations")
    parser.add_argument("--out", required=True, help="Output CSV file path")
    args = parser.parse_args()

    df = pd.read_csv(args.points)
    print(f"Processing {len(df)} WiFi device locations...")
    print(f"Grid size: {args.grid_size}x{args.grid_size}")
    
    # Generate signal map
    output_data = []
    for x in range(args.grid_size):
        for y in range(args.grid_size):
            strength = signal_strength(x, y)
            if strength > -70:
                output_data.append({'x': x, 'y': y, 'signal_strength_dbm': round(strength, 2)})
    
    output_df = pd.DataFrame(output_data)
    output_df.to_csv(args.out, index=False)
    print(f"Signal distribution saved to {args.out}")

if __name__ == "__main__":
    main()