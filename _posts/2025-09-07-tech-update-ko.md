# 🛠️ 2025-09-07 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Pod Replacement Policy for Jobs Goes GA
Kubernetes v1.34에서 Pod 교체 정책 기능이 일반적으로 사용 가능하게 되었습니다. 이 기능은 Job 실행 시 Pod가 실패하거나 종료될 때 새로운 Pod로 대체되는 방식을 제어할 수 있도록 합니다. 기본적으로 Job 컨트롤러는 Pod가 실패하거나 종료되기 시작하면 즉시 새 Pod를 생성하지만, 이는 머신러닝 프레임워크와 같은 특정 워크로드에서 문제가 될 수 있습니다. Pod 교체 정책은 `.spec.podReplacementPolicy` 필드를 통해 설정할 수 있으며, Pod가 완전히 종료된 후에만 교체가 이루어지도록 설정할 수 있습니다. 이 기능은 Kubernetes 사용자에게 Pod 교체 시점을 제어할 수 있는 능력을 제공하여 불필요한 클러스터 확장 및 자원 낭비를 방지합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/05/kubernetes-v1-34-pod-replacement-policy-for-jobs-goes-ga/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Cloud guru Ryan Baxter
Spring 블로그 글 요약: 이 글에서는 SpringOne 2025 행사에서 Spring Cloud의 뛰어난 기여자인 Ryan Baxter와의 인터뷰 내용을 다루고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/04/a-bootiful-podcast-ryan-baxter)

## 🔹 Docker - Docker Acquisition of MCP Defender Helps Meet Challenges of Securing the Agentic Future
Docker, Inc.는 AI 애플리케이션 보안을 위해 설립된 MCP Defender를 인수했다고 발표했습니다. AI의 빠른 발전은 소프트웨어 개발을 혁신적으로 변화시켰으며, 이로 인해 새로운 보안 과제가 발생했습니다. Docker는 이러한 도전을 해결하기 위해 클라우드 및 AI 네이티브 개발 도구, 인프라 및 서비스를 제공하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/)

## 🔹 Java - Java 21 ⮕ 25: Performance and Runtime Enhancements #RoadTo25
이 기술 블로그 글은 Java 21에서 Java 25로의 성능 및 런타임 향상에 대해 다루고 있습니다. 각 Java 버전마다 성능과 런타임 업데이트가 포함되어 있으며, Java 21에서 25로 업그레이드하는 조직은 많은 릴리스 노트를 검토해야 합니다. ACME Soft의 Billy Korando가 주요 성능 및 런타임 업데이트를 정리해 주어 이를 쉽게 이해할 수 있도록 도와줍니다. Compact Object Headers, ZGC 및 JFR 업데이트 등 알아야 할 주요 업데이트를 소개합니다.
👉 [자세히 보기](https://inside.java/2025/09/05/roadto25-performance/)

## 🔹 Golang - Testing Time (and other asynchronicities)
블로그 글 "Testing Time (and other asynchronicities)"는 비동기 코드 테스트 방법과 `testing/synctest` 패키지에 대한 탐구를 다룹니다. 이 글은 GopherCon Europe 2025에서 같은 제목으로 발표된 내용을 바탕으로 작성되었습니다. 비동기 코드 테스트의 중요성과 이를 보다 효과적으로 수행하기 위한 도구 및 기법을 소개합니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
제목: Debian/Ubuntu Helm Apt 저장소 이동

요약: Apt를 사용하여 Helm을 설치하는 경우, Debian/Ubuntu Helm Apt 저장소가 이전된다는 점에 유의해야 합니다. 이전에는 Balto에서 호스팅되었으나, 이제는 Buildkite에서 호스팅될 예정입니다. 새로운 설치 지침을 참고하여 APT 키와 저장소에 대한 참조를 업데이트하세요.

링크: [블로그 글](https://helm.sh/blog/debian-helm-repository-move/)
👉 [자세히 보기](https://helm.sh/blog/debian-helm-repository-move/)

