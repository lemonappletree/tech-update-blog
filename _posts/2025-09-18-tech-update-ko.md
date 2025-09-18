# 🛠️ 2025-09-18 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Pods Report DRA Resource Health
이 블로그 글은 Kubernetes v1.34 버전의 새로운 알파 기능에 대해 다루고 있습니다. AI/ML과 같은 고성능 작업 부하로 인해 GPU, TPU, FPGA와 같은 특수 하드웨어가 Kubernetes 클러스터에서 중요해졌습니다. 하지만 이러한 하드웨어가 실패하면 진단이 어렵고, 이는 상당한 다운타임을 초래할 수 있습니다. 이번 릴리스에서는 장치의 상태를 Pod의 상태 필드에 직접 보고할 수 있는 기능이 추가되어, 운영자와 개발자에게 중요한 인사이트를 제공합니다. 이 기능은 Device Plugin이 관리하는 장치의 상태를 보고하는 메커니즘을 도입한 KEP-4680의 기능을 확장하여, Dynamic Resource Allocation(DRA)에도 적용됩니다. 새로운 gRPC 서비스와 Kubelet 통합을 통해, Pod 상태에 장치 건강 정보를 포함시켜 문제가 있는 장치가 원인인지 신속히 파악할 수 있습니다. 이 기능은 현재 알파 단계이며, 사용하려면 특정 설정이 필요합니다. 향후 베타 단계로 발전시키기 위해 커뮤니티 피드백이 중요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/17/kubernetes-v1-34-pods-report-dra-resource-health/)

## 🔹 Spring Boot - Spring AI 1.0.2 Available Now
Spring AI 1.0.2 버전이 출시되어 Maven Central에서 이용 가능합니다. 이번 패치 릴리스에서는 중요 안정성 개선과 버그 수정이 이루어졌으며, 총 91개의 개선 사항과 문서 업데이트가 포함되었습니다. 주요 개선 사항으로는 GPT-5 모델 지원, MariaDB 벡터 유사성 점수, Kotlin 데이터 클래스 JSON 스키마 지원 등이 추가되었습니다. 또한, 오류 처리 향상, 스레드 안전한 날짜 형식화, 향상된 null 안전성 등의 버그 수정도 이루어졌습니다. 보안 업데이트와 성능 향상도 포함되어 있습니다. 이번 릴리스에 기여한 모든 분들께 감사드립니다. 자세한 릴리스 노트는 관련 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/17/spring-ai-1-0-2-available-now)

## 🔹 Docker - How to Build Secure AI Coding Agents with Cerebras and Docker Compose
이 글은 Cerebras와 Docker Compose를 활용하여 안전한 AI 코딩 에이전트를 구축하는 방법에 대해 설명합니다. Cerebras는 세계에서 가장 빠른 AI 추론 API를 제공하며, 이를 Docker Compose, ADK-Python, MCP 서버와 결합하여 격리된 AI 코드 환경을 구축하는 방법을 소개했습니다. 이 블로그 글에서는 이러한 기술의 기본 원리를 더 깊이 탐구하고 각 요소들이 어떻게 상호작용하는지를 설명합니다.
👉 [자세히 보기](https://www.docker.com/blog/cerebras-docker-compose-secure-ai-coding-agents/)

## 🔹 Java - Detaching GraalVM from the Java Ecosystem Train
기술 블로그 글의 요약: 이 글은 GraalVM의 릴리스 주기가 Java SE 릴리스 주기에서 독립적으로 진화하고 있다는 소식을 전합니다. 이를 통해 다양한 언어와 플랫폼을 지원하는 GraalVM의 생태계를 더 잘 지원할 수 있게 됩니다.
👉 [자세히 보기](https://inside.java/2025/09/17/detaching-graalvm-java-ecosystem/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
제목: 설문 조사 시간입니다! Go 언어는 당신에게 어떻게 작용하고 있나요?
요약: Go 언어의 미래를 형성하는 데 도움을 주세요.
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기에 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지를 공유하고자 합니다. 자세한 내용은 [블로그 글](https://helm.sh/blog/path-to-helm-v4/)에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

