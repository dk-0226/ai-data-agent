import os

# Define pipeline steps
steps = [
    "v2-architect/databricks/bronze.py",
    "v2-architect/databricks/silver.py",
    "v2-architect/databricks/agent_layer.py"
]

# Execute pipeline
for step in steps:
    print(f"\n Running: {step}\n")
    exit_code = os.system(f"python {step}")

    if exit_code != 0:
        print(f"\n Error in step: {step}")
        break
print("\n Pipeline execution completed")

