# 🛠️ 2025-07-08 기술 업데이트 요약

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
이 블로그 글은 Kubernetes에서 GPU와 같은 특수 하드웨어를 사용하는 포드의 실패 처리 문제를 다룹니다. AI/ML 작업이 증가하면서 이러한 특수 하드웨어의 실패는 성능 저하와 중단을 유발할 수 있습니다. Kubernetes는 리소스를 정적으로 관리하기 때문에 하드웨어 실패를 잘 처리하지 못하는데, 이는 AI/ML 작업에서 큰 문제가 됩니다. 블로그는 현재의 문제점과 DIY 솔루션을 설명하고, 향후 Kubernetes가 이러한 문제를 어떻게 개선할 것인지에 대한 로드맵을 제시합니다. Kubernetes는 여전히 AI/ML 작업을 위한 주요 플랫폼으로, 이러한 문제에 대한 솔루션을 개발하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - Spring gRPC 0.9.0 available now
Spring gRPC 0.9.0 버전이 출시되었습니다. 이 버전은 Maven Central에서 다운로드할 수 있으며, Spring Boot 4.0.0 출시 시기에 맞춰 1.0.0 버전도 계획 중입니다. 주요 변경 사항으로는 Spring Boot 3.5로 업그레이드, `StubFactory` 계약 변경, `GrpcClientFactoryCustomizer`가 `GrpcChannelBuilderCustomizer`로 대체된 것, in-process gRPC 클라이언트에서 인터셉터를 필터링할 수 있는 기능 추가 등이 있습니다. 또한, 글로벌 인터셉터와 서비스 정의를 필터링할 수 있는 기능도 추가되었습니다. 도움이 필요하시다면 GitHub 이슈를 확인하거나 Stack Overflow에서 `spring-grpc` 태그를 사용해 질문할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/04/spring-grpc-0-9-0-available-now)

## 🔹 Docker - From Dev to Deploy: Compose as the Spine of the Application Lifecycle
이 기술 블로그 글은 애플리케이션 개발 과정에서 Docker Compose가 중요한 역할을 한다는 내용을 다룹니다. '척추'에 비유하여 설명하듯이, Docker Compose는 애플리케이션의 전체 수명 주기를 지원하고 강화하는 핵심 요소로 작용합니다. 이를 통해 개발 과정에서 발생할 수 있는 여러 문제를 효율적으로 관리하고, 애플리케이션의 안정성과 이해도를 높일 수 있음을 강조하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-compose-powering-the-full-app-lifecycle/)

## 🔹 Java - The Inside Java Newsletter: Contribute to Learn.java!
Inside Java 뉴스레터의 2025년 6월 호에서는 학생, 교사, 개발자 등 전 세계 학습자를 지원하기 위한 새로운 웹사이트인 Learn.java에 대해 다루고 있습니다. 이번 호의 주요 기사에서는 Learn.java에 대한 특별 기고 요청이 있습니다. 또한 여러 팟캐스트 인터뷰, 커뮤니티 소식, Java의 혁신에 대한 최신 기술 비디오도 소개됩니다. Java 30주년 기념 행사도 계속되고 있으며, 최근의 주요 연설 세션들이 강조되어 있습니다. 이 뉴스레터는 Java 개발자 관계 팀에서 제작하며 Java 플랫폼 그룹과 커뮤니티의 활동을 다룹니다. 아카이브를 확인하고, 구독하며, 친구에게 공유할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/07/inside-java-newsletter/)

## 🔹 Golang - Generic interfaces
블로그 글 "Generic interfaces"는 인터페이스 타입에 타입 매개변수를 추가하는 것이 얼마나 강력한지를 설명합니다. 이를 통해 코드의 유연성과 재사용성을 크게 향상시킬 수 있으며, 다양한 타입을 보다 효율적으로 처리할 수 있게 됩니다. 이 글에서는 이러한 개념의 이점과 활용 방법에 대해 다루고 있습니다.
👉 [자세히 보기](https://go.dev/blog/generic-interfaces)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의를 위해 유지관리자들과의 토크 세션 및 프로젝트 파빌리온에 있는 Helm 부스에서 참여할 수 있습니다. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

