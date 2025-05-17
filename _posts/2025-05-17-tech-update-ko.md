# 🛠️ 2025-05-17 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
이 기술 블로그 글에서는 Kubernetes v1.33에서 인-플레이스 Pod 리사이즈 기능이 베타로 승격되었음을 발표하고 있습니다. 이 기능은 처음 v1.27에서 알파로 소개되었으며, 이제 기본적으로 활성화됩니다. 인-플레이스 Pod 리사이즈는 실행 중인 Pod의 CPU 및 메모리 요청과 제한을 변경할 수 있게 하여, 리소스 관리의 유연성을 높이고 중단을 줄입니다. 전통적으로 컨테이너의 리소스를 변경하려면 Pod를 재시작해야 했으나, 이 기능을 통해 재시작 없이 리소스를 조정할 수 있습니다. 이를 통해 상태 저장 애플리케이션, 배치 작업 및 민감한 워크로드에 대한 중단을 최소화하고, 리소스 활용도를 개선하며, 더욱 빠른 스케일링을 제공합니다. 이번 베타 릴리스에서는 사용자 경험을 개선하고 안정성을 높이는 여러 변경 사항들이 포함되었습니다. 향후 개발 방향으로는 안정성 강화, 제한사항 해결, 수직 포드 자동 확장기(VPA) 통합 등이 있습니다. 사용자는 새로운 베타 기능을 테스트하고, 피드백을 제공함으로써 발전에 기여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Data 2025.0.0 goes GA
이 블로그 글은 Spring Data 2025.0.0의 일반 출시를 알리는 내용입니다. 주요 변경 사항으로는 MongoDB와 Apache Cassandra에서 벡터 타입 및 벡터 검색 지원, Spring Data JPA에서 DTO 프로젝션을 위한 생성자 표현 유도, Spring Data JDBC와 R2DBC에서 시퀀스를 사용한 식별자 생성 지원, Cassandra 5 저장소 부착 인덱스를 사용한 인덱스 생성 등이 포함됩니다. 또한 Spring Boot 3.5가 Spring Data 2025.0.0으로 업그레이드될 예정이며, 이는 3.x 개발 라인의 마지막 기능 릴리스입니다. 이후 4.0 릴리스가 2025년 11월에 GA로 출시될 예정입니다. 각 모듈의 문서와 변경 로그에 대한 링크도 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/16/spring-data-2025-0-goes-ga)

## 🔹 Docker - Docker at Microsoft Build 2025: Where Secure Software Meets Intelligent Innovation
기술 블로그 글 요약: "Microsoft Build 2025에서 Docker는 개발자 경험, 보안, AI 혁신을 결합한 최신 제품 발표를 선보입니다. 시애틀 컨벤션 센터에서 직접 참석하거나 온라인으로 참여하더라도 Docker가 현대 애플리케이션을 구축, 보안 및 확장하는 방식을 어떻게 재정의하고 있는지 확인할 수 있습니다."
👉 [자세히 보기](https://www.docker.com/blog/docker-at-microsoft-build-2025/)

## 🔹 Java - Mastering JVM Memory Troubleshooting - From OutOfMemoryErrors to Leaks
이 기술 블로그 글은 Java 애플리케이션에서 발생하는 메모리 문제의 진단 방법에 대해 다루고 있습니다. 메모리 문제는 Java 힙 메모리 부족, 메타스페이스 오버플로우, 네이티브 메모리 누수 등 다양한 형태로 나타날 수 있으며, 이를 해결하는 것은 어려운 작업입니다. 이 글에서는 일반적이거나 잘 알려지지 않은 메모리 문제를 탐색하고, 이러한 문제를 효과적으로 해결하는 방법에 대해 설명합니다.
👉 [자세히 보기](https://inside.java/2025/05/15/javaone-jvm-troubleshooting/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 블로그 글은 Go 1.24 버전에서 도입된 `testing.B.Loop` 기능을 통해 벤치마크 테스트를 보다 예측 가능하게 수행할 수 있는 방법에 대해 설명하고 있습니다. 새로운 루프 메커니즘은 벤치마크 테스트의 반복성을 개선하여 더 안정적인 성능 측정을 가능하게 합니다. 이를 통해 개발자는 코드의 성능을 보다 정확하게 평가할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의를 위해 유지 관리자들과의 대화 세션 및 프로젝트 파빌리온의 Helm 부스를 방문해보세요. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 사항은 블로그 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

