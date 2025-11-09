# 🛠️ 2025-11-09 기술 업데이트 요약

## 🔹 Kubernetes - Gateway API 1.4: New Features
Gateway API 1.4.0은 Kubernetes 네트워킹을 강화하는 최신 기능을 제공합니다. 이번 릴리스에서는 세 가지 새로운 표준 기능과 세 가지 실험적 기능이 도입되었습니다. 표준 기능에는 게이트웨이와 백엔드 간 TLS 정책, GatewayClass의 지원 기능, 라우트의 명명된 규칙이 포함됩니다. 실험적 기능에는 서비스 메쉬 구성을 위한 메쉬 리소스, 기본 게이트웨이, HTTPRoute에 대한 외부 인증 필터가 포함됩니다. 또한, 클라이언트 인증서 검증 구성을 개선하여 보안 취약점을 해결하고, GRPCRoute와 HTTPRoute에 대한 몇 가지 기술적 변경 사항을 포함하고 있습니다. 개발자 경험을 향상시키기 위해 다양한 개선사항도 추가되었습니다. Kubernetes 1.26 이상 사용자들은 최신 Gateway API를 사용할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/06/gateway-api-v1-4/)

## 🔹 Spring Boot - Spring AI 1.1.0-RC1 Available Now
Spring AI 1.1.0-RC1 버전이 출시되었습니다. 이 버전은 안정성 향상과 버그 수정에 중점을 두고 있으며, 총 40개의 개선 사항, 버그 수정 및 문서 업데이트가 포함되어 있습니다. 주요 개선 사항으로는 기능 확장, 보안 개선을 위한 종속성 업데이트, OpenAI API의 reasoningContent 지원, MongoDB를 통한 대화 기록 저장 등이 있습니다. 또한, 자동 네트워크 재시도 기능이 추가되어 분산형 배포에서의 복원력이 향상되었습니다. Spring AI 팀은 앞으로도 Spring Boot를 활용한 AI 애플리케이션 개발을 지속적으로 개선할 예정이며, 곧 1.1.0 GA 버전 출시를 계획하고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/08/spring-ai-1-1-0-RC1-available-now)

## 🔹 Docker - Most DevSecOps Advice Is Useless without Context—Here’s What Actually Works
블로그 글의 요약: 일반적인 DevSecOps 조언은 문서상으로는 그럴듯해 보일 수 있지만, 실제로는 팀의 상황, 워크플로우, 환경에 맞는 필요성을 무시하기 때문에 실패하는 경우가 많습니다. 과도한 통제, 광범위한 정책, 잘못 적용된 도구는 개발 흐름을 방해하며, 흐름이 깨지면 보안 조치가 가장 먼저 무시됩니다. 해결책은 더 많은 규칙이 아니라 더 스마트한 접근 방식입니다.
👉 [자세히 보기](https://www.docker.com/blog/context-aware-devsecops-what-works/)

## 🔹 Java - Pulling the (Foreign) String
이 기술 블로그 글은 "Pulling the (Foreign) String"이라는 제목으로, Foreign Function & Memory (FFM) API가 메모리 세그먼트에서 문자열을 읽고 쓰는 방법과 기존 Java 문자열에서 메모리 세그먼트를 할당하는 방법을 제공하는 것에 대해 설명합니다. 문서에서는 문자열과 메모리 세그먼트 간의 상호 운용성을 더욱 효율적으로 지원하기 위해 FFM API를 개선하는 방법을 탐구합니다.
👉 [자세히 보기](https://inside.java/2025/11/08/ffm-string/)

## 🔹 Golang - The Green Tea Garbage Collector
Go 1.25 버전에는 새로운 실험적 가비지 컬렉터인 'Green Tea'가 포함되었습니다. 이 블로그 글은 해당 가비지 컬렉터의 특징과 기능에 대해 설명하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/greenteagc)

