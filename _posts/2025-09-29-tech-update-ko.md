# 🛠️ 2025-09-29 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 기술 블로그 글은 Kubernetes의 스토리지 생태계에 효율성을 더해주는 변경된 블록 추적(Changed Block Tracking) API에 대한 알파 지원을 발표하는 내용입니다. 이 기능은 CSI 스토리지 드라이버가 PersistentVolume 스냅샷에서 변경된 블록을 식별할 수 있게 하여 백업 작업을 보다 빠르고 자원 효율적으로 수행할 수 있도록 합니다. 변경된 블록 추적은 스냅샷 간의 블록 수준 변경을 식별하고 추적할 수 있도록 하며, 전체 볼륨을 스캔하지 않고도 백업 작업을 간소화합니다. 현재 이 API는 블록 볼륨에만 지원되며, 파일 기반 스토리지 시스템에서는 사용할 수 없습니다. 이 블로그 글은 또한 이 기능을 구현하기 위한 스토리지 공급자와 백업 솔루션의 요구 사항, 주요 구성 요소, 시작 방법 및 향후 계획에 대해 설명합니다. Kubernetes 사용자는 이 API를 통해 더 효율적인 백업 프로세스를 구현할 수 있으며, 이는 특히 대규모 데이터 세트를 다룰 때 유용합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
이번 기술 블로그 글에서는 스프링 팬들을 위해 스프링 배치 프로젝트의 리더인 마흐무드 벤 하신과의 인터뷰를 소개합니다. 이 인터뷰에서는 스프링 부트 4 세대에서의 스프링 배치의 최신 기능과 발전에 대해 논의합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - The Trust Paradox: When Your AI Gets Catfished
블로그 글 "The Trust Paradox: When Your AI Gets Catfished"는 AI를 대상으로 한 MCP(멀티채널 프로세스) 공격의 기본 문제를 다루고 있습니다. 이 공격들은 기술적 정교함보다는 해커들이 AI의 신뢰 관계를 이용해 '캣피싱'을 하는 데 성공한 것이 핵심입니다. 공격은 개발 팀이 의존하는 신뢰 관계를 악용하여 이루어지며, 예를 들어 디자이너가 오랫동안 협력해 온 에이전시로부터 Figma 파일을 기대할 때, 또는 DevOps 팀이 특정 출처를 신뢰할 때 발생할 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/mcp-prompt-injection-trust-paradox/)

## 🔹 Java - Episode 40 “Amber &amp; Valhalla - Incremental Design and Feature Arcs” with Brian Goetz
이 블로그 글은 에피소드 40 "Amber & Valhalla - Incremental Design and Feature Arcs"에 대한 요약입니다. Nicolai Parlog이 Oracle의 Java 언어 아키텍트인 Brian Goetz와 함께 진행한 이 에피소드에서는 Project Amber와 Project Valhalla의 주요 업데이트와 통찰을 공유합니다. 특히 Amber의 새로운 기능 아크와 Valhalla의 null 제한 계획 등에 대해 논의합니다.
👉 [자세히 보기](https://inside.java/2025/09/28/podcast-040/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구인 '비행 기록' 기능이 도입되었습니다. 이 도구는 프로그램 실행 시 발생하는 다양한 이벤트를 기록하여 문제 해결을 돕습니다. 이를 통해 개발자는 버그를 더 쉽게 찾아내고, 성능 문제를 분석할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 향한 여정

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에 현재 진행 상황과 커뮤니티가 참여할 수 있는 방법에 대해 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

