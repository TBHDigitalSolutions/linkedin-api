import os
import subprocess
import inspect

# Define output directories
base_dir = "/Users/tbhdigitalsolutions/Documents/GitHub/linkedin-api"
output_dirs = {
    "Pydeps": os.path.join(base_dir, "understand_output/Pydeps_output"),
    "PyInspect": os.path.join(base_dir, "understand_output/PyInspect_output"),
    "Pyreverse": os.path.join(base_dir, "understand_output/Pyreverse_output"),
    "Recipy": os.path.join(base_dir, "understand_output/Recipy_output"),
}

# Create output directories if they do not exist
for dir_path in output_dirs.values():
    os.makedirs(dir_path, exist_ok=True)

# 1. Run Pyreverse to generate UML diagrams
def run_pyreverse():
    print("Running Pyreverse...")
    try:
        # Run Pyreverse to generate .dot files
        subprocess.run(
            [
                "pyreverse",
                "-o",
                "png",  # Generate PNG output
                "-p",
                "linkedin_api",  # Project name specified, which affects file names
                "linkedin_api/",
            ],
            cwd=base_dir,
            check=True,
        )

        # Define expected output filenames based on the specified project name
        generated_files = [
            "classes_linkedin_api.png",
            "packages_linkedin_api.png",
        ]

        # Move the generated files to the Pyreverse output directory
        for file_name in generated_files:
            subprocess.run(
                [
                    "mv",
                    file_name,
                    output_dirs["Pyreverse"],
                ],
                cwd=base_dir,
                check=True,
            )

        print("Pyreverse completed successfully.")
    except Exception as e:
        print(f"Error running Pyreverse: {e}")

# 2. Use PyInspect to inspect Linkedin module
def run_pyinspect():
    print("Running PyInspect...")
    try:
        output_file = os.path.join(output_dirs["PyInspect"], "inspect_output.txt")
        with open(output_file, "w") as f:
            from linkedin_api import Linkedin

            def analyze_module(module):
                try:
                    f.write("Source Code:\n")
                    f.write(inspect.getsource(module))
                except TypeError:
                    f.write("Could not retrieve source code. The module may be compiled or obfuscated.\n")

                f.write("\n\nSignature:\n")
                try:
                    f.write(str(inspect.signature(module)))
                except ValueError:
                    f.write("Could not retrieve signature information.\n")

                f.write("\n\nDocstring:\n")
                doc = inspect.getdoc(module)
                if doc:
                    f.write(doc)
                else:
                    f.write("No docstring available.\n")

            # Example inspection of Linkedin class without executing any code
            analyze_module(Linkedin)
        print("PyInspect completed successfully.")
    except Exception as e:
        print(f"Error running PyInspect: {e}")

# 3. Run Pydeps to visualize dependencies
def run_pydeps():
    print("Running Pydeps...")
    try:
        # Pydeps does not directly accept --output; using --noshow to suppress display
        subprocess.run(
            [
                "pydeps",
                "--noshow",  # To avoid displaying the graph
                "linkedin_api"
            ],
            cwd=base_dir,
            check=True,
        )
        # Move the generated .svg file from the root to the designated folder
        default_svg = os.path.join(base_dir, "linkedin_api.svg")  # Check the generated filename
        output_file = os.path.join(output_dirs["Pydeps"], "dependencies.svg")
        if os.path.exists(default_svg):
            os.rename(default_svg, output_file)
        print("Pydeps completed successfully.")
    except Exception as e:
        print(f"Error running Pydeps: {e}")

# 4. Use Recipy for logging code analysis instead of execution
def run_recipy():
    print("Running Recipy...")
    try:
        recipy_log_path = os.path.join(output_dirs["Recipy"], "recipy_log.txt")
        # Set environment variables to direct Recipy logging to a custom file
        os.environ["RECIPY_LOGFILE"] = recipy_log_path
        
        # Rather than executing scripts, log simulated analysis or metadata
        with open(recipy_log_path, "a") as log:
            log.write("Recipy Analysis Log\n")
            log.write("This is a simulated log entry capturing metadata about the project.\n")
            log.write(f"Analyzed linkedin.py without executing real-time API calls.\n")

        print("Recipy simulation completed successfully.")
    except Exception as e:
        print(f"Error running Recipy: {e}")

# Run all tools
if __name__ == "__main__":
    run_pyreverse()
    run_pyinspect()
    run_pydeps()
    run_recipy()
