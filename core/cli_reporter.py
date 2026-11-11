"""
Open GRC Framework - Unified CLI Reporter (v0.1)
Scans all schema files in the 'schemas/' directory and generates a unified compliance coverage report.
"""

import glob
import os
import yaml


def generate_unified_report(schemas_dir: str = "schemas") -> None:
    """Read all YAML mapping schemas and print a consolidated summary report."""
    pattern = os.path.join(schemas_dir, "*.yaml")
    schema_files = sorted(glob.glob(pattern))

    if not schema_files:
        print(f"[INFO] No YAML schema files found in '{schemas_dir}/'.")
        return

    print("=" * 65)
    print("OPEN GRC FRAMEWORK - UNIFIED COMPLIANCE COVERAGE REPORT")
    print("=" * 65)

    total_frameworks = 0
    total_domains = 0
    total_controls = 0
    total_evidence = 0

    for file_path in schema_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as exc:
            print(f"[WARNING] Skipping invalid file '{file_path}': {exc}")
            continue

        if not isinstance(data, dict) or "framework_mapping" not in data:
            continue

        total_frameworks += 1
        meta = data.get("framework_mapping", {})
        domains = data.get("domains", [])

        file_controls = 0
        file_evidence = 0
        for domain in domains:
            controls = domain.get("controls", [])
            file_controls += len(controls)
            for ctrl in controls:
                file_evidence += len(ctrl.get("evidence_requirements", []))

        total_domains += len(domains)
        total_controls += file_controls
        total_evidence += file_evidence

        print(f"\nFramework ID : {meta.get('id', 'N/A')}")
        print(f"Title        : {meta.get('name', 'Unnamed')}")
        print(f"Source File  : {os.path.basename(file_path)}")
        print(f"Coverage     : {len(domains)} Domains | {file_controls} Unified Controls | {file_evidence} Evidence Items")

    print("\n" + "-" * 65)
    print(f"TOTAL SUMMARY: {total_frameworks} Frameworks | {total_domains} Domains | "
          f"{total_controls} Controls | {total_evidence} Evidence Requirements")
    print("=" * 65)


if __name__ == "__main__":
    generate_unified_report()
