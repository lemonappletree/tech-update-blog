# 🛠️ 2025-09-13 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA
Kubernetes v1.34에서는 새로운 자동 설정 기능이 GA(일반 가용성)로 출시되었습니다. 이전에는 Linux 시스템에서 cgroup 드라이버(`cgroupfs`와 `systemd`)를 설정하는 것이 까다로웠습니다. kubelet과 CRI 구현(예: CRI-O, containerd)이 동일한 cgroup 드라이버를 사용하도록 설정하지 않으면 문제가 발생하곤 했습니다. v1.28.0에서 SIG Node 커뮤니티는 `KubeletCgroupDriverFromCRI` 기능 게이트를 도입하여 kubelet이 CRI 구현에 어떤 cgroup 드라이버를 사용할지 문의하도록 했습니다. 이 기능은 Kubernetes 1.34.0에서 GA로 발표되었습니다.

관리자는 CRI 구현이 충분히 최신인지 확인해야 합니다. containerd는 v2.0.0부터, CRI-O는 v1.28.0부터 이 기능을 지원합니다. Kubernetes는 containerd v1.y 지원을 단계적으로 중단할 계획입니다. 마지막 지원 릴리스는 v1.35의 최종 버전이 될 것이며, v1.36.0에서 지원이 중단됩니다. 관리자는 `kubelet_cri_losing_support` 메트릭을 통해 클러스터의 노드가 곧 지원되지 않을 containerd 버전을 사용 중인지 확인할 수 있으며, v1.36.0으로 업그레이드하기 전에 containerd를 v2.0 이상으로 업그레이드해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M2 (aka Oakwood) has been released
Spring Cloud 2025.1.0-M2(일명 Oakwood) 릴리스가 발표되었습니다. 이 릴리스는 Maven Central에서 확인할 수 있으며, Spring Boot 4.0.0-M2를 기반으로 합니다. 이번 릴리스에는 Spring Cloud OpenFeign, Config, Build, Stream, Netflix, Circuitbreaker, Contract, Commons, Consul, Gateway, Vault, Function, Dependencies, Task, Kubernetes, Bus, Zookeeper 등 여러 모듈이 포함되어 있습니다. 각 모듈의 업데이트된 버전과 관련된 이슈는 GitHub에서 확인할 수 있습니다. Maven 또는 Gradle을 사용하여 프로젝트에 통합할 수 있으며, 커뮤니티 피드백은 GitHub, Stack Overflow 또는 Twitter를 통해 환영합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/12/spring-cloud-2025-1-0-M2-aka-oakwood-has-been-released)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
이 블로그 글은 AI 에이전트를 안전하게 구축하기 위해 개발자들이 런타임 보안을 어떻게 적용하는지에 대해 설명합니다. AI 워크플로우는 강력하지만 예측 불가능하고 취약점이 존재할 수 있습니다. 예를 들어, LLM에 특정 입력을 주면 Dockerfile이나 쉘 스크립트를 생성할 수 있는데, 이는 처음에는 올바르게 보일 수 있습니다. 하지만 이를 개발 환경에서 실행할 때 예상치 못한 문제가 발생할 수 있습니다. 이러한 이유로 AI 워크플로우를 공격 표면으로부터 보호하는 것이 중요하며, 개발자들은 이에 대한 솔루션을 찾고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
이 블로그 글에서는 Java 21부터 Java 25까지의 모든 API 추가 사항에 대해 설명합니다. 주요 추가 기능으로는 범위 값, 스트림 수집기, 클래스 파일 API, 외부 함수 및 메모리 API, Javadoc 추가 기능 등이 있습니다. 이 글은 Java의 최신 버전으로 업그레이드하면서 주목해야 할 새로운 기능들을 이해하는 데 도움을 줍니다.
👉 [자세히 보기](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
제목: JSON을 위한 새로운 실험적 Go API  
요약: Go 1.25 버전에서는 `encoding/json/jsontext`와 `encoding/json/v2` 패키지에 대한 실험적 지원을 도입했습니다.  
링크: https://go.dev/blog/jsonv2-exp
👉 [자세히 보기](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시까지의 여정

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기에 현재 진행 상황과 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

