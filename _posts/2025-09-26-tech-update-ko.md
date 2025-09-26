# 🛠️ 2025-09-26 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 블로그 글은 Kubernetes의 저장소 생태계에 대한 새로운 기능인 변경 블록 추적 API 알파 버전 지원을 발표합니다. 이 기능은 CSI 저장소 드라이버가 PersistentVolume 스냅샷에서 변경된 블록을 식별할 수 있도록 하여 백업 작업을 더 빠르고 자원 효율적으로 수행할 수 있게 합니다. 

변경 블록 추적은 스냅샷 사이의 블록 수준에서의 변경 사항을 식별하고 추적하여 백업 작업 시 전체 볼륨을 스캔할 필요성을 제거합니다. 이 API는 Kubernetes의 컨테이너 저장소 인터페이스와 저장소 지원에 변화를 가져와, 대규모 데이터를 관리하는 사용자에게 더 효율적인 백업 프로세스를 제공합니다. 

이 기능은 현재 블록 볼륨에만 지원되며, 파일 기반 저장소 시스템을 관리하는 CSI 드라이버는 이 기능을 구현할 수 없습니다. Kubernetes 사용자들은 이 API를 통해 증분 백업 기능을 활용하여 백업 창을 줄이고, 자원 사용을 최적화하며, 저장 비용을 절감할 수 있습니다. 

이 기능을 사용하려면, CSI 드라이버가 스냅샷 메타데이터 기능을 구현하고, 외부 스냅샷 메타데이터 사이드카를 사용해야 합니다. 또한, 백업 솔루션은 적절한 인증 설정과 스트리밍 클라이언트 코드 구현을 통해 이 기능을 활용해야 합니다. 

Kubernetes 개발자들은 이 기능에 대한 피드백과 채택 상황에 따라 향후 베타 버전으로의 추진을 계획하고 있습니다. 이 기능에 대한 자세한 정보는 Kubernetes CSI 개발자 문서와 GitHub 리포지토리에서 확인할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
블로그 글 요약: 이 글에서는 Spring Batch 프로젝트의 리더인 Mahmoud Ben Hassine과의 인터뷰를 다룹니다. 그는 Spring Boot 4 세대에서의 최신 Spring Batch 기능과 발전에 대해 이야기합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - Introducing the Docker Premium Support and TAM service
Docker는 고객 지원과 기술 계정 관리를 위한 새로운 서비스인 프리미엄 지원 및 TAM 서비스를 소개했습니다. 이 서비스는 24/7 항상 지원, 우선 순위 서비스 수준 협약(SLA), 전문가의 조언 및 TAM 추가 서비스를 포함하여 Docker의 지원을 확장하기 위해 설계되었습니다. 이러한 새로운 서비스는 개발자와 글로벌 비즈니스 고객을 지원하기 위해 신중하게 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-the-docker-premium-support-and-tam-service/)

## 🔹 Java - Reviewing the JDK 25 Release Notes - Inside Java Newscast #98
블로그 글 "JDK 25 릴리스 노트 리뷰 - Inside Java Newscast #98"는 JDK 25의 주요 변경사항을 다룹니다. JDK 25는 LTS(장기 지원) 버전으로, 많은 Java 개발자들이 앞으로 이 버전으로 마이그레이션할 것으로 예상됩니다. 이 블로그는 JDK 25의 전체 릴리스 노트를 검토하여 최신 버전의 주요 변경사항을 소개하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/09/25/newscast-98/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
블로그 글 요약: Go 언어의 미래를 형성하는 데 도움을 주기 위해 설문조사를 진행합니다. 개발자들이 Go 언어를 어떻게 사용하고 있는지에 대한 피드백을 받고자 하며, 이를 통해 Go의 발전 방향을 설정하려고 합니다. 설문조사에 참여하여 여러분의 의견을 공유해 주세요.
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

