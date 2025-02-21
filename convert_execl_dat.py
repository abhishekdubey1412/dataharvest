import json
import pandas as pd

# def save_table_data_to_excel(file_name, table_id):
#     with open(file_name, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     # all_table_data = []
#     # for entry in data.get("Data", []):
#     #     tables = entry.get("tables", {})
#     #     if isinstance(tables, dict):
#     #         main_body = tables.get("main_body_content", {})
#     #         if isinstance(main_body, dict):
#     #             table_data = main_body.get(table_id, [])
#     #             all_table_data.extend(table_data)

#     # df_all_table = pd.DataFrame(all_table_data).dropna(how="all")

#     excel_path = file_name.replace(".json", ".xlsx")
#     df_all_table.to_excel(excel_path, index=False)

#     print(f"Excel file saved at: {excel_path}")


# file_name = {
#     "tpchd.org": "table_3",
#     "stowe.co.uk": "table_1",
#     "sc.edu": "table_1",
#     "marathoncounty.gov": "table_1"
# }
# for file, table_id in file_name.items():
#     json_file_name = f"{file}.json"
#     save_table_data_to_excel(json_file_name, table_id)


def save_filtered_data_to_excel(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    filtered_data = data.get("filtered_data", [])

    if filtered_data:
        df_filtered = pd.DataFrame(filtered_data)
        excel_path = json_file.replace(".json", ".xlsx")
        df_filtered.to_excel(excel_path, index=False)
        print(f"Excel file saved at: {excel_path}")
    else:
        print(f"No filtered data found in {json_file}")

file_name = [
    "wlv.ac.uk"
]

for file in file_name:
    json_file_name = f"{file}.json"
    save_filtered_data_to_excel(json_file_name)