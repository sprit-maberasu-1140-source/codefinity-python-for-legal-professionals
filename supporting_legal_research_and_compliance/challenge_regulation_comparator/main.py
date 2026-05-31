def compare_regulations(old_sections, new_sections):
    added_sections = [section for section in new_sections if section not in old_sections]
    removed_sections = [section for section in old_sections if section not in new_sections]
    added_str = ", ".join(added_sections)
    removed_str = ", ".join(removed_sections)
    print("Added sections:", added_str)
    print("Removed sections:", removed_str)

# Sample regulation lists
old_version = ["Section 1", "Section 2", "Section 3", "Section 4"]
new_version = ["Section 2", "Section 3", "Section 4", "Section 5", "Section 6"]

compare_regulations(old_version, new_version)
