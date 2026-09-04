#!/usr/bin/env python3

import importlib
import sys


DATA_POINTS = 1000
OUTPUT_FILE = "matrix_analysis.png"
RANDOM_SEED = 42
PANDAS_MODULE = "pandas"
NUMPY_MODULE = "numpy"
MATPLOTLIB_MODULE = "matplotlib"
PYPLOT_MODULE = "matplotlib.pyplot"
REQUIRED_PACKAGES = {
    PANDAS_MODULE: "Data manipulation ready",
    NUMPY_MODULE: "Numerical computation ready",
    MATPLOTLIB_MODULE: "Visualization ready",
}


def build_dependency_modules() -> dict[str, object | None]:
    """Load required dependency modules dynamically"""

    return {
        package_name: load_module(package_name)
        for package_name in REQUIRED_PACKAGES
    }


def load_module(module_name: str) -> object | None:
    """Return an imported module or None when it is unavailable"""

    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def print_dependency_status(modules: dict[str, object | None]) -> None:

    print("Checking dependencies:")
    for package_name, description in REQUIRED_PACKAGES.items():
        print(format_dependency_status(package_name, description, modules))
    print()


def format_dependency_status(
    package_name: str,
    description: str,
    modules: dict[str, object | None],
) -> str:
    """Return one dependency status line"""

    module = modules[package_name]
    if module is None:
        return f"[MISSING] {package_name} - {description}"
    return (
        f"[OK] {package_name} ({get_module_version(module)}) - "
        f"{description}"
    )


def get_module_version(module: object) -> str:
    """Return a module version or unknown when absent"""

    version = getattr(module, "__version__", "unknown")
    return str(version)


def print_dependency_management_comparison() -> None:

    print(
        "Dependency management comparison:\n"
        "pip uses requirements.txt for direct package installation.\n"
        "Poetry uses pyproject.toml to manage project metadata and locks.\n"
    )


def has_all_dependencies(modules: dict[str, object | None]) -> bool:
    """Return whether all required dependencies are available"""

    return all(module is not None for module in modules.values())


def print_installation_instructions() -> None:

    print(
        "Missing programs detected.\n"
        f"Install with pip:\n"
        f"{sys.executable} -m pip install -r requirements.txt\n"
        f"Or install with Poetry:\n"
        f"poetry install\n"
        f"Then run this program again.\n"
    )


def run_analysis(modules: dict[str, object | None]) -> None:
    """Run the Matrix data analysis workflow"""

    pd = require_module(modules, PANDAS_MODULE)
    np = require_module(modules, NUMPY_MODULE)
    plt = importlib.import_module(PYPLOT_MODULE)

    print("Analyzing Matrix data...")
    dataframe = build_matrix_dataframe(pd, np)
    get_data_count = getattr(dataframe, "__len__")
    print(f"Processing {get_data_count()} data points...")
    get_analysis_summary(dataframe)
    print("Generating visualization...")
    save_visualization(dataframe, plt, OUTPUT_FILE)
    print(
        "\nAnalysis complete!\n"
        f"Results saved to: {OUTPUT_FILE}"
    )


def require_module(
    modules: dict[str, object | None],
    module_name: str,
) -> object:
    """Return a loaded module or raise when unavailable"""

    module = modules[module_name]
    if module is None:
        raise RuntimeError(f"Missing required dependency: {module_name}")
    return module


def build_matrix_dataframe(
    pandas_module: object,
    numpy_module: object,
) -> object:
    """Build simulated Matrix data from numpy arrays"""

    random_generator = get_numpy_random_generator(numpy_module)
    normal = getattr(random_generator, "normal")
    integers = getattr(random_generator, "integers")
    signal = normal(loc=50, scale=12, size=DATA_POINTS)
    anomaly = integers(0, 2, size=DATA_POINTS)
    noise = normal(loc=0, scale=4, size=DATA_POINTS)
    dataframe_builder = getattr(pandas_module, "DataFrame")
    return dataframe_builder({
        "signal": signal,
        "anomaly": anomaly,
        "stability": signal - noise,
    })


def get_numpy_random_generator(numpy_module: object) -> object:
    """Return a seeded numpy random generator"""

    random_module = getattr(numpy_module, "random")
    default_rng = getattr(random_module, "default_rng")
    return default_rng(RANDOM_SEED)


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


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")
    modules = build_dependency_modules()
    print_dependency_status(modules)
    print_dependency_management_comparison()
    if not has_all_dependencies(modules):
        print_installation_instructions()
        return
    run_analysis(modules)


if __name__ == "__main__":
    main()
