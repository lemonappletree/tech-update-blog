# 🛠️ 2025-10-02 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
제목: 변경된 블록 추적 API 지원 발표 (알파)

요약: Kubernetes가 PersistentVolume 스냅샷에서 변경된 블록을 식별하는 효율적인 방법을 제공하는 '변경된 블록 추적' 메커니즘에 대한 알파 지원을 발표했습니다. 이 기능을 통해 백업 작업을 더 빠르고 자원 효율적으로 수행할 수 있습니다. 이 기능은 CSI 스토리지 드라이버와 함께 작동하며, Kubernetes의 스토리지 생태계를 강화합니다. 

변경된 블록 추적은 스냅샷 간의 블록 변경을 식별하고 추적하여, 백업 시 전체 볼륨을 스캔할 필요를 없애줍니다. 이는 Kubernetes의 Container Storage Interface(CSI)와 스토리지 지원에 대한 개선 사항을 포함합니다. 

현재 이 API는 블록 볼륨에 대해서만 지원되며, 파일 기반 스토리지 시스템을 관리하는 CSI 드라이버는 이 기능을 구현할 수 없습니다. Kubernetes 사용자들은 이를 통해 더 효율적인 백업 프로세스를 구현할 수 있습니다. 

또한, 구현 요구 사항과 백업 솔루션의 책임 사항도 상세히 설명되어 있으며, 알파 기능을 클러스터에서 사용하는 방법에 대한 안내도 포함되어 있습니다. 이 기능의 성공적인 피드백과 채택에 따라 Kubernetes 개발자들은 향후 베타로 전환할 계획입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Spring AI 1.0.3 Available Now
Spring AI 1.0.3이 이제 Maven Central에서 사용할 수 있습니다. 이 패치 릴리스는 중요한 안정성 개선과 버그 수정을 제공합니다. 총 27개의 개선 사항, 버그 수정, 문서 업데이트가 포함되어 있으며, 특히 기능 확장과 커뮤니티에서 보고된 문제 해결에 중점을 두었습니다. 주요 개선 사항으로는 GemFire 벡터 스토어의 메타데이터 필터링, AWS Bedrock의 새로운 API 및 프록시 채팅 모델 수정, GraalVM 네이티브 이미지의 사전 컴파일 개선 등이 있습니다. 또한, Spring Bean 주입과 개발자 경험 개선도 포함되어 있습니다. 다음 버전은 1.1 GA 릴리스로 4-5주 후에 계획되어 있으며, Model Context Protocol (MCP) 기능에 주력할 예정입니다. 자세한 업데이트는 GitHub 저장소 및 커뮤니티 채널을 통해 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/01/spring-ai-1-0-3-available-now)

## 🔹 Docker - Expanding Docker Hardened Images: Secure Helm Charts for Deployments
기술 블로그 글 요약: 개발 팀들은 소프트웨어 공급망을 안전하게 보호해야 한다는 압박을 받고 있습니다. 이들은 신뢰할 수 있는 이미지, 간편한 배포, 그리고 장기적으로 의지할 수 있는 파트너로부터의 준수 가능한 도구를 필요로 합니다. 고객들은 일회성 공급업체가 아닌, 개발과 배포 전반에 걸친 진정한 보안 파트너를 원하고 있습니다. 이러한 요구에 부응하기 위해...
👉 [자세히 보기](https://www.docker.com/blog/docker-hardened-images-helm-charts-beta/)

## 🔹 Java - Oracle Java Extension for Visual Studio Code Version 24.1.2 Is Now Available!
제목: Oracle Java Extension for Visual Studio Code 버전 24.1.2 출시!

요약: Visual Studio Code를 위한 새로운 Java 플랫폼 확장판이 출시되었습니다. 이번 업데이트는 개발자들이 Java 코드를 더 효율적으로 작성하고 디버깅할 수 있도록 다양한 기능 개선과 버그 수정을 포함하고 있습니다. 상세 내용은 제공된 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/10/01/java-vscode-extension-update/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구인 "플라이트 레코딩" 기능이 도입되었습니다. 이 기능은 프로그램의 실행 중 발생하는 다양한 사건들을 기록하여 문제를 진단하고 성능을 최적화하는 데 도움을 줍니다. 자세한 내용은 [여기](https://go.dev/blog/flight-recorder)를 참조하세요.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

