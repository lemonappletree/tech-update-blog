# 🛠️ 2025-09-08 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Pod Replacement Policy for Jobs Goes GA
Kubernetes v1.34 버전에서는 작업에 대한 Pod 교체 정책 기능이 일반 가용성(GA) 단계에 도달했습니다. 기본적으로 Job 컨트롤러는 Pod가 실패하거나 종료되기 시작하면 즉시 재생성합니다. 이는 특정 상황에서 문제가 될 수 있는데, 예를 들어 TensorFlow와 같은 머신러닝 프레임워크는 정확히 하나의 Pod만 작업자 인덱스에 기대합니다. Pod 교체 정책을 통해 사용자는 Pod가 종료되는 시점을 제어할 수 있습니다. 두 가지 정책(종료 또는 실패 시 교체, 완전히 실패한 후 교체) 중에서 선택할 수 있으며, 이를 통해 불필요한 Pod 중복 실행을 방지할 수 있습니다. 예시로, 두 번의 작업을 병렬로 실행하고 Pod가 완전히 종료된 후 교체하는 Job 설정이 소개되었습니다. 이 기능의 발전에 기여한 여러 사람들에게 감사의 말을 전하며, Kubernetes 커뮤니티와 함께 새로운 기능 개발에 참여할 수 있는 방법도 안내하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/05/kubernetes-v1-34-pod-replacement-policy-for-jobs-goes-ga/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Cloud guru Ryan Baxter
이 블로그 글은 "A Bootiful Podcast" 시리즈의 일부로, Spring Cloud의 기여자인 Ryan Baxter와의 대화를 다루고 있습니다. 이 인터뷰는 SpringOne 2025 행사에서 진행되었습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/04/a-bootiful-podcast-ryan-baxter)

## 🔹 Docker - Docker Acquisition of MCP Defender Helps Meet Challenges of Securing the Agentic Future
Docker, Inc.는 클라우드 네이티브 및 AI 네이티브 개발 도구, 인프라, 서비스를 제공하는 회사로, AI 애플리케이션 보안을 위해 설립된 MCP Defender를 인수했다고 발표했습니다. AI의 빠른 발전은 소프트웨어 개발을 혁신적으로 변화시켰지만, 강력한 새로운 기술은 새로운 보안 과제를 동반합니다. Docker는 이 인수를 통해 AI 에이전트의 미래를 안전하게 구축하는 데 기여하려고 합니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/)

## 🔹 Java - How to Handle Security Changes in Java 25 #RoadTo25
이 기술 블로그 글은 Java 25에서의 보안 변경 사항에 대한 내용을 다룹니다. Java 플랫폼은 지속적으로 보안 태세를 강화하고 있으며, 이는 오래된 알고리즘의 사용 중단, 구식 메커니즘의 단계적 제거, 최신 암호화 표준의 통합을 통해 이루어집니다. Ana는 JDK 21 이후 도입된 주요 보안 변경 사항을 검토하고, 이러한 업데이트에 대비하여 애플리케이션을 준비하는 방법을 설명합니다. 그녀는 런타임 보안 설정을 검토하고 조정하는 방법과 양자 컴퓨터 공격에 대비하여 안전한 새로운 세대의 표준인 포스트 양자 암호화에 애플리케이션을 준비시키는 방법에 중점을 둡니다.
👉 [자세히 보기](https://inside.java/2025/09/07/roadto25-security/)

## 🔹 Golang - Testing Time (and other asynchronicities)
이 블로그 글은 비동기 코드 테스트와 `testing/synctest` 패키지에 대한 탐구를 다루고 있습니다. 2025년 유럽 고퍼콘에서 같은 제목으로 발표된 내용을 바탕으로 작성되었습니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
제목: Debian/Ubuntu Helm Apt 저장소 이동

요약: Apt를 사용하여 Helm을 설치하는 경우, Debian/Ubuntu Helm Apt 저장소가 이전됨을 주의해야 합니다. 이전에는 Balto에서 호스팅되었으나, 이제 Buildkite에서 호스팅됩니다. APT 키와 저장소에 대한 참조를 새로운 설치 지침을 사용하여 업데이트하세요.
👉 [자세히 보기](https://helm.sh/blog/debian-helm-repository-move/)

