# 🛠️ 2025-05-18 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes v1.33 버전에서 인플레이스(In-Place) Pod 리사이즈 기능이 베타로 승격되어 기본적으로 활성화됩니다. 이 기능은 CPU와 메모리 자원을 Pod를 재시작하지 않고도 조정할 수 있어, 상태 유지 애플리케이션이나 배치 작업 등에서 발생하는 중단 문제를 줄이는 데 도움이 됩니다. 알파 버전 이후 기능의 안정성과 사용자 경험이 크게 개선되었으며, 베타 버전에서는 `resize` 서브리소스를 통해 자원 조정을 수행해야 합니다. 이 기능은 Pod의 자원 사용 효율성을 개선하고, 빠른 확장을 가능하게 하며, 사이드카 컨테이너의 리사이즈도 지원합니다. 앞으로의 개발 계획에는 기능의 안정성 강화, 제한사항 해결, VerticalPodAutoscaler와의 통합 등이 포함됩니다. Kubernetes 커뮤니티는 사용자 피드백을 통해 기능을 더욱 향상시킬 계획입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Data 2025.0.0 goes GA
Spring Data 2025.0.0이 정식으로 출시되었습니다. 이번 릴리스는 Maven Central에서 사용할 수 있으며, 드라이버 업그레이드와 개별 스토어 모듈의 개선 사항이 포함되어 있습니다. 주요 변경 사항으로는 MongoDB와 Apache Cassandra의 벡터 타입 및 벡터 검색 지원, Spring Data JPA의 DTO 프로젝션을 위한 생성자 표현식 유도, Spring Data JDBC 및 R2DBC의 시퀀스를 사용한 식별자 생성 지원, Cassandra 5의 스토리지 부착 인덱스를 사용한 인덱스 생성 등이 있습니다. Spring Boot 3.5는 Spring Data 2025.0.0으로 업그레이드되며, 2025.0.0 릴리스는 3.x 개발 라인의 마지막 기능 릴리스입니다. 앞으로 4.0 릴리스가 예정되어 있으며, 2025년 11월에 정식 출시될 예정입니다. 자세한 사항은 릴리스 노트를 참조하세요.
👉 [자세히 보기](https://spring.io/blog/2025/05/16/spring-data-2025-0-goes-ga)

## 🔹 Docker - Docker at Microsoft Build 2025: Where Secure Software Meets Intelligent Innovation
Microsoft Build 2025 행사에서 Docker는 개발자 경험, 보안, AI 혁신을 결합한 최신 제품 발표를 선보입니다. 시애틀 컨벤션 센터에서 직접 참석하든 온라인으로 참여하든, Docker가 현대 애플리케이션을 구축, 보호 및 확장하는 방식을 어떻게 재정의하고 있는지 확인할 수 있습니다. Docker는 개발자들을 위한 비전을 제시하며, 새로운 제품과 기술을 통해 팀의 개발 과정에 혁신을 더하고자 합니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-at-microsoft-build-2025/)

## 🔹 Java - Java 24, Faster Than Ever
글 요약: Java는 성능 면에서 끊임없이 발전하고 있으며, 새로운 Java 버전이 출시될 때마다 변경되지 않은 응용 프로그램 코드도 더 빠르게 실행될 수 있습니다. 이 글에서는 표준 Java 라이브러리, JIT 컴파일러, 가비지 컬렉터를 포함한 JDK의 최근 성능 개선 사항 다섯 가지를 자세히 살펴봅니다.
👉 [자세히 보기](https://inside.java/2025/05/17/javaone-faster-jdk24/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
Go 1.24 버전에서 도입된 `testing.B.Loop` 기능에 대한 기술 블로그입니다. 이 기능은 Go 언어의 벤치마크 테스트에서 반복 실행의 예측 가능성을 개선하는 데 중점을 두고 있습니다. `testing.B.Loop`을 사용하면 벤치마크 테스트의 반복 실행이 더 일관되고 정확한 결과를 제공할 수 있도록 도와줍니다. 이를 통해 개발자는 성능 측정을 보다 신뢰성 있게 수행할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀은 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 마련되어 있으며, 발표 세션과 Project Pavilion의 Helm 부스에서 유지 관리자들과의 대화도 가능합니다. 행사 기간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

