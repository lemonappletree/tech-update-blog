# 🛠️ 2025-05-09 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes 1.33: Volume Populators Graduate to GA
Kubernetes 1.33 버전에서 볼륨 인구자(Volume Populators)가 일반 사용(GA)으로 전환되었습니다. 이제 사용자들은 PersistentVolumeClaim(PVC)의 데이터 소스로 적합한 사용자 정의 리소스를 지정할 수 있습니다. 주요 변경 사항으로는 Populator Pod가 선택 사항이 되었고, Kubernetes 리소스를 수정할 수 있는 변형 함수 및 유연한 메트릭 처리가 포함되었습니다. 또한, 임시 리소스 정리 기능이 추가되었습니다. 앞으로의 발전 방향으로는 다중 동기화 및 양방향 동기화, 우선순위 기반 데이터 채우기 등이 제안되고 있습니다. 관련 문의는 SIG Storage 커뮤니티에 문의할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/08/kubernetes-v1-33-volume-populators-ga/)

## 🔹 Spring Boot - A Bootiful Podcast: V Körbes on security from the platform on up
제목: 아름다운 팟캐스트: 플랫폼에서 시작하는 보안에 대한 V Körbes의 이야기

요약: Spring 팬 여러분, 안녕하세요! 오늘 특별한 에피소드에서는 Broadcom의 V Körbes와 함께 애플리케이션 상하단에서의 보안에 대해 이야기합니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/08/a-bootiful-podcast-v-korbes)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
이 기술 블로그 글은 모델 컨텍스트 프로토콜(MCP)의 보안 문제와 이를 해결하기 위한 방안에 대해 다루고 있습니다. MCP 도구는 초기 사용자들 사이에서 주로 사용되고 있으나, 점점 더 널리 채택되고 있습니다. 그러나 이와 함께 MCP 보안 문제도 점점 중요해지고 있습니다. MCP 도구는 에이전트의 자율성을 증가시켜, 사용자 기대와 에이전트 행동 간의 불일치 및 통제되지 않은 실행과 관련된 새로운 위험을 초래합니다. 이러한 시스템은 또한 새로운 형태의 보안 문제를 제기합니다. 블로그는 이러한 문제를 해결하기 위해 컨테이너를 사용하여 에이전트형 AI의 안전성을 높이는 방법을 제안합니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - Structured Concurrency Revamp in Java 25 - Inside Java Newscast #91
이 기술 블로그 글에서는 Java 25에서의 구조적 동시성 API 개편에 대해 다루고 있습니다. JDK Enhancement Proposal 505를 통해 JDK 25에 설정(configuration)과 조인(joiners)이 도입되어 구조적 동시성 API가 개선됩니다.
👉 [자세히 보기](https://inside.java/2025/05/08/newscast-91/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글은 Go 1.24 버전에서 도입된 `testing.B.Loop` 기능을 통해 벤치마크 테스트를 더 예측 가능하게 만드는 방법을 다룹니다. 새로운 개선점으로 인해 벤치마크 루핑이 이전보다 더욱 효율적이고 일관성 있게 수행될 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 주어지며, 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과의 대화 세션도 마련되어 있습니다. 주간 내내 진행되는 Helm 관련 활동에 대한 자세한 정보는 원문을 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

