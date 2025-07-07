# 🛠️ 2025-07-07 기술 업데이트 요약

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
이 블로그 글은 Kubernetes 환경에서 GPU와 같은 특수 하드웨어를 사용하는 파드에서 발생할 수 있는 실패 모드를 다루고 있습니다. AI/ML 워크로드의 증가로 인해 이러한 하드웨어의 중요성이 커지면서, 하드웨어 오류가 성능에 미치는 영향이 커졌습니다. Kubernetes는 여전히 AI/ML 워크로드를 위한 주요 플랫폼이지만, 하드웨어 오류 처리에 대한 지원이 부족합니다.

블로그에서는 다양한 실패 모드와 DIY 솔루션을 설명하며, 특히 Kubernetes 인프라, 디바이스 실패, 컨테이너 코드 실패, 디바이스 성능 저하와 관련된 문제를 다룹니다. 또한, 향후 Kubernetes 커뮤니티가 해결해야 할 개선 사항과 로드맵을 제시합니다. 

Kubernetes는 AI/ML 워크로드의 복잡한 요구 사항을 충족하기 위해 지속적으로 확장점을 개선하고 있으며, 커뮤니티의 피드백과 참여를 요청하고 있습니다. 이 블로그는 이러한 문제를 해결함으로써 Kubernetes가 AI/ML 워크로드에서의 지배적인 플랫폼으로 자리 잡을 수 있도록 기여하고자 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - Spring gRPC 0.9.0 available now
Spring gRPC 0.9.0 버전이 출시되었습니다. 이번 릴리스에서는 Spring Boot 3.5로 업그레이드되었으며, `StubFactory` 계약의 변경, `GrpcClientFactoryCustomizer` 대신 `GrpcChannelBuilderCustomizer` 사용, 인프로세스 gRPC 클라이언트의 인터셉터 필터링 기능 추가, `InProcessGrpcServer`와 `NettyGrpcServer`에서 전역 인터셉터 및 서비스 정의 필터링 기능 추가 등이 주요 변경 사항입니다. 더 많은 정보를 원하거나 기여를 원하시면 GitHub 이슈 페이지를 참조하세요.
👉 [자세히 보기](https://spring.io/blog/2025/07/04/spring-grpc-0-9-0-available-now)

## 🔹 Docker - 5 Best Practices for Building, Testing, and Packaging MCP Servers
제목: MCP 서버 구축, 테스트 및 패키징을 위한 5가지 모범 사례

요약: 최근에 새로운 Docker MCP 카탈로그를 출시하여 발견 기능을 개선하고 새로운 제출 프로세스를 도입했습니다. 컨테이너화된 MCP 서버는 에이전트 애플리케이션을 안전하게 실행하고 확장할 수 있는 방법을 제공하며, 호스트 접근 및 비밀 관리와 관련된 위험을 최소화합니다. 개발자는 두 가지 방법으로 서버를 제출할 수 있는데, 하나는 Docker로 빌드된 서버로, 전체 보안 스위트를 포함하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/mcp-server-best-practices/)

## 🔹 Java - Java 25 is ALSO no LTS Version - Inside Java Newscast #94
블로그 글 요약: Java 25는 Java 21과 마찬가지로 "장기 지원 버전"이라고 설명될 수 있지만, 이는 사실이 아닙니다. Java 표준을 관리하는 JCP나 참조 구현을 개발하는 OpenJDK에는 "지원"이라는 개념이 없습니다. 이 용어가 어떻게 생겨났고, 왜 중요한지에 대해 설명합니다.
👉 [자세히 보기](https://inside.java/2025/07/03/newscast-94/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
블로그 글은 Go 팀이 오류 처리에 대한 문법적 지원을 계획하고 있다는 내용을 담고 있습니다. 이 글에서는 Go 언어의 오류 처리 방식에 대한 논의와 앞으로의 계획을 다루고 있습니다. 현재 Go 팀은 오류 처리에 대한 문법적 지원을 추가할지 여부를 고려 중이며, 이에 대한 다양한 의견과 아이디어를 수렴하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4와 관련하여 유지보수자들과 대화할 수 있는 기회가 마련되어 있으며, Project Pavilion에 있는 Helm 부스에서도 다양한 활동이 진행됩니다. 자세한 정보는 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

