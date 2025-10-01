# 🛠️ 2025-10-01 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 기술 블로그 글에서는 Kubernetes 저장소 생태계에 대한 새로운 기능인 '변경된 블록 추적(Changed Block Tracking) API'의 알파 지원을 발표합니다. 이 기능을 통해 CSI 저장소 드라이버가 PersistentVolume 스냅샷에서 변경된 블록을 효율적으로 식별할 수 있게 되어, 백업 작업이 더 빠르고 자원 효율적으로 진행될 수 있습니다. 변경된 블록 추적은 스냅샷 사이의 블록 수준에서 수정 사항을 추적하여 백업 시 전체 볼륨을 스캔할 필요를 없애줍니다. 이 기능은 현재 블록 볼륨에 대해서만 지원되며, 파일 기반 저장소 시스템에는 적용되지 않습니다. Kubernetes 사용자는 이 API를 통해 더 효율적인 백업 프로세스를 구현할 수 있으며, 이는 특히 큰 데이터 세트를 관리하는 사용자에게 유용합니다. 향후 피드백과 채택에 따라 이 기능을 베타 버전으로 발전시키고자 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Securing MCP Servers with Spring AI
이 기술 블로그 글은 "Spring AI"를 사용하여 MCP(Model Context Protocol) 서버의 보안을 강화하는 방법을 설명합니다. MCP는 AI 분야에서 중요한 프로토콜로, 최신 버전의 사양이 에코시스템에서 더 많은 지원을 받고 있습니다. 이를 위해 GitHub에 전용 프로젝트가 만들어졌으며, Spring AI 1.1.x 기반 애플리케이션에 추가할 수 있는 첫 릴리스가 제공됩니다.

글에서는 OAuth2를 사용하여 MCP 서버를 보호하는 방법, MCP 호환 Spring Authorization Server를 구축하는 방법, 그리고 OAuth2 대신 API 키를 사용하여 MCP 서버를 보호하는 방법을 다룹니다. 예를 들어, OAuth2를 통해 MCP 서버는 HTTP를 통해 노출된 경우 반드시 OAuth2 액세스 토큰으로 보호되어야 하며, API 키를 사용하는 경우에는 특정 헤더를 통해 인증을 수행할 수 있습니다.

글의 주요 포인트는 Spring AI와 Spring Security를 활용하여 MCP 서버의 보안을 강화하는 다양한 방법과 이를 설정하고 사용하는 방법을 설명하는 것입니다. 추가로, Spring Authorization Server를 사용하여 MCP 호환 인증 서버를 구축하는 방법도 소개합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/30/spring-ai-mcp-server-security)

## 🔹 Docker - Expanding Docker Hardened Images: Secure Helm Charts for Deployments
이 블로그 글은 소프트웨어 공급망 보안의 중요성이 커짐에 따라 개발 팀이 신뢰할 수 있는 이미지와 간소화된 배포, 규제 준수 도구를 필요로 한다는 점을 강조합니다. 고객들은 일회성 공급업체가 아닌, 개발과 배포 전반에서 신뢰할 수 있는 보안 파트너를 찾고 있다고 말합니다. 이러한 요구에 따라 Docker는 강화된 이미지를 제공하고 Helm 차트를 활용한 보안 배포 솔루션을 제안합니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-hardened-images-helm-charts-beta/)

## 🔹 Java - Episode 40 “Amber &amp; Valhalla - Incremental Design and Feature Arcs” with Brian Goetz
블로그 글 요약: 이 에피소드에서는 Nicolai Parlog이 Oracle의 Java 언어 아키텍트인 Brian Goetz와 함께 Project Amber와 Project Valhalla에 대해 이야기합니다. Brian은 Amber의 새로운 기능 아크와 Valhalla의 null 제한 계획 등 이 두 프로젝트의 중요한 업데이트와 통찰을 공유합니다.
👉 [자세히 보기](https://inside.java/2025/09/28/podcast-040/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전은 새로운 진단 도구로 "플라이트 레코딩" 기능을 도입했습니다. 이 기능은 프로그램의 실행 중 특정 이벤트나 상태를 기록하여 문제 해결 및 성능 최적화를 돕습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀으므로, 현재 진행 상황과 더 넓은 커뮤니티가 참여할 수 있는 방법에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

