import csv

def generate_html(csv_filepath, html_filepath):
    # Read data from CSV
    applications = []
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            applications.append(row)

    # Group applications by category
    categories = {}
    for app in applications:
        category = app.get('Category', 'Uncategorized') # Use 'Uncategorized' if no category
        if not category.strip(): # Handle empty category names
            category = 'Uncategorized'
        if category not in categories:
            categories[category] = []
        categories[category].append(app)

    # Start HTML content
    html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 应用导航</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>AI 应用导航</h1>
    </header>
    <main>
"""

    # Add categories and applications to HTML
    sorted_categories = sorted(categories.keys())

    for category_name in sorted_categories:
        apps_in_category = categories[category_name]
        # Create a URL-friendly ID for the category
        category_id = category_name.lower().replace(' ', '-').replace('/', '-').replace('&', '-').replace('(', '').replace(')', '')
        html_content += f'        <section class="category-section" id="category-{category_id}">\n'
        html_content += f'            <h2>{category_name}</h2>\n'
        html_content += '            <div class="app-grid">\n'
        for app in apps_in_category:
            name = app.get('Name', 'N/A')
            website = app.get('Website', '#')
            # Use '描述' column for description, fallback to 'Description' if '描述' is empty or not present
            description_zh = app.get('描述', '')
            description_en = app.get('Description', 'No description available.')
            description = description_zh if description_zh.strip() else description_en
            
            html_content += '                <div class="app-card">\n'
            html_content += f'                    <h3><a href="{website}" target="_blank">{name}</a></h3>\n'
            html_content += f'                    <p class="description">{description}</p>\n'
            # Tags are omitted as per todo.md
            html_content += '                </div>\n'
        html_content += '            </div>\n'
        html_content += '        </section>\n'

    # End HTML content
    html_content += """
    </main>
    <footer>
        <p>&copy; 2025 AI 应用导航</p>
    </footer>
</body>
</html>
"""

    # Write HTML to file
    with open(html_filepath, mode='w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"HTML file generated at {html_filepath}")

if __name__ == '__main__':
    csv_file = '/home/ubuntu/upload/site.csv'
    html_file = '/home/ubuntu/index.html'
    generate_html(csv_file, html_file)

