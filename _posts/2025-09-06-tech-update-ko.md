# 🛠️ 2025-09-06 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Pod Replacement Policy for Jobs Goes GA
Kubernetes v1.34 버전에서 'Pod 교체 정책' 기능이 일반 가용성(GA) 단계에 도달했습니다. 이 기능은 Job 컨트롤러가 Pod가 실패하거나 종료 상태에 돌입할 때 즉시 새로운 Pod를 생성하는 기본 동작을 제어할 수 있게 합니다. 두 가지 정책 옵션은 'TerminatingOrFailed'과 'Failed'로, 각각 Pod가 종료되기 시작할 때 또는 완전히 종료된 후에만 새로운 Pod를 생성하도록 설정할 수 있습니다. 이 기능은 특히 TensorFlow와 같은 머신러닝 프레임워크에서 중복 Pod 실행 문제를 방지하는 데 유용합니다. Kubernetes 사용자 문서와 KEPs를 통해 더 많은 정보를 얻을 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/05/kubernetes-v1-34-pod-replacement-policy-for-jobs-goes-ga/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Cloud guru Ryan Baxter
기술 블로그 글 요약:  
이 블로그 글에서는 SpringOne 2025 행사에서 라이브로 진행된 팟캐스트에서 Spring Cloud의 뛰어난 기여자인 라이언 백스터와의 대화를 다루고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/04/a-bootiful-podcast-ryan-baxter)

## 🔹 Docker - Docker Acquisition of MCP Defender Helps Meet Challenges of Securing the Agentic Future
Docker, Inc.는 AI 애플리케이션 보안을 전문으로 하는 MCP Defender를 인수했다고 발표했습니다. AI 기술의 급속한 발전은 소프트웨어 개발 방식에 큰 변화를 가져왔으며, 이러한 강력한 기술의 발전은 새로운 보안 과제를 동반합니다. Docker는 이번 인수를 통해 클라우드 및 AI 네이티브 개발 도구와 인프라, 서비스를 강화하고, 안전한 AI 애플리케이션 개발을 지원하고자 합니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-acquires-mcp-defender-ai-agent-security/)

## 🔹 Java - Java 21 ⮕ 25: Performance and Runtime Enhancements #RoadTo25
이 블로그 글은 Java 21에서 25로 업그레이드할 때 알아야 할 성능 및 런타임 개선 사항을 다룹니다. 각 Java 버전은 성능 및 런타임 업데이트를 포함하고 있으며, 이로 인해 많은 릴리스 노트를 검토해야 합니다. ACME Soft의 Billy Korando가 주요 성능 및 런타임 업데이트를 정리해 주었으며, Compact Object Headers, ZGC 및 JFR 업데이트 등을 포함한 핵심 업데이트를 다루고 있습니다. 이 글에서는 이러한 중요한 변경 사항을 쉽게 이해할 수 있도록 설명합니다.
👉 [자세히 보기](https://inside.java/2025/09/05/roadto25-performance/)

## 🔹 Golang - Testing Time (and other asynchronicities)
블로그 글 "Testing Time (and other asynchronicities)"는 비동기 코드 테스트에 대해 논의하고 `testing/synctest` 패키지를 탐구합니다. 이 글은 GopherCon Europe 2025에서 같은 제목으로 진행된 발표를 기반으로 하고 있습니다. 이 블로그는 비동기 코드의 테스트 방법과 관련된 다양한 기법과 도구를 소개하고, 이를 효과적으로 구현하는 방법에 대해 설명합니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Debian/Ubuntu Helm Apt Repository Move
제목: Debian/Ubuntu Helm Apt 저장소 이전

요약: Apt를 사용하여 Helm을 설치하는 경우, Debian/Ubuntu Helm Apt 저장소가 이전되고 있다는 점을 유의해야 합니다. 기존에는 Balto에서 호스팅되었으나 이제는 Buildkite에서 호스팅됩니다. 새로운 설치 지침을 참고하여 APT 키와 저장소에 대한 참조를 업데이트하세요.
👉 [자세히 보기](https://helm.sh/blog/debian-helm-repository-move/)

