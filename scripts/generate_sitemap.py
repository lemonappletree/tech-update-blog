import os
from datetime import datetime

BASE_URL = "https://tech.lovely-world-together.com"  # 너의 블로그 URL

def generate_sitemap(posts_dir="_posts", output_file="sitemap.xml"):
    urls = []
    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            date_part = filename.split('-')[:3]
            slug_part = "-".join(filename.split('-')[3:]).replace('.md', '')
            url = f"{BASE_URL}/{date_part[0]}/{date_part[1]}/{date_part[2]}/{slug_part}.html"
            urls.append(url)

    now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in urls:
            f.write('  <url>\n')
            f.write(f'    <loc>{url}</loc>\n')
            f.write(f'    <lastmod>{now}</lastmod>\n')
            f.write('    <changefreq>daily</changefreq>\n')
            f.write('    <priority>0.8</priority>\n')
            f.write('  </url>\n')
        f.write('</urlset>\n')

if __name__ == "__main__":
    generate_sitemap()