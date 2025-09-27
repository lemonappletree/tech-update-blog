# 🛠️ 2025-09-27 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 기술 블로그 글은 Kubernetes의 저장소 생태계를 개선하기 위해 변경 블록 추적(Change Block Tracking) API에 대한 알파 지원을 발표합니다. 이 기능은 CSI 저장소 드라이버가 PersistentVolume 스냅샷에서 변경된 블록을 식별할 수 있게 하여 백업 작업을 더 빠르고 효율적으로 수행할 수 있도록 돕습니다. 주요 내용은 다음과 같습니다:

- 변경 블록 추적이란 스냅샷 간에 블록 수준에서의 변경 사항을 식별하고 추적하여 전체 볼륨을 스캔할 필요 없이 백업 작업을 효율화하는 기능입니다.
- Kubernetes 사용자에게 더 효율적인 백업 프로세스를 가능하게 하며, 변경된 블록만 처리함으로써 자원 소비를 줄일 수 있습니다.
- 현재 이 API는 블록 볼륨에만 적용되며, 파일 볼륨에는 지원되지 않습니다.
- 주요 구성 요소로는 CSI SnapshotMetadata 서비스 API, SnapshotMetadataService API, 외부 스냅샷 메타데이터 사이드카가 있습니다.
- 스토리지 제공자는 CSI RPC를 구현하고 외부 컴포넌트를 배포해야 하며, 백업 솔루션은 인증 설정과 스트리밍 클라이언트 코드 구현을 필요로 합니다.

이 기능을 사용하려면 CSI 드라이버가 스냅샷 메타데이터 기능을 구현하고 클라이언트가 API에 접근할 수 있도록 설정해야 합니다. 향후 베타 버전으로의 발전을 목표로 하고 있으며, 관련 문서와 리소스를 통해 더 많은 정보를 얻을 수 있습니다. Kubernetes Storage Special Interest Group에 참여하여 CSI 또는 Kubernetes 저장소 시스템의 개발에 기여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
이 블로그 글은 Spring Batch 프로젝트의 리더인 Mahmoud Ben Hassine과의 팟캐스트 인터뷰를 소개합니다. 그는 Spring Boot 4 버전에서의 최신 Spring Batch에 대해 이야기합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - The Trust Paradox: When Your AI Gets Catfished
제목: 신뢰의 역설: 당신의 AI가 피싱 당할 때

이 블로그 글은 MCP(멀티 채널 피싱) 공격의 주요 문제는 기술의 복잡함이 아니라, 해커들이 AI를 속이는 방법을 터득했다는 점에 대해 다룹니다. 이러한 공격은 개발 팀을 실제로 작동하게 만드는 신뢰 관계를 악용하기 때문에 성공합니다. 예를 들어, 디자이너들이 오랫동안 협력해온 에이전시로부터 Figma 파일을 기대할 때나 DevOps 팀이 특정 소스를 신뢰할 때 이러한 신뢰 관계가 공격의 대상이 될 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/mcp-prompt-injection-trust-paradox/)

## 🔹 Java - JEPs in JDK 25 Integrated Since JDK 21
이 기술 블로그 글에서는 JDK 21 이후 통합된 JEPs(자바 개선 제안서)를 설명하고 있습니다. JDK 21은 대부분의 벤더가 제공하는 이전 장기 지원(LTS) 릴리스였습니다. JDK 22부터 25까지의 릴리스에서 나중에 다른 JEPs로 대체된 미리 보기 및 인큐베이터 JEPs는 포함되지 않았습니다. 각 JEP가 통합된 릴리스는 JEP 제목 뒤 괄호 안에 표시되어 있습니다.
👉 [자세히 보기](https://inside.java/2025/09/26/jeps-since-jdk-21/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구인 "플라이트 레코더"가 도입되었습니다. 이는 Go 애플리케이션의 성능과 동작을 분석하는 데 도움을 주는 도구입니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 위한 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀으며, 이번 블로그 글에서는 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

