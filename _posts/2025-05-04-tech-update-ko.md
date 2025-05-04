# 🛠️ 2025-05-04 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Mutable CSI Node Allocatable Count
Kubernetes v1.33에서는 상태 저장 애플리케이션의 신뢰할 수 있는 스케줄링을 위해 노드의 리소스 가용성 정보를 정확히 제공하는 것이 중요하다는 점을 강조하고 있습니다. 이를 위해, 새로운 알파 기능인 "mutable CSI node allocatable count"를 도입하여 컨테이너 스토리지 인터페이스(CSI) 드라이버가 노드가 처리할 수 있는 최대 볼륨 수를 동적으로 업데이트할 수 있도록 합니다. 이 기능은 파드 스케줄링 결정을 더 정확하게 하고, 오류를 줄이는 데 도움을 줍니다.

기존에는 CSI 드라이버가 초기화 시 노드 볼륨 첨부 한도를 정적으로 보고했지만, 실제 첨부 용량은 노드의 라이프사이클 동안 변경될 수 있습니다. 새로운 기능을 사용하면, Kubernetes는 CSI 드라이버가 노드 첨부 용량을 런타임에 동적으로 조정하고 보고할 수 있게 해줍니다. 이를 통해 스케줄러는 노드 용량에 대한 최신 정보를 얻을 수 있습니다.

이 기능을 사용하려면 `MutableCSINodeAllocatableCount` 기능 게이트를 활성화해야 하며, 이를 통해 주기적 및 즉각적인 업데이트 메커니즘을 지원합니다. 주기적 업데이트는 정해진 간격으로 노드의 할당 가능 용량을 새로 고치며, 즉각적인 업데이트는 자원 고갈 오류가 발생했을 때 즉시 수행됩니다.

Kubernetes 커뮤니티는 이 기능에 대한 피드백을 환영하며, 테스트와 경험 공유를 통해 베타 및 정식 버전으로의 발전을 도모하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/)

## 🔹 Spring Boot - Spring Cloud 2025.0.0-RC1 (aka Northfields) has been released
Spring Cloud 2025.0.0-RC1(일명 Northfields)의 릴리스가 발표되었습니다. 이번 릴리스는 Spring Boot 3.5.0-RC1을 기반으로 하며 다양한 기능 개선사항을 포함하고 있습니다. 주요 변경 사항으로는 Spring Cloud Config의 AWS S3 버킷에서 YAML 프로필 문서 지원, Spring Cloud Gateway의 사용자 정의 필터 및 프레디케이트를 빈으로 등록 가능, Spring Cloud Task의 Remote Partitioning 및 Task Launcher의 사용 중단 알림 등이 있습니다. 또한, Spring Cloud Function Web의 사용 중단과 Spring Cloud Gateway로의 대체 등이 포함됩니다. 각 모듈의 세부 변경 사항은 GitHub에서 확인할 수 있으며, Maven과 Gradle을 통해 쉽게 시작할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/01/spring-cloud-2025-0-0-rc1-released)

## 🔹 Docker - Update on the Docker DX extension for VS Code
제목: VS Code용 Docker DX 확장 업데이트

요약: Visual Studio Code를 위한 새로운 Docker DX 확장이 출시된 지 몇 주가 지났습니다. 이번 출시는 컨테이너화된 애플리케이션을 개발하는 개발자들을 더 잘 지원하기 위해 Docker와 Microsoft 간의 깊은 협력을 반영합니다. 지난 몇 주 동안 VS Code의 Docker 확장 기능에 일부 변화가 있었을 것입니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - Java for AI
글 제목은 "Java for AI"입니다. 이 글에서는 AI의 요구를 충족할 수 있는 Java의 기존 및 미래 기능에 대해 설명합니다. 기존 기능에는 Foreign Function and Memory API와 Vector API가 포함됩니다. 미래 기능으로는 Project Valhalla와 Project Babylon에서 제안된 기능들이 있습니다. 이 비디오에서는 이러한 기능들이 Java 라이브러리와 애플리케이션에서 어떻게 활용되어 경쟁력 있는 AI 솔루션을 구축할 수 있는지를 논의합니다.
👉 [자세히 보기](https://inside.java/2025/05/03/javaone-java-ai/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
제목: testing.B.Loop을 통한 더 예측 가능한 벤치마킹  
요약: Go 1.24에서는 테스트와 벤치마크를 위한 새로운 루핑 메커니즘인 testing.B.Loop이 도입되었습니다. 이를 통해 벤치마크 테스트의 일관성과 예측 가능성이 향상되어 더 정확한 성능 측정이 가능합니다.  
링크: [Go 블로그](https://go.dev/blog/testing-b-loop)
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 이번 주 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 관한 논의에 참여하고 싶다면, 우리의 발표 세션과 Project Pavilion의 Helm 부스에서 유지 관리자들과 대화를 나누세요. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 아래 링크를 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

