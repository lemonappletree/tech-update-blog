# 🛠️ 2025-08-23 기술 업데이트 요약

## 🔹 Kubernetes - Tuning Linux Swap for Kubernetes: A Deep Dive
이 블로그 글에서는 Kubernetes v1.34에서 안정적으로 도입될 가능성이 있는 NodeSwap 기능을 다루고 있습니다. 이 기능은 전통적으로 성능 예측 가능성을 위해 비활성화되었던 스왑을 사용할 수 있게 하여, 리소스 활용을 개선하고 메모리 부족(OOM) 문제를 줄이는 데 목적을 두고 있습니다. Linux 노드에서 스왑을 조정하는 방법에 중점을 두고 있으며, 잘못된 설정은 성능 저하와 Kubelet의 퇴거 로직에 방해가 될 수 있음을 강조합니다.

글은 스왑 행동을 제어하는 주요 Linux 커널 매개변수(예: vm.swappiness, vm.min_free_kbytes, vm.watermark_scale_factor)를 탐구하고, 이러한 매개변수가 Kubernetes 워크로드 성능과 스왑 활용에 어떤 영향을 미치는지 설명합니다. 다양한 테스트 결과를 공유하며, 안정적이고 고성능의 Kubernetes 클러스터를 위한 최적 설정을 제안합니다.

테스트 결과, 기본 커널 매개변수 설정에서는 높은 메모리 압력 하에서 OOM 킬과 예기치 않은 노드 재시작이 발생할 수 있었습니다. 적절한 매개변수 조정을 통해 노드 안정성과 성능 간의 균형을 찾을 수 있었습니다. 스왑 활성화는 강력한 도구이지만, 성능 저하, 메모리 누수, 퇴거 비활성화의 위험이 있으므로 주의 깊은 조정이 필요합니다.

마지막으로, 글은 스왑을 활성화한 Linux 노드에 대한 추천 시작점을 제시하며, 테스트 환경에서 자체 워크로드로 벤치마크 테스트를 실행해볼 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/19/tuning-linux-swap-for-kubernetes-a-deep-dive/)

## 🔹 Spring Boot - Spring Modulith 2.0 M2, 1.4.3, and 1.3.9 released
Spring Modulith 2.0 M2, 1.4.3 및 1.3.9 버전이 출시되었습니다. 이 버전들은 일반적인 의존성 업그레이드와 몇 가지 사소한 개선 사항을 포함한 버그 수정 릴리스입니다. 2.0 M2 버전에서는 MongoDB 및 Neo4j에 대한 이벤트 게시 저장소 구현이 업데이트되었고, `ApplicationModulesEndpoint`의 부트스트랩 절차가 개선되었으며, Spring Boot 4.0 M2로 업그레이드되었습니다. 자세한 릴리스 정보는 각 버전의 변경 로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/08/22/spring-modulith-2-0-0-m2-1-4-3-and-1-3-9-released)

## 🔹 Docker - Prototyping an AI Tutor with Docker Model Runner
이 기술 블로그 글은 Docker의 Model Runner를 사용하여 AI 튜터를 프로토타입하는 방법에 대해 설명합니다. 글의 시작은 개발자들이 처음으로 'docker run hello-world' 명령어를 실행했을 때의 설렘과 놀라움을 회상하며 시작합니다. 글쓴이는 Docker의 Docs 팀에서 기술 작가로 일하면서 개발자 경험을 개선하기 위해 AI가 어떻게 활용될 수 있을지에 대해 고민하고 있다고 전합니다. 이 블로그 글은 AI가 Docker 사용 경험을 더 나은 방향으로 발전시킬 수 있는 가능성을 탐구합니다.
👉 [자세히 보기](https://www.docker.com/blog/how-to-build-an-ai-tutor-with-model-runner/)

## 🔹 Java - Growing the Java Language #JVMLS
블로그 글에서는 Brian Goetz가 2025년 JVM Language Summit에서 발표한 Java 언어의 발전에 대한 세션을 다루고 있습니다. Java 언어 아키텍트인 그는 Java의 지속적인 발전과 진화를 위한 방향성을 제시하며, 새로운 기능 및 개선 사항을 논의했습니다. 이러한 변화는 Java를 더욱 현대적이고 강력한 언어로 만들기 위한 노력의 일환이라고 요약할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/08/21/jvmls-growing-java-language/)

## 🔹 Golang - Container-aware GOMAXPROCS
이 블로그 글은 Go 1.25 버전에서 새롭게 도입된 GOMAXPROCS 기본값이 컨테이너 환경에서의 성능을 개선한다는 내용을 다루고 있습니다. GOMAXPROCS는 Go 런타임에서 동시에 실행할 수 있는 최대 프로세서 수를 설정하는 변수로, 이번 업데이트를 통해 컨테이너의 리소스를 보다 효율적으로 활용할 수 있게 되었습니다.
👉 [자세히 보기](https://go.dev/blog/container-aware-gomaxprocs)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대해 논의할 수 있는 기회가 마련되어 있으며, 유지관리자들과의 대화 세션 및 프로젝트 파빌리온에 위치한 Helm 부스에서 다양한 활동이 진행됩니다. 주간 동안의 Helm 관련 활동에 대한 자세한 정보는 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

