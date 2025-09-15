# 🛠️ 2025-09-15 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA
Kubernetes v1.34에서는 노드 Cgroup 드라이버의 자동 설정 기능이 GA(일반 사용 가능)로 출시되었습니다. 이전에는 kubelet과 CRI 구현(containerd, CRI-O 등)이 동일한 cgroup 드라이버를 사용하도록 수동으로 설정해야 했으나, v1.28.0부터 도입된 KubeletCgroupDriverFromCRI 기능 게이트를 통해 kubelet이 CRI 구현에 적합한 cgroup 드라이버를 자동으로 감지할 수 있게 되었습니다. 이 기능은 이제 Kubernetes 1.34.0에서 일반적으로 사용할 수 있습니다. 또한, Kubernetes는 containerd v1.y 지원을 중단할 예정이며, 이를 대비하기 위해 kubelet_cri_losing_support 메트릭을 통해 노드에서 사용 중인 containerd 버전의 지원 여부를 확인할 수 있습니다. 관리자는 kubelet을 v1.36.0으로 업그레이드하기 전이나 동시에 containerd를 v2.0 이상으로 업그레이드해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M2 (aka Oakwood) has been released
Spring Cloud 2025.1.0-M2(Oakwood) 버전이 출시되었습니다. 이 버전은 Spring Boot 4.0.0-M2에 의존하며, Maven Central에서 확인할 수 있습니다. 주요 변경 사항으로는 여러 모듈의 업데이트가 포함되어 있으며, Spring Cloud OpenFeign, Spring Cloud Config, Spring Cloud Build 등 다양한 모듈이 5.0.0-M2로 업데이트되었습니다. 자세한 내용은 GitHub, Stack Overflow 또는 Twitter를 통해 피드백을 받을 수 있습니다. Maven 또는 Gradle을 사용한 시작 가이드도 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/12/spring-cloud-2025-1-0-M2-aka-oakwood-has-been-released)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
이 기술 블로그 글은 AI 워크플로우를 실행하는 동안 보안을 확보하는 방법에 대해 설명합니다. 현재 사용되는 AI 도구들은 매우 강력하지만, 동시에 예측 불가능하고 악용될 가능성이 있습니다. 예를 들어, 대형 언어 모델(LLM)을 사용하여 Dockerfile이나 셸 스크립트를 생성하면 겉보기에 올바르거나 합리적으로 보일 수 있지만, 실제로 실행할 때 예상치 못한 문제가 발생할 수 있습니다. 이 글은 개발자들이 이러한 AI 에이전트를 안전하게 구축하기 위해 런타임 보안을 어떻게 적용하는지를 다룹니다.
👉 [자세히 보기](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
이 기술 블로그 글은 Java 21부터 Java 25까지의 API 추가 사항을 다룹니다. 주요 내용으로는 범위가 지정된 값(scped values), 스트림 수집기(stream gatherers), 클래스 파일 API, 외부 함수 및 메모리 API, Javadoc 추가 사항 등이 있습니다. 이러한 새로운 API 기능들은 Java의 기능성과 효율성을 향상시키기 위한 것입니다.
👉 [자세히 보기](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
블로그 글 요약: Go 1.25 버전에서는 새로운 실험적 JSON API가 도입되었습니다. 이 버전에서는 `encoding/json/jsontext`와 `encoding/json/v2` 패키지에 대한 실험적 지원이 포함되어 있습니다.
👉 [자세히 보기](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 향한 여정

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 접어든 만큼, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다. 상세 내용은 [링크](https://helm.sh/blog/path-to-helm-v4/)를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

