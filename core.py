from datascience import Table
from gradio_client import Client

MAX_ROWS = 50

def analyze_csv(csv_path, max_rows=MAX_ROWS):
    table = Table.read_table(csv_path)
    
    if table.num_rows > max_rows:
        sampled_table = table.sample(max_rows)
        table_str = sampled_table.as_text()
        prompt = (
            f"Here is a sample of a large table (showing {max_rows} rows out of {table.num_rows} total):\n"
            f"{table_str}\n\n"
            "Please summarize what this data is, explain what it means, make predictions, "
            "and provide a final stylized summary."
        )
    else:
        table_str = table.as_text()
        prompt = (
            f"Here is a table:\n{table_str}\n\n"
            "Please summarize what this data is, explain what it means, make predictions, "
            "and provide a final stylized summary."
        )
    
    client = Client("TejAndrewsACC/Nyxion-7v-2.0-ACC-10.00")
    result = client.predict(
        user_message=prompt,
        api_name="/gradio_chat"
    )
    
    return result.replace(";", "\n    ")


