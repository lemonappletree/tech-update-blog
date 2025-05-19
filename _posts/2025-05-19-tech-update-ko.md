# 🛠️ 2025-05-19 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes v1.33 버전에서 '인플레이스 Pod 리사이즈' 기능이 베타로 졸업하여 기본적으로 활성화되었습니다. 이 기능은 Kubernetes v1.27에서 알파로 처음 도입되었으며, Pod를 재시작하지 않고 실행 중인 상태에서 CPU 및 메모리 자원을 조정할 수 있게 해줍니다. 이는 상태 저장 애플리케이션이나 배치 작업 등 재시작에 민감한 워크로드에 유용합니다. 베타로의 졸업은 이 기능의 안정성과 사용자 경험을 개선하고, 커뮤니티의 피드백을 반영하여 사용성을 높인 결과입니다. 앞으로도 이 기능의 안정성 강화와 프로덕션 환경에서의 활용을 위한 개발이 계속될 예정입니다. Kubernetes v1.33 클러스터에서 kubectl을 사용하여 이 기능을 경험할 수 있으며, 피드백은 Kubernetes의 공식 채널을 통해 제공할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Data 2025.0.0 goes GA
"Spring Data 2025.0.0이 일반 공급(GA)됨"이라는 제목의 기술 블로그 글은 Spring Data 2025.0.0 버전이 Maven Central을 통해 일반 공급되었음을 발표하는 내용입니다. 이번 릴리스에서는 드라이버 업그레이드와 각 스토어 모듈의 개선이 이루어졌습니다. 주요 변경 사항으로는 MongoDB와 Apache Cassandra에서 벡터 타입 및 벡터 검색 지원, Spring Data JPA의 DTO 프로젝션을 위한 생성자 표현식 유도, Spring Data JDBC 및 R2DBC에서 시퀀스를 사용한 식별자 생성 지원, Cassandra 5의 스토리지 부착 인덱스를 사용한 인덱스 생성이 포함됩니다. Spring Boot 3.5는 Spring Data 2025.0.0으로 업그레이드될 예정이며, 이는 3.x 개발 라인의 마지막 기능 릴리스입니다. 향후 몇 달간 4.0 릴리스 작업이 진행될 예정입니다. 추가적인 세부 사항은 릴리스 노트를 참조할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/16/spring-data-2025-0-goes-ga)

## 🔹 Docker - Docker at Microsoft Build 2025: Where Secure Software Meets Intelligent Innovation
2025년 Microsoft Build에서 Docker는 개발자 경험, 보안, AI 혁신을 결합한 최신 제품 발표를 선보일 예정입니다. 시애틀 컨벤션 센터에서 직접 참석하거나 온라인으로 참여하더라도 Docker가 현대 애플리케이션을 구축, 보호 및 확장하는 방식을 어떻게 재정의하고 있는지 확인할 수 있습니다. Docker는 이번 행사에서 개발자들을 위한 비전을 제시할 예정입니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-at-microsoft-build-2025/)

## 🔹 Java - Java 24, Faster Than Ever
블로그 글은 최신 Java 24가 성능 면에서 더욱 빨라졌음을 설명하고 있습니다. 새로운 Java 릴리스마다 변경되지 않은 애플리케이션 코드가 더 빠르게 실행될 수 있도록 지속적으로 발전하고 있습니다. 이 글에서는 JDK의 최근 성능 개선 다섯 가지를 자세히 살펴보며, 표준 Java 라이브러리, JIT 컴파일러, 가비지 컬렉터와 관련된 개선 사항을 다루고 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/17/javaone-faster-jdk24/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글은 Go 1.24 버전에서 개선된 벤치마킹 방법인 `testing.B.Loop`에 대해 다룹니다. 새로운 `testing.B.Loop` 기능을 통해 벤치마킹을 더 예측 가능하고 일관되게 수행할 수 있게 되었습니다. 이를 통해 개발자들은 성능 테스트 결과의 변동성을 줄이고, 더 신뢰할 수 있는 성능 데이터를 얻을 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25  
요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대해 이야기할 수 있는 기회가 될 예정으로, 유지 보수자들과의 대화 세션 및 프로젝트 파빌리온에 있는 Helm 부스에서 관련 활동이 진행됩니다. 주간 동안의 모든 Helm 관련 활동에 대한 자세한 내용은 아래 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

