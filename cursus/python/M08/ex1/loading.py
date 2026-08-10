#!/usr/bin/env python3

"""Analyze simulated Matrix data with optional external packages"""

import importlib
import sys


DATA_POINTS = 1000
OUTPUT_FILE = "matrix_analysis.png"
REQUIRED_PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def load_module(module_name: str) -> object | None:
    """Return an imported module or None when it is unavailable"""

    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def get_module_version(module: object) -> str:
    """Return a module version or unknown when absent"""

    version = getattr(module, "__version__", "unknown")
    return str(version)


def build_dependency_modules() -> dict[str, object | None]:
    """Load required dependency modules dynamically"""

    return {
        package_name: load_module(package_name)
        for package_name in REQUIRED_PACKAGES
    }


def print_dependency_status(
    modules: dict[str, object | None],
) -> None:
    """Print dependency availability and versions"""

    print("Checking dependencies:")
    for package_name, description in REQUIRED_PACKAGES.items():
        module = modules[package_name]
        if module is None:
            print(f"[MISSING] {package_name} - {description}")
            continue
        print(
            f"[OK] {package_name} ({get_module_version(module)}) - "
            f"{description}"
        )


def has_all_dependencies(modules: dict[str, object | None]) -> bool:
    """Return whether all required dependencies are available"""

    return all(module is not None for module in modules.values())


def print_installation_instructions() -> None:
    """Print dependency installation instructions"""

    print("Missing programs detected.")
    print("Install with pip:")
    print(f"{sys.executable} -m pip install -r requirements.txt")
    print("Or install with Poetry:")
    print("poetry install")
    print("Then run this program again.")


def print_dependency_management_comparison() -> None:
    """Print a short pip and Poetry comparison"""

    print("Dependency management comparison:")
    print("pip uses requirements.txt for direct package installation.")
    print("Poetry uses pyproject.toml to manage project metadata and locks.")


def build_matrix_dataframe(
    pandas_module: object,
    numpy_module: object,
) -> object:
    """Build simulated Matrix data from numpy arrays"""

    random_module = getattr(numpy_module, "random")
    default_rng = getattr(random_module, "default_rng")
    random_generator = default_rng(42)
    signal = random_generator.normal(loc=50, scale=12, size=DATA_POINTS)
    anomaly = random_generator.integers(0, 2, size=DATA_POINTS)
    noise = random_generator.normal(loc=0, scale=4, size=DATA_POINTS)
    dataframe_builder = getattr(pandas_module, "DataFrame")
    return dataframe_builder({
        "signal": signal,
        "anomaly": anomaly,
        "stability": signal - noise,
    })


def get_analysis_summary(dataframe: object) -> dict[str, float]:
    """Return numeric analysis results for Matrix data"""

    get_column = getattr(dataframe, "__getitem__")
    signal_column = get_column("signal")
    stability_column = get_column("stability")
    anomaly_column = get_column("anomaly")
    return {
        "mean_signal": float(signal_column.mean()),
        "max_stability": float(stability_column.max()),
        "anomaly_rate": float(anomaly_column.mean()),
    }


def save_visualization(
    dataframe: object,
    pyplot_module: object,
    output_file: str,
) -> None:
    """Save a Matrix signal visualization"""

    subplots = getattr(pyplot_module, "subplots")
    close = getattr(pyplot_module, "close")
    get_column = getattr(dataframe, "__getitem__")
    signal_column = get_column("signal")
    figure, axis = subplots(figsize=(8, 4))
    signal_column.head(100).plot(ax=axis, title="Matrix Signal")
    axis.set_xlabel("Data point")
    axis.set_ylabel("Signal")
    figure.tight_layout()
    figure.savefig(output_file)
    close(figure)


def run_analysis(modules: dict[str, object | None]) -> None:
    """Run the Matrix data analysis workflow"""

    pandas_module = modules["pandas"]
    numpy_module = modules["numpy"]
    matplotlib_module = modules["matplotlib"]
    if (
        pandas_module is None
        or numpy_module is None
        or matplotlib_module is None
    ):
        print_installation_instructions()
        return
    pyplot_module = importlib.import_module("matplotlib.pyplot")
    print("Analyzing Matrix data...")
    dataframe = build_matrix_dataframe(pandas_module, numpy_module)
    get_data_count = getattr(dataframe, "__len__")
    print(f"Processing {get_data_count()} data points...")
    get_analysis_summary(dataframe)
    print("Generating visualization...")
    save_visualization(dataframe, pyplot_module, OUTPUT_FILE)
    print("Analysis complete!")
    print(f"Results saved to: {OUTPUT_FILE}")


def main() -> None:
    """Run the loading programs workflow"""

    print("LOADING STATUS: Loading programs...")
    modules = build_dependency_modules()
    print_dependency_status(modules)
    print_dependency_management_comparison()
    if not has_all_dependencies(modules):
        print_installation_instructions()
        return
    run_analysis(modules)


if __name__ == "__main__":
    main()
