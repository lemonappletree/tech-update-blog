import feedparser
from datetime import datetime
import os
from openai import OpenAI

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 블로그에 사용할 RSS 피드 목록
feeds = {
    "Kubernetes": "https://kubernetes.io/feed.xml",
    "Spring Boot": "https://spring.io/blog.atom",
    "Docker": "https://www.docker.com/blog/feed/",
    "Java": "https://inside.java/feed.xml",
    "Golang": "https://go.dev/blog/feed.atom",
    "Helm": "https://helm.sh/blog/index.xml"
}

def summarize(title, link, summary, language="ko"):
    if language == "ko":
        prompt = f"""다음 기술 블로그 글을 한국어로 간단히 요약해줘:\nTitle: {title}\nSummary: {summary}\nLink: {link}"""
    else:
        prompt = f"""Summarize this tech blog post in English:\nTitle: {title}\nSummary: {summary}\nLink: {link}"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content

def generate_markdown(posts, language="ko"):
    today = datetime.now().strftime('%Y-%m-%d')
    suffix = "ko" if language == "ko" else "en"
    filename = f"_posts/{today}-tech-update-{suffix}.md"

    if language == "ko":
        title = f"# 🛠️ {today} 기술 업데이트 요약"
    else:
        title = f"# 🛠️ {today} Tech Update Summary"

    content = title + "\n\n"

    for post in posts:
        if language == "ko":
            content += f"## 🔹 {post['title']}\n{post['summary']}\n👉 [자세히 보기]({post['link']})\n\n"
        else:
            content += f"## 🔹 {post['title']}\n{post['summary']}\n👉 [Read more]({post['link']})\n\n"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    collected_ko = []
    collected_en = []

    for name, url in feeds.items():
        feed = feedparser.parse(url)
        if not feed.entries:
            continue
        latest = feed.entries[0]

        # summary 안전하게 가져오기
        summary_text = getattr(latest, "summary", "") if hasattr(latest, "summary") else latest.get("summary", "")

        summary_ko = summarize(latest.title, latest.link, summary_text, language="ko")
        summary_en = summarize(latest.title, latest.link, summary_text, language="en")

        collected_ko.append({
            'title': f"{name} - {latest.title}",
            'link': latest.link,
            'summary': summary_ko
        })

        collected_en.append({
            'title': f"{name} - {latest.title}",
            'link': latest.link,
            'summary': summary_en
        })

    generate_markdown(collected_ko, language="ko")
    generate_markdown(collected_en, language="en")

if __name__ == "__main__":
    main()