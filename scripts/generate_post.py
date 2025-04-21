import feedparser
from datetime import datetime
import os
from openai import OpenAI
from pathlib import Path

# OpenAI 키 설정
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 기술 RSS 피드 목록
feeds = {
    "Kubernetes": "https://kubernetes.io/feed.xml",
    "Spring Boot": "https://spring.io/blog.atom",
    "Docker": "https://www.docker.com/blog/feed/",
    "Java": "https://inside.java/feed.xml",
    "Golang": "https://go.dev/blog/feed.atom",
    "Helm": "https://helm.sh/blog/index.xml"
}

def summarize(title, link, summary):
    prompt = f"""Summarize this tech blog post in Korean:
Title: {title}
Summary: {summary}
Link: {link}
"""
    response = client.chat.completions.create(
        model="gpt-4o",  # 또는 gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content


def generate_markdown(posts):
    today = datetime.now().strftime('%Y-%m-%d')
    posts_dir = Path("_posts")
    posts_dir.mkdir(exist_ok=True)

    filename = posts_dir / f"{today}-tech-update.md"
    content = f"# 🛠️ {today} 기술 업데이트 요약\n\n"
    for post in posts:
        content += f"## 🔹 {post['title']}\n{post['summary']}\n👉 [자세히 보기]({post['link']})\n\n"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    collected = []
    for name, url in feeds.items():
        feed = feedparser.parse(url)
        if not feed.entries:
            continue

        latest = feed.entries[0]
        summary_text = getattr(latest, "summary", "")
        summary = summarize(latest.title, latest.link, summary_text)
        collected.append({
            'title': f"{name} - {latest.title}",
            'link': latest.link,
            'summary': summary
        })

    if collected:
        generate_markdown(collected)
        print("✅ 포스트 생성 완료!")
    else:
        print("⚠️ 업데이트할 내용이 없습니다.")

if __name__ == "__main__":
    main()
