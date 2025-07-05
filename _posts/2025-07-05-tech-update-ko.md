# 🛠️ 2025-07-05 기술 업데이트 요약

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
이 기술 블로그 글은 Kubernetes에서 GPU와 같은 특수 하드웨어를 다루는 Pod의 실패 처리에 대한 복잡한 문제를 다루고 있습니다. AI/ML 워크로드의 증가로 인해 Kubernetes는 새로운 도전에 직면하게 되었으며, 하드웨어 실패는 성능에 큰 영향을 미치고 중단을 초래할 수 있습니다. Kubernetes의 자원 처리 방식은 여전히 정적이며, 하드웨어 실패에 대한 지원이 부족합니다.

AI/ML 워크로드는 특수한 하드웨어와 까다로운 스케줄링 요구사항을 가지며, 이러한 워크로드에서는 기존의 가정이 깨지는 경우가 많습니다. Kubernetes는 여전히 AI/ML 워크로드의 플랫폼으로 널리 사용되고 있으며, 많은 확장 포인트를 제공해 DIY 솔루션을 구현할 수 있습니다. 그러나 이러한 솔루션은 비용이 많이 들고, Kubernetes는 이러한 문제를 해결하기 위한 로드맵을 개발 중입니다.

블로그는 또한 Kubernetes의 현재 상태, 다양한 실패 모드, 그리고 이러한 문제를 해결하기 위한 모범 사례와 DIY 솔루션을 설명합니다. Kubernetes 커뮤니티는 이러한 문제에 대한 피드백과 참여를 장려하며, AI/ML 워크로드를 위한 최고의 플랫폼으로 자리매김하기 위해 노력하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - Spring gRPC 0.9.0 available now
Spring gRPC 0.9.0 버전이 출시되었습니다. 주요 변경 사항으로는 Spring Boot 3.5로의 업그레이드, `StubFactory` 계약 변경(정적 메서드로 변경), `GrpcClientFactoryCustomizer`의 제거 및 `GrpcChannelBuilderCustomizer`로 대체, 인프로세스 gRPC 클라이언트에서 인터셉터 필터링 기능 추가, 글로벌 인터셉터 및 서비스 정의 필터링 기능 추가 등이 있습니다. 추가적으로, 참여를 원하는 사람들은 GitHub에서 이슈를 확인하거나 Stack Overflow에서 질문할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/04/spring-grpc-0-9-0-available-now)

## 🔹 Docker - 5 Best Practices for Building, Testing, and Packaging MCP Servers
제목: MCP 서버 구축, 테스트 및 패키징을 위한 5가지 모범 사례

요약: 우리는 최근에 개선된 검색 기능과 새로운 제출 프로세스를 포함한 새로운 Docker MCP 카탈로그를 출시했습니다. 컨테이너화된 MCP 서버는 에이전트 기반 애플리케이션을 안전하게 실행하고 확장하며, 호스트 접근 및 비밀 관리와 관련된 위험을 최소화하는 방법을 제공합니다. 개발자는 Docker가 구축한 서버를 포함하여 전체 보안 스위트를 갖춘 서버를 제출할 수 있는 두 가지 방법으로 서버를 제출할 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/mcp-server-best-practices/)

## 🔹 Java - Java 25 is ALSO no LTS Version - Inside Java Newscast #94
블로그 글은 Java 25가 Java 21과 마찬가지로 "장기 지원 버전"으로 설명되지만, 이는 사실과 다르다는 내용을 담고 있습니다. Java 표준을 관리하는 JCP나 참조 구현을 개발하는 OpenJDK는 "지원"이라는 개념을 알지 못합니다. 이 개념이 어디에서 비롯되었는지, 그리고 왜 중요한지를 설명하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/03/newscast-94/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
Go 팀은 오류 처리에 대한 구문 지원 계획을 논의하고 있습니다. 이 블로그 글에서는 Go 언어의 오류 처리 메커니즘에 대한 현재 상태와 향후 개선 방향에 대한 계획이 설명되어 있습니다. Go 팀은 오류 처리를 보다 효율적이고 직관적으로 만들기 위한 여러 가지 옵션을 검토하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 주어지며, 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과 대화할 수 있습니다. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 본문을 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

