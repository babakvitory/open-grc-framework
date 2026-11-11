"""
Open GRC Framework - Core Schema Validator (v0.1)
Validates machine-readable GRC compliance mapping YAML files and generates coverage summaries.
"""

import os
import sys
import yaml


REQUIRED_TOP_KEYS = ["schema_version", "framework_mapping", "domains"]
REQUIRED_CONTROL_KEYS = ["unified_control_id", "title", "mappings", "evidence_requirements"]


def validate_grc_schema(file_path: str) -> bool:
    """Validate structure and required fields of a GRC YAML mapping file."""
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return False

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(f"[ERROR] Invalid YAML syntax in {file_path}: {exc}")
        return False

    if not isinstance(data, dict):
        print("[ERROR] Root structure must be a YAML mapping/dictionary.")
        return False

    # Check top-level keys
    for key in REQUIRED_TOP_KEYS:
        if key not in data:
            print(f"[ERROR] Missing required top-level key: '{key}'")
            return False

    domains = data.get("domains", [])
    if not isinstance(domains, list) or len(domains) == 0:
        print("[ERROR] 'domains' must be a non-empty list.")
        return False

    total_controls = 0
    for domain in domains:
        domain_id = domain.get("domain_id", "UNKNOWN")
        controls = domain.get("controls", [])
        for ctrl in controls:
            total_controls += 1
            for req_key in REQUIRED_CONTROL_KEYS:
                if req_key not in ctrl:
                    print(f"[ERROR] Control in domain '{domain_id}' missing key: '{req_key}'")
                    return False

    mapping_name = data["framework_mapping"].get("name", "Unnamed Mapping")
    print(f"[SUCCESS] Valid GRC Schema: '{mapping_name}'")
    print(f"          Domains validated: {len(domains)} | Unified Controls: {total_controls}")
    return True


if __name__ == "__main__":
    default_sample = os.path.join("schemas", "iso27001-nis2-mapping-sample.yaml")
    target_file = sys.argv[1] if len(sys.argv) > 1 else default_sample
    is_valid = validate_grc_schema(target_file)
    sys.exit(0 if is_valid else 1)
