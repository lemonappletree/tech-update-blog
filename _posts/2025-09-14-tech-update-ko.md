# 🛠️ 2025-09-14 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA
Kubernetes v1.34에서는 노드 cgroup 드라이버의 자동 구성 기능이 일반 제공(GA) 단계에 도달했습니다. 기존에는 Kubernetes 클러스터 설정 시 <code>cgroupfs</code>와 <code>systemd</code>라는 두 가지 cgroup 드라이버를 수동으로 맞춰 설정해야 했습니다. 하지만 v1.28.0에서 도입된 <code>KubeletCgroupDriverFromCRI</code> 기능 게이트를 통해 kubelet이 CRI 구현으로부터 사용할 cgroup 드라이버를 자동으로 감지할 수 있게 되었습니다. 이 기능은 이제 Kubernetes 1.34.0에서 GA로 제공됩니다. 또한, Kubernetes는 containerd v1.y 지원 중단을 발표하였으며, v1.36.0부터는 containerd v2.0 이상 버전이 필요합니다. 이를 위해 <code>kubelet_cri_losing_support</code> 메트릭을 통해 노드의 containerd 버전 상태를 모니터링할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M2 (aka Oakwood) has been released
Spring Cloud 2025.1.0-M2 (Oakwood) 버전이 출시되었습니다. 이번 릴리스는 Spring Boot 4.0.0-M2에 의존하며, 주요 모듈인 Spring Cloud OpenFeign, Config, Build 등 여러 모듈이 업데이트되었습니다. 상세한 변경 사항은 GitHub 릴리스 노트에서 확인할 수 있습니다. 개발자들은 Maven 또는 Gradle을 통해 이 버전을 사용할 수 있으며, 피드백은 GitHub, Stack Overflow, Twitter를 통해 받을 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/12/spring-cloud-2025-1-0-M2-aka-oakwood-has-been-released)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
이 기술 블로그 글은 AI 워크플로우에서 발생할 수 있는 보안 문제와 이를 해결하기 위한 런타임 보안 전략에 대해 설명합니다. 현재 사용되는 AI 도구들은 강력하지만 예측하기 어렵고 악용될 가능성이 있습니다. 개발자들은 이러한 도구들을 안전하게 사용하기 위해 런타임 보안을 AI 에이전트에 통합하고 있습니다. 글은 AI 워크플로우가 공격 표면이 될 수 있음을 강조하며, 개발자가 AI 에이전트를 안전하게 구축하는 방법을 다룹니다.
👉 [자세히 보기](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
이 기술 블로그 글은 Java 21부터 Java 25까지의 API 추가 내용을 다룹니다. 주요 추가 사항으로는 범위 값(scped values), 스트림 수집기(stream gatherers), 클래스 파일 API, 외부 함수 및 메모리 API, 그리고 Javadoc 관련 추가 기능들이 있습니다. 이 글을 통해 각 버전에서 도입된 새로운 API에 대해 자세히 배울 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
Go 1.25 버전에서는 실험적인 기능으로 encoding/json/jsontext 및 encoding/json/v2 패키지에 대한 지원을 도입했습니다. 이는 JSON 처리 기능을 확장하고 개선하기 위한 새로운 API를 제공합니다.
👉 [자세히 보기](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이른 만큼, 현재 진행 상황과 커뮤니티가 참여할 수 있는 방법에 대해 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

