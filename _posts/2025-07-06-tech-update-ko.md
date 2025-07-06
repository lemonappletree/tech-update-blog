# 🛠️ 2025-07-06 기술 업데이트 요약

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
이 블로그 글은 Kubernetes에서 GPU와 같은 특수 하드웨어를 사용하는 파드의 실패 모드를 관리하는 데 있어 겪는 어려움과 해결책에 대해 설명합니다. AI/ML 워크로드의 증가로 인해 Kubernetes가 직면한 새로운 도전 과제를 다루며, 특히 하드웨어 고장 시 성능에 미치는 영향을 강조합니다. Kubernetes는 여전히 AI/ML 워크로드를 위한 주요 플랫폼으로 자리잡고 있으며, 다양한 실패 모드에 대한 현재 상태와 문제 해결을 위한 모범 사례를 제시합니다. 또한, 향후 개선 사항과 관련된 로드맵을 제공하며, Kubernetes 커뮤니티의 참여를 독려합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - Spring gRPC 0.9.0 available now
Spring gRPC 0.9.0 버전이 출시되어 Maven Central에서 이용 가능합니다. 이번 릴리스에서는 Spring Boot 3.5로 업그레이드되었으며, `StubFactory` 계약 변경, `GrpcClientFactoryCustomizer` 제거 및 `GrpcChannelBuilderCustomizer` 도입, gRPC 클라이언트에서 인터셉터 필터링 기능 추가 등의 주요 변경 사항이 포함되었습니다. 또한 `InProcessGrpcServer`와 `NettyGrpcServer`에 대한 전역 인터셉터와 서비스 정의 필터링 기능이 추가되었습니다. 도움이 필요하다면 GitHub 이슈를 확인하거나 Stack Overflow에서 `spring-grpc` 태그를 사용해 질문할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/04/spring-grpc-0-9-0-available-now)

## 🔹 Docker - 5 Best Practices for Building, Testing, and Packaging MCP Servers
블로그 글에서는 Docker MCP Catalog의 새로운 출시와 함께 MCP 서버의 빌드, 테스트, 패키징을 위한 5가지 모범 사례를 소개합니다. 컨테이너화된 MCP 서버는 에이전트 애플리케이션을 안전하게 실행하고 확장할 수 있으며, 호스트 접근 및 비밀 관리와 관련된 위험을 최소화합니다. 개발자는 두 가지 방법으로 서버를 제출할 수 있으며, 그 중 하나는 Docker에서 빌드된 서버로, 이는 전체 보안 스위트를 포함합니다.
👉 [자세히 보기](https://www.docker.com/blog/mcp-server-best-practices/)

## 🔹 Java - Java 25 is ALSO no LTS Version - Inside Java Newscast #94
블로그 글 요약: Java 25는 Java 21과 마찬가지로 "장기 지원 버전"으로 설명될 것이지만, 이는 잘못된 표현입니다. Java 표준을 관리하는 JCP나 참조 구현을 개발하는 OpenJDK 모두 "지원"의 개념을 알지 못합니다. 이 혼동의 출처와 그 중요성을 설명합니다.
👉 [자세히 보기](https://inside.java/2025/07/03/newscast-94/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
이 블로그 글은 Go 팀의 오류 처리 지원 계획에 대해 다루고 있습니다. Go 언어에서의 오류 처리에 대한 문법적 지원에 관한 논의와 결정 사항을 설명하고 있으며, 오류 처리를 개선하기 위한 다양한 접근 방식과 그에 따른 장단점을 검토합니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시될 예정인 Helm 4에 대한 논의에 참여하고, 유지보수자들과의 대화 세션 및 Helm 부스를 통해 다양한 활동에 참여할 수 있습니다. 주간 동안 모든 Helm 관련 활동에 대한 자세한 정보는 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

