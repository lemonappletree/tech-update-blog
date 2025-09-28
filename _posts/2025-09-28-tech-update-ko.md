# 🛠️ 2025-09-28 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 기술 블로그 글은 Kubernetes 생태계에서 변경된 블록 추적(Changed Block Tracking) API의 알파 지원을 발표하는 내용입니다. 이 기능은 CSI 스토리지 드라이버가 PersistentVolume 스냅샷 내에서 변경된 블록을 식별할 수 있도록 하여 더욱 효율적인 백업 작업을 가능하게 합니다. 변경된 블록 추적은 전체 볼륨을 스캔할 필요 없이 스냅샷 간의 변경 사항을 블록 레벨에서 추적할 수 있게 하여 대규모 데이터 세트를 관리하는 Kubernetes 사용자에게 더 효율적인 백업 프로세스를 제공합니다. 그러나 이 API는 현재 블록 볼륨에만 지원되며 파일 볼륨에는 적용되지 않습니다. 이 블로그는 또한 이 기능을 구현하기 위한 요구 사항 및 백업 솔루션을 최적화하는 방법에 대해서도 설명합니다. 마지막으로, Kubernetes 개발자들은 피드백과 채택에 따라 이 기능을 베타로 발전시킬 계획입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
이 블로그 글은 Spring Batch 프로젝트의 리더인 Mahmoud Ben Hassine과의 인터뷰를 다루고 있습니다. 주로 Spring Boot 4 세대에서의 최신 Spring Batch 기능에 대해 이야기합니다. Spring 팬들에게 유익한 정보를 제공합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - The Trust Paradox: When Your AI Gets Catfished
**제목**: 신뢰의 역설: AI가 속임수에 넘어갈 때

**요약**: MCP를 이용한 공격의 근본적인 문제는 기술적 정교함이 아닙니다. 해커들이 AI를 속이는 방법을 알아냈기 때문입니다. 이러한 공격은 개발 팀이 원활히 기능하도록 만드는 신뢰 관계를 악용하기 때문에 효과적입니다. 예를 들어, 디자이너들이 오랫동안 협력해 온 에이전시로부터 Figma 파일을 기대하거나, DevOps 팀이 신뢰하는 상황에서 이러한 공격이 발생할 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/mcp-prompt-injection-trust-paradox/)

## 🔹 Java - JEPs in JDK 25 Integrated Since JDK 21
이 블로그 글은 JDK 21 이후 JDK 25까지 통합된 JEPs(자바 개선 제안서)에 대해 다루고 있습니다. JDK 21은 대부분의 벤더가 제공하는 이전 장기 지원(LTS) 릴리스였으며, JDK 22부터 25까지의 릴리스에 포함된 JEPs 중 후속 JEPs로 대체된 프리뷰 및 인큐베이터 JEPs는 포함되지 않았습니다. 각 JEP가 통합된 릴리스는 JEP 제목 뒤 괄호 안에 표시되어 있습니다.
👉 [자세히 보기](https://inside.java/2025/09/26/jeps-since-jdk-21/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 진단 도구 모음에 새로운 도구인 "플라이트 레코딩"이 추가되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 문제 해결에 유용한 정보를 제공합니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

