from smartmoneyconcepts.smc import smc
# smartmoneyconcepts/__init__.py
import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

# Load the CSV data
csv_file_path = "../tests/test_data/EURUSD/EURUSD_15M.csv"
ohlc = load_csv(csv_file_path)


print("OHLC Data Head:")
print(ohlc.head())

# Assuming smc is a module and fvg is a function within that module
result = smc.fvg(ohlc, join_consecutive=True)

print("FVG Result:")
print(result)

# Save the result as a CSV file
result_csv_path = "result0803.csv"
result.to_csv(result_csv_path, index=False)
print(f"Result saved to {result_csv_path}")




# smc.swing_highs_lows("ohlc", swing_length = 50)


# smc.ob("ohlc", "swing_highs_lows", close_mitigation = False)
